import asyncio

async def factorial(num):
    f = 1

    for i in range(2, num + 1):
        print("Asyncio. Task: Compute factorial(%s)" % (i))
        await asyncio.sleep(1)
        f *= i
    print("Asyncio. Task - factorial(%s) = %s" % (num, f))


async def fabnacci(num):
    a, b = 0, 1

    for i in range(num):
        print("Asyncio. Task: Compute fabnacci (%s)" % (i))
        await asyncio.sleep(1)
        a, b = b, a + b

    print("Asyncio. Task: fabnacci(%s) = %s" % (num, a))


async def binomialCoef(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print("Asyncio. Task: Computer binomialCoef (%s)" % (i))
        await asyncio.sleep(1)

    print("Asyncio. Task: binomialCoef (%s, %s) = %s" % (n, k, result))


if __name__ == "__main__":
    tasks = [asyncio.Task(factorial(10)),
             asyncio.Task(fabnacci(10)),
             asyncio.Task(binomialCoef(20, 10))]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

