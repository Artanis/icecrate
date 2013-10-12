from functools import partial

from pydispatch import dispatcher

from icecrate import database
from icecrate.utils import keygen

itemkey = partial(keygen, "icecrate", "items")

def all_items():
    return database.smembers(itemkey(meta="all"))

def by_item_id(item_id):
    """Retrieve an item from the database by it's id (UPC)

    """
    return database.hgetall(itemkey(item_id))

def save_item_data(item_id, data):
    """Save item data to the database.

    Fires the following signals:
    1. icecrate.items.preupdate
    2. icecrate.items.postupdate

    During pre-update, item data is mutable. Handlers of this event are
    free to modify the data. Order of handler execution is undefined.
    Keys and values must always be strings or numbers.

    When post-update is triggered, item data has already been inserted
    into the database. Postupdate sends only the item id, rather than
    full item data.

    """
    dispatcher.send("icecrate.items.preupdate", item=data)

    # icecrate.items.update
    database.hmset(itemkey(item_id), data)
    database.sadd(itemkey(meta="all"), item_id)
    
    dispatcher.send("icecrate.items.postupdate", item_id=item_id)
