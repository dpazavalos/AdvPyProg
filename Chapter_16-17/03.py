from math import sqrt
import asyncio


async def check_prime(x: int) -> None:
    """Stdout prime checker, calls on Prime check logic function"""
    is_prime = None
    if (x < 2) or (x == 2) or (x % 2 == 0):
        is_prime = False
    while is_prime is None:
        max = int(sqrt(x)) + 1
        for i in range(3, max, 2):
            if is_prime is None:
                if x % i == 0:
                    is_prime = False
                elif i % 1_000_000 == 1:
                    await asyncio.sleep(0)
        if is_prime is None:
            is_prime = True
    if is_prime:
        print("✔:", x)
    else:
        print("❌:", x)


async def asyncio_man() -> None:
    """Asyncio manager. Creates tasks, holds in await"""
    t1 = asyncio.create_task(check_prime(9637529763296797))
    t2 = asyncio.create_task(check_prime(427920331))
    t3 = asyncio.create_task(check_prime(157))
    await asyncio.wait([t1, t2, t3])


def main() -> None:
    """Primary try loop, handles exceptions. closes global loop"""
    try:
        asyncio.run(asyncio_man())
    except Exception as e:
        print(e)


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
    main()
    time_stop()
