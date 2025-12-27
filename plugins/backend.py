import time
import sys

print("Python engine Warming up...", flush=True)
i = 0
while True:
    time.sleep(2)
    print(f"Processing Data Batch #{i}", flush=True)
    i += 1