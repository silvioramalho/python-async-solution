from datetime import datetime
import time
import random
import asyncio
import aiohttp
import redis

URL = 'https://api.github.com/events'
MAX_THREADS = 100
redis = redis.Redis('localhost', port=6379, db=0, password='Redis2019!')


async def fetch_async(pid, session):
    start = datetime.now()
    sleepy_time = random.randint(2, 5)
    print('Async process start at {}, waiting for {} seconds'.format(
        start.strftime("%Y-%m-%d, %H:%M:%S"), sleepy_time))
    async with session.get(URL) as response:
        return await response.json()

@asyncio.coroutine
async def asynchronous():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        futures = [fetch_async(i, session) for i in range(1, MAX_THREADS + 1)]
        for i, future in enumerate(asyncio.as_completed(futures)):
            result = await future
            # Here we can make calculations
            if (type(result) is list):
                pos = random.randint(1, 10)
                data = result[pos].get('id')
            else:
                data = result.get('message')

            print('{} {}'.format(">>" * (i + 1), data))
            
            # Insert in REDIS LIST
            redis.rpush('dates', data)

    print("The process took: {:.2f} seconds".format(time.time() - start))

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
