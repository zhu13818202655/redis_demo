import redis
from random import random

import time
start = time.time()
conn = redis.Redis(host='localhost', port=6379, decode_responses=True, db=0)


# for i in range(100*100*100):
#     conn.set(int(random()*10000000000), int(random()*10000000000))


# for i in range(1000000):
#     conn.delete(conn.randomkey())


for i in range(1000000, 2000000):
    field = str(i)[:5]
    keys = str(i)[2:]
    value = int(random()*10000000000)
    conn.hset(field, keys, value)
print(time.time()-start)
