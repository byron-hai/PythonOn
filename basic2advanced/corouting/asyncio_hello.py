import asyncio

async def main():
    print("Hello...")
    await asyncio.sleep(2)
    for i in range(100):
        print(i)
    print("...World")


asyncio.run(main())

