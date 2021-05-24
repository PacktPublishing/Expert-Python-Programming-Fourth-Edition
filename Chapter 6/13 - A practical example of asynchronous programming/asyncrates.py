import aiohttp


async def get_rates(session: aiohttp.ClientSession, base: str):
    async with session.get(f"https://api.vatcomply.com/rates?base={base}") as response:
        rates = (await response.json())["rates"]
        rates[base] = 1.0

        return base, rates
