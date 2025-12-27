import asyncio
import json
import sys
from core.logger import Logger

class Dispatcher:
    def __init__(self, manifest_path):
        self.manifest_path = manifest_path
        self.processes = []
        self.signals = {} # Stores asyncio.Events

    def load_manifest(self):
        try:
            with open(self.manifest_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Config not found at {self.manifest_path}")
            sys.exit(1)

    async def run_service(self, service):
        name = service['name']
        cmd = service['command']
        color = service.get('color', "")
        ready_signal = service.get('ready_signal')
        depends_on = service.get('depends_on')

        # 1. Wait for dependencies
        if depends_on:
            if depends_on in self.signals:
                print(f"... {name} is waiting for {depends_on} ...")
                await self.signals[depends_on].wait()
            else:
                print(f"Error: {name} depends on unknown service: {depends_on}")
                return

        print(f"Checking processes for {name}...")
        process = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        self.processes.append(process)

        # We pass the event signal if this service has a 'ready_signal'
        event_trigger = self.signals[name] if name in self.signals else None

        await asyncio.gather(
            Logger.stream_output(process.stdout, name, color, ready_signal, event_trigger),
            Logger.stream_output(process.stderr, f"{name}-ERR", "\u001b[31m")
        )
        
        await process.wait()

    async def start(self):
        config = self.load_manifest()
        tasks = []

        print(f"Turbostar script initializing...")
        
        # Initialize events (signals) for dependency tracking
        for s in config['services']:
            if 'ready_signal' in s:
                self.signals[s['name']] = asyncio.Event()

        # Create tasks
        for service in config['services']:
            tasks.append(self.run_service(service))

        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            print("\n🛑 ERROR -- Something went wrong...")

    def shutdown(self):
        print("\nShutting down...")
        for p in self.processes:
            try:
                p.terminate()
            except ProcessLookupError:
                pass
        sys.exit(0)