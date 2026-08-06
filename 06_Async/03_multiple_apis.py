import asyncio

async def api_call(url:str, delay:int):
    print(f"fetching data from {url}...")
    await asyncio.sleep(delay)  # Simulate an API call that takes the specified delay
    print(f"data fetched from {url}")
    return f"{url} data"

async def main():
    await asyncio.gather(
    api_call("https://api.example.com/data1", 2),
    api_call("https://api.example.com/data2", 3),
    api_call("https://api.example.com/data3", 1),
)

    print("fetching completed")
 

# Run the async function
asyncio.run(main())