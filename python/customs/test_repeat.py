import asyncio

from repeat import repeat_every, arepeat


@repeat_every(seconds=1, max_repetitions=3)
async def aprint_decorated(a):
    print(a)


async def aprint(a, b=None):
    print(a, b)


if __name__ == "__main__":
    # test repeat_every
    asyncio.run(aprint_decorated("Hello, World!"))
    # test arepeat for a async function
    asyncio.run(
        arepeat(
            aprint,
            seconds=1,
            max_repetitions=3,
            args=["This is a test for arepeat!"],
            kwargs={"b": "This is a test for arepeat!"},
        )
    )
    # test arepeat for a sync function
    asyncio.run(
        arepeat(
            print,
            seconds=1,
            max_repetitions=3,
            args=["This is a test for arepeat with a sync function!"],
        )
    )
    # run in async gather
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(
            aprint_decorated("Hello, World!"),
            arepeat(
                aprint,
                seconds=1,
                max_repetitions=3,
                args=["This is a test for arepeat!"],
                kwargs={"b": "This is a test for arepeat!"},
            ),
            arepeat(  # this works as async even though it is a sync function
                print,
                seconds=1,
                max_repetitions=3,
                args=["This is a test for arepeat with a sync function!"],
            ),
        )
    )
