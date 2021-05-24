"""
"Asynchronous programming" section example showing simple
asynchronous printing of numbers sequence.

"""
import asyncio
import random


async def print_number(number):
    await asyncio.sleep(0)
    print(number)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.gather(*[print_number(number) for number in range(10)])
    )
    loop.close()
