import aiohttp
import asyncio


async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        return await res.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, 'http://packtpub.com')
        with open('output/html.html', 'w') as f:
            f.write(html)

if __name__ == '__main__':
    asyncio.run(main())
