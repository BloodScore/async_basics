import asyncio
import time

import aiohttp
import requests


def get_file(url):
    response = requests.get(url, allow_redirects=True)
    return response


def save_file(response):
    filename = response.url.split('/')[-1]
    with open(f'downloaded_images/{filename}', 'wb') as file:
        file.write(response.content)


def sync_main():
    url = 'https://via.placeholder.com/150'

    for _ in range(10):
        save_file(get_file(url))


def write_file(data):
    filename = f'downloaded_images/file-{int(time.time() * 1000)}.jpg'
    with open(filename, 'wb') as file:
        file.write(data)


async def async_get_file(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        # write_file(data)


async def async_main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            task = asyncio.create_task(async_get_file(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    sync_main()      # 4-6 seconds
    # asyncio.run(async_main())

    print(f'Done in {time.time() - start} seconds')
