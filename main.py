import asyncio
import inspect

from config import ENDLESS_MENU


from provider import get_module


async def run_option(methods: list):
    for method in methods:
        if callable(method):
            if inspect.iscoroutinefunction(method):
                await method()
            else:

                method()
        else:
            print(f"Object {method} is not callable")


async def startup():
    try:
        while True:

            module = input("Module: ")
            if not module.isdigit():
                print("Wrong module format. It should be number")

            if module == "0":
                print("Shutting down. Bye!")
            else:
                print(f"Start module {module}")

            worker = get_module(module)
            if not worker:
                print("Wrong module number")

            await run_option(worker)

            if not ENDLESS_MENU:
                exit()

    except Exception as e:
        print(e)


asyncio.run(startup())
