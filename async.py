import asyncio

# FUNCTION 1
async def main():
    # means that once processor will have a idle time it will call other_function()
    task = asyncio.create_task(other_function())

    print("A")

    # execution will move to other_function()
    await asyncio.sleep(1) 
    
    print("B")

    # this will wait for other_function() to complete from the line where it left
    return_value = await task

    # print returned value
    print(f"Return value is : {return_value}")

# FUNCTION 2
async def other_function():
    print("1")

    # execution will move back to main() where it left
    await asyncio.sleep(2)
    
    print("2")
    return 10
    
asyncio.run(main())