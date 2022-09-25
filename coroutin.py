import asyncio
import time
async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(f"{what}-{delay}-这是内部")
    return f"{what}-{delay}"

async def main():
    task1 = asyncio.create_task(say_after(2,"hello"))
    task2 = asyncio.create_task(say_after(1 ,"world"))
    print(f"start at {time.strftime('%X')}")
    # ret = await asyncio.gather(
    #     say_after(2,"hello"),
    #     say_after(1,"world")
    # )
    res1 = await task1
    res2 = await task2
    print(res1)
    print(res2)
    print(f"finished at {time.strftime('%X')}")
    
if __name__ == "__main__":
    asyncio.run(main())