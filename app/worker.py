import time
import random

def worker_loop():
    while True:
        print("[Worker] Waiting for incoming tasks...")
        time.sleep(3)
        print("[Worker] No queued tasks right now.")

if __name__ == "__main__":
    worker_loop()
