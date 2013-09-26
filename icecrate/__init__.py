import os.path

import redis

# TEMP CONFIG
HOST = "localhost"
PORT = 6379
DB   = 0

database = redis.StrictRedis(host=HOST, port=PORT, db=DB, decode_responses=True)
