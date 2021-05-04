#!/usr/bin/env python3

import concurrent.futures
import time

# race example
# The difference is that each of the threads is
# accessing the same global variable counter and incrementing it.
# Counter is not protected in any way, so it is not thread-safe.

counter = 0


def increment_counter(fake_value):
    global counter
    for _ in range(100):
        counter += 1


if __name__ == "__main__":
    start_time = time.time()
    fake_data = [x for x in range(5000)]
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
        executor.map(increment_counter, fake_data)
    duration = time.time() - start_time
    print(f"Racing exmaple took {duration} seconds")
