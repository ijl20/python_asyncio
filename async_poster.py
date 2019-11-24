
import aiofiles
import aiohttp

class AsyncPoster(object):

    def __init__(self):
        print("AsyncPoster init")

    async def get(self, url, session):

        print("AsyncPoster post", url)

        resp = await session.request(method="GET", url=url)
        resp.raise_for_status()
        print("Got response [%s] for URL: %s", resp.status, url)
        html = await resp.text()
        return html

    async def write_file(self, filename, write_str):
        """Write write_str to `file` filename."""
        async with aiofiles.open(file, "a") as f:
            await f.write(write_str+"\n")
            print("Wrote {} to {}".format(write_str, filename))
