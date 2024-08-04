import asyncio

from repeat import repeat


@repeat(seconds=1)
async def aprint(a):
    print(a)


if __name__ == "__main__":
    asyncio.run(aprint("Hello, World!"))
