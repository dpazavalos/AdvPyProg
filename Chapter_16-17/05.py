from math import sqrt
import asyncio
from concurrent.futures import ProcessPoolExecutor
from timeit import default_timer as timer


def _is_prime(x: int):
    if (x < 2) or (x == 2) or (x % 2 == 0):
        return False
    roof = int(sqrt(x)) + 1
    for i in range(3, roof, 2):
        if x % i == 0:
            return False
        return True


def check_prime(x: int) -> None:
    """Stdout prime checker, calls on Prime check logic function"""
    if _is_prime(x):
        print("✔:", x)
    else:
        print("❌:", x)


async def main():
    tasks = [
        loop.run_in_executor(executor, check_prime, 9637529763296797),
        loop.run_in_executor(executor, check_prime, 427920331),
        loop.run_in_executor(executor, check_prime, 157)
    ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = timer()
    executor = ProcessPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        stop = timer() - start
        print(f"Took {format(stop, 'f')} seconds")
    except Exception as e:
        print(e)
    finally:
        loop.stop()
        loop.close()
