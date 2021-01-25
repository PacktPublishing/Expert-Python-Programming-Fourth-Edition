import aiohttp


async def get_rates(session: aiohttp.ClientSession, base: str):
    async with session.get(
        f"https://api.exchangeratesapi.io/latest?base={base}"
    ) as response:
        rates = (await response.json())['rates']
        rates[base] = 1.

        return base, rates
