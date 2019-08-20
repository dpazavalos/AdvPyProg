import aiohttp
import aiofiles
import asyncio
import os


async def download_html(session: aiohttp.ClientSession, url: str):
    # Get http
    async with session.get(url, ssl=False) as res:
        filename = f'output/{os.path.basename(url)}.html'
        # Async write to file, using url as filename
        async with aiofiles.open(filename, 'wb') as f:
            while True:
                chunk = await res.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)
    return await res.release()


async def async_man(url):
    async with aiohttp.ClientSession() as session:
        await download_html(session, url)


def time_start():
    from timeit import default_timer as timer
    global start, timer
    start = 0.0
    start = timer()


def time_stop():
    global start
    stop = timer() - start
    print(f"Took {format(stop, 'f')} seconds")


def main():
    urls = [
        'http://packtpub.com',
        'http://python.org',
        'http://docs.python.org/3/library/asyncio',
        'http://aiohttp.readthedocs.io',
        'http://google.com'
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(*[async_man(url) for url in urls])
    )


if __name__ == '__main__':
    time_start()
    main()
    time_stop()
