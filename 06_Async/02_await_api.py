import asyncio

async def api_call():
    await asyncio.sleep(3)  # Simulate an API call that takes 2 seconds
    return "API response"

async def execute_api_call():
    print("Calling API...")
    response = await api_call()  # Await the result of the API call
    print(f"Received response: {response}")

# Run the async function
asyncio.run(execute_api_call())