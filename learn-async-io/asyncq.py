import asyncio
import itertools as it
import os
import random
import time


# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[37m",
    "\033[38m",
    "\033[39m",
)


async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()


async def randsleep(a: int = 1, b: int = 5, caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(c[0] + f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(c[name + 1] + f"Producer {name} added <{i}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(c[name + 1] + f"Consumer {name} got element <{i}>"
              f" in {now-t:0.5f} seconds.")
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--nprod",
        type=int,
        default=5,
    )
    parser.add_argument(
        "-c",
        "--ncon",
        type=int,
        default=10,
    )

    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(c[0] + f"Program completed in {elapsed:0.5f} seconds.")
