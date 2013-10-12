from functools import partial

from pydispatch import dispatcher

from icecrate import database
from icecrate import items
from icecrate.utils import keygen

tagkey = partial(keygen, "icecrate", "tags")

def all_tags():
    return database.smembers(tagkey(meta="all"))

def by_item_id(item_id):
    """Retrieves tag information for all tags attached to the item.

    """
    item = items.by_item_id(item_id)
    item_tags = _split_tags(item.get("tags", ""))
    yield from map(by_tag_id, item_tags)

def by_tag_id(tag_id):
    """Retrieves tag information.

    """
    tag = database.hgetall(tagkey(tag_id))
    members = database.smembers(tagkey(tag_id, meta="all"))

    return (tag, members)

def _split_tags(tags_field):
    """Split a tag string and return a set of tag IDs.

    Empty tags and duplicates are filtered out.

    """
    return set(filter(None, (tag.strip() for tag in tags_field.split(","))))

# handle events

def handle_item_preupdate(item):
    tags = item.get("tags", "")

    # filter duplicates and empties out of tag list
    tags = _split_tags(tags)

    # echo filtered tag list back to item
    item["tags"] = ", ".join(tags)

    for tag in tags:
        # save tag name
        database.hset(tagkey(tag), "name", tag)

        # add item upc to tag members
        database.sadd(tagkey(tag, meta="all"), item.get("upc"))

        # add tag to set of all tags
        database.sadd(tagkey(meta="all"), tag)

dispatcher.connect(handle_item_preupdate,
    signal="icecrate.items.preupdate")
