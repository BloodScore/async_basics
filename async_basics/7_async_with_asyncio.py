import asyncio


""" @asyncio.coroutine == async def (from python 3.5) 
    но вообще-то говоря первое создаёт из функции генератор, а второе - корутину 
    
    yield from заменили на await
    
    ensure_future == create_task
    
    loop = asyncio.create_loop()
    loop.run_until_complete(main())     ==      asyncio.run(main())
    loop.close()
"""


async def print_nums():
    num = 0
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    t = 0
    while True:
        if t % 3 == 0:
            print(f'{t} second have passed')
        t += 1
        await asyncio.sleep(1)


async def main():
    task_1 = asyncio.create_task(print_nums())
    task_2 = asyncio.create_task(print_time())

    await asyncio.gather(task_1, task_2)


if __name__ == '__main__':
    asyncio.run(main())
