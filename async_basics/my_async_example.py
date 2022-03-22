import asyncio


async def print_with_delay():
    print('Entered delay function')
    await asyncio.sleep(10)
    print('Finished delay function')


async def just_print():
    for _ in range(3):
        print('hehehe')


async def main():
    task_1 = asyncio.create_task(print_with_delay())
    task_2 = asyncio.create_task(just_print())

    await asyncio.gather(task_1, task_2)


if __name__ == '__main__':
    asyncio.run(main())
