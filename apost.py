#!/usr/bin/env python3
# apost.py

"""Asynchronously POST to web url"""

import asyncio
import sys
import urllib.error
import urllib.parse

import aiohttp

from async_poster import AsyncPoster

def foo():
    print("foo")
    
async def main():

    a = AsyncPoster()

    # Define a global timeout for HTTP requests of 10 seconds
    http_timeout = aiohttp.ClientTimeout(total=10)

    # Create a common ClientSession object to be used by all HTTP
    async with aiohttp.ClientSession(timeout=http_timeout) as session:
        for i in range(3):
            print(i, "foo")
            if i == 0:
                asyncio.ensure_future(a.get("http://forsterlewis.com", session))
            if i == 1:
                asyncio.ensure_future(a.get("http://smartcambridgex.org", session))
            if i == 2:
                asyncio.ensure_future(a.get("https://github.com", session))

        await asyncio.sleep(10)

    print("main() completed")

def handle_exception(loop, context):
    # context["message"] will always be there; but context["exception"] may not
    msg = context.get("exception", context["message"])
    print(f"Caught exception: {msg}")

if __name__ == "__main__":
    
    # Python 3.7
    # assert sys.version_info >= (3, 7), "Script requires Python 3.7+."

    # Python 3.7
    #asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))

    # Python 3.6
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handle_exception)
    loop.run_until_complete(main())

