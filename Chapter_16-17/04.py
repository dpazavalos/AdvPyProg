from concurrent.futures import ThreadPoolExecutor
import asyncio
import time

start = time.perf_counter()


def count_down(char, delay):
    indents = (ord(char) - ord('A')) * '\t'
    n = 3
    while n:
        time.sleep(delay)
        duration = time.perf_counter() - start
        print('-' * 40)
        print(f"{format(duration, 'f')}\t{indents}{char}={n}")
        n -= 1


async def main():
    futures = [loop.run_in_executor(
        executor,
        count_down,
        *args
    ) for args in [('A', 1), ('B', 0.8), ('C', 0.5)]]

    await asyncio.gather(*futures)
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


time_start()
executor = ThreadPoolExecutor(max_workers=3)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
time_stop()
