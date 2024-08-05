import asyncio

from repeat import repeat_every, arepeat


@repeat_every(seconds=1, max_repetitions=3)
async def aprint_decorated(a):
    print(a)


async def aprint(a, b=None):
    print(a, b)


if __name__ == "__main__":
    asyncio.run(aprint_decorated("Hello, World!"))
    asyncio.run(
        arepeat(
            aprint,
            seconds=1,
            max_repetitions=3,
            args=["This is a test for arepeat!"],
            kwargs={"b": "This is a test for arepeat!"},
        )
    )
