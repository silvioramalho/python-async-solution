import asyncio
import asyncio_redis

@asyncio.coroutine
def example():
    # Create connection
    connection = yield from asyncio_redis.Connection.create(host='localhost', port=6379, db=0, password='Redis2019!')

    # Create subscriber.
    subscriber = yield from connection.start_subscribe()

    # Subscribe to channel.
    yield from subscriber.subscribe([ 'our-channel' ])

    # Inside a while loop, wait for incoming events.
    while True:
        reply = yield from subscriber.next_published()
        print('Received: ', repr(reply.value), 'on channel', reply.channel)

    # When finished, close the connection.
    connection.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())