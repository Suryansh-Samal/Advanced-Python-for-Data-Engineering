import asyncio
import time

#first task
async def api_call(url:str, delay:int):
    print(f"fetching data from {url}...")
    await asyncio.sleep(delay)  # Simulate an API call that takes the specified delay
    print(f"data fetched from {url}")
    return f"{url} data"

#second task
async def execution():
    time.sleep(5)  # Simulate a blocking operation that takes 5 seconds
    print("Task execution completed")

#third task
async def transformation():
    asyncio.sleep(4)  # Simulate a non-blocking operation that takes 4 seconds
    print("Data transformation completed")


async def main():
    await asyncio.gather(
    api_call("https://api.example.com/data1", 3),
    execution(),
    transformation()
)

    print("All the tasks are completed")
 

# Run the async function
asyncio.run(main())