"""
"Asynchronous programming" section example showing how
two coroutines cooperate by releasing control to event
loop on blocking calls.

"""
import asyncio
import random


async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print(f"{name} waited {time_to_sleep} seconds")


async def main():
    await asyncio.gather(waiter("first"), waiter("second"))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
