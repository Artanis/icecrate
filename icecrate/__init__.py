import os.path

from xdg import BaseDirectory
import redis

from icecrate.utils import keygen
from icecrate._version import __version__, __version_info__

__db_version__ = "1"

# TEMP CONFIG
HOST = "localhost"
PORT = 6379
DB   = 0
INDEXDIR = BaseDirectory.save_cache_path("icecrate")

database = redis.StrictRedis(host=HOST, port=PORT, db=DB, decode_responses=True)
database.set(keygen("icecrate", meta="version"), __version__)
database.set(keygen("icecrate", meta="dbversion"), __db_version__)

import icecrate.items
import icecrate.tags
import icecrate.search
