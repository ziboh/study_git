from contextlib import contextmanager, asynccontextmanager
import asyncio
import time


@contextmanager
def MyOpen(filename):
    f = open(filename, "rb")
    try:
        yield f
    finally:
        f.close()


@asynccontextmanager
async def AsyncMyOpen(filename, delay):
    await asyncio.sleep(delay=delay)
    f = open(filename, "rb")
    try:
        yield f
    finally:
        f.close()


def my_generator(num: int):
    tmp = 1
    while num > 0:
        yield tmp
        num -= 1
        tmp += 1


async def put_file_contnet(filename, delay):
    async with AsyncMyOpen(filename, delay) as f:
        current_task = asyncio.current_task()
        # print(id(current_task), current_task.get_name(), "\n", asyncio.all_tasks())
        print(f"AsyncMyOpen----{delay}".ljust(30, "-"), f.read(),)


async def taskalways(filename, mg):
    while True:
        try:
            delay = next(mg)
            print(f"delay = {delay} start at {time.strftime('%X')}")

        except StopIteration:
            break
        task = asyncio.create_task(put_file_contnet(
            filename, delay), name=f"task{delay}")
        # task.print_stack()
        await task
        print(f"delay = {delay} finshed at {time.strftime('%X')}")


class Myopen_class():
    def __new__(cls,*args, **kwargs):
        print("创建了实例",cls,*args, **kwargs)
        instance = object.__new__(cls)
        print(instance)
        return instance
    def __init__(self, filename) -> None:
        print("接收参数：",filename)
        self.filename = filename

    def __enter__(self):
        self.f = open(self.filename, "rb")
        print("打开了文件")
        return self.f

    def __exit__(self, *exc):
        print(*exc)
        self.f.close()
        print("关闭了文件")
        return True

async def main():
    mg = my_generator(10)
    filename = "3.txt"
    print(f"in main start at {time.strftime('%X')}")

    await asyncio.gather(taskalways(filename, mg), taskalways(filename, mg))

    print(f"in main finshed at {time.strftime('%X')}")

if __name__ == "__main__":
    # with MyOpen("3.txt") as f:
    #     print("MyOpen".ljust(30, "-"), f.read())
    with Myopen_class("3.txt") as f:
        print("Myopen_class".ljust(30, "-"), f.read())
        a = 1/0
    # asyncio.run(main())
