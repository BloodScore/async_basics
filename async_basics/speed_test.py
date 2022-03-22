import asyncio
import time


def delayed_func():
    time.sleep(5)
    print('SUS')


def sync_main():
    for _ in range(5):
        delayed_func()


async def async_delayed_func():
    await asyncio.sleep(5)
    print('SUS')


async def async_main():
    tasks = []

    for _ in range(5):
        task = asyncio.create_task(async_delayed_func())
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()

    # sync_main()
    asyncio.run(async_main())

    print(f'Done in {time.time() - start} seconds')
