import asyncio
import time

#coroutine function
async def main():
    print("hello") #This will be printed immediately
    asyncio.sleep(3) #The thread is idle here
    print("world")#This will be executed right after the thread is idle

async def main_():
    print("hello") #This will be printed immediately
    await asyncio.sleep(3) #The thread is idle here but will not block the event loop
    print("world")#This will be executed after the wait time is over that is 3 seconds

#Run the main coroutine
asyncio.run(main_())