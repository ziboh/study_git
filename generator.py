import asyncio

async def say_after(delay,what):
    await asyncio.sleep(1)
    return f"{what}-{delay}"

async def main():
    print("start at {time.strftime('%x')}")
    ret = asyncio.gather(
        say_after(2,"hello"),
        say_after(1,"world"),
    )
    print("finished at {time.strftime('%x')}")
    
if __name__ == "__main__":
    asyncio.run(main())