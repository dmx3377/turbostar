import asyncio

# ANSI Color Codes
RESET = "\u001b[0m"
COLORS = {
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m"
}

class Logger:
    def __init__(self):
        pass

    @staticmethod
    async def stream_output(stream, service_name, color_code, ready_signal=None, event=None):
        """
        Reads line-by-line from a subprocess stream and prints it.
        Triggers an asyncio.Event if ready_signal is found.
        """
        while True:
            line = await stream.readline()
            if line:
                decoded = line.decode('utf-8').strip()
                # Print the formatted log
                print(f"{color_code}[{service_name}]{RESET} {decoded}")

                # Check for signals
                if ready_signal and event and ready_signal in decoded:
                    if not event.is_set():
                        print(f"{RESET}>>> Signal acquired: {service_name} is READY.{RESET}")
                        event.set()
            else:
                break