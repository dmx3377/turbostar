import asyncio
import os
import argparse
from core.dispatcher import Dispatcher

def main():
    parser = argparse.ArgumentParser(description="Turbostar Process Orchestrator")
    parser.add_argument("--config", default="configs/manifest.json", help="Path to the manifest file")
    args = parser.parse_args()
    if not os.path.exists(args.config):
        print(f"Configuration file not found: {args.config}")
        return
#init core logic
    engine = Dispatcher(args.config)
    try:
        asyncio.run(engine.start())
    except KeyboardInterrupt:
        engine.shutdown()

if __name__ == "__main__":
    main()