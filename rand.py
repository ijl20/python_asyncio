#!/usr/bin/env python3
# rand.py

import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    res = await asyncio.gather( makerandom(0, 9),
                                makerandom(1, 8),
                                makerandom(2, 7)
          )

    return res

if __name__ == "__main__":
    random.seed(444)

    # Python 3.6
    loop = asyncio.get_event_loop()
    r1, r2, r3 = loop.run_until_complete(main())

    # Python 3.7
    # r1, r2, r3 = asyncio.run(main())

    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

