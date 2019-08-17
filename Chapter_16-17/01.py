from math import sqrt
import asyncio

# Global asyncio event loop
loop = asyncio.get_event_loop()



def _primecheck(x) -> bool:
    """Prime check logic"""
    if (x < 2) or (x == 2) or (x % 2 == 0):
        return False
    max = int(sqrt(x)) + 1
    for i in range(3, max, 2):
        if x % i == 0:
            return False
    return True


async def check_prime(x: int) -> None:
    """Stdout prime checker, calls on Prime check logic function"""
    is_prime = _primecheck(x)
    if is_prime:
        print("✔:", x)
    else:
        print("❌:", x)


async def asyncio_man() -> None:
    """Asyncio manager. Creates tasks, holds in await"""
    t1 = loop.create_task(check_prime(9637529763296797))
    t2 = loop.create_task(check_prime(427920331))
    t3 = loop.create_task(check_prime(157))
    await asyncio.wait([t1, t2, t3])


def main() -> None:
    """Primary try loop, handles exceptions. closes global loop"""
    try:
        # Loop already created as global. Run
        loop.run_until_complete(asyncio_man())
    except Exception as e:
        print(e)
    finally:
        loop.stop()
        loop.close()


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
