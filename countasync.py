#!/usr/bin/env python3
# countasync.py

import asyncio

async def count(i):
    print(i,"One")
    await asyncio.sleep(1)
    print(i,"Two")

async def main():
    await asyncio.gather(count(1), count(2), count(3))

if __name__ == "__main__":
    import time
    s = time.perf_counter()

    # Python 3.7+
    # asyncio.run(main())

    # Python 3.6
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

