import time
import asyncio

# global perf count time start
start = time.perf_counter()


async def count_down_sleep(name: str, delay):
    indents = (ord(name) - ord('A')) * '\t'
    n = 3
    while n:
        time.sleep(delay)
        duration = time.perf_counter() - start
        print('-'*40)
        print(f"{format(duration, 'f')}\t{indents}{name}={n}")
        n -= 1


async def count_down_wait(name, delay):
    indents = (ord(name) - ord('A')) * '\t'
    n = 3
    while n:
        await asyncio.sleep(delay)
        duration = time.perf_counter() - start
        print('-' * 40)
        print(f"{format(duration, 'f')}\t{indents}{name}={n}")
        n -= 1


def main_wait():
    print('Running with wait')
    loop = asyncio.get_event_loop()
    tasks = {
        loop.create_task(count_down_wait('A', 1)),
        loop.create_task(count_down_wait('B', 0.8)),
        loop.create_task(count_down_wait('C', 0.5))
    }
    # start perf time
    loop.run_until_complete(asyncio.wait(tasks))
    print('-' * 40)
    print('Done')


def main_sleep():
    print('Running with sleep')
    loop = asyncio.get_event_loop()
    tasks = {
        loop.create_task(count_down_sleep('A', 1)),
        loop.create_task(count_down_sleep('B', 0.8)),
        loop.create_task(count_down_sleep('C', 0.5))
    }
    # start perf time
    loop.run_until_complete(asyncio.wait(tasks))
    print('-' * 40)
    print('Done')


def time_start():
    from timeit import default_timer as timer
    global start, timer
    start = 0.0
    start = timer()


def time_stop():
    global start
    stop = timer() - start
    print(f"Took {format(stop, 'f')} seconds")


if __name__ == '__main__':
    time_start()
    main_wait()
    time_stop()

    time_start()
    main_sleep()
    time_stop()
