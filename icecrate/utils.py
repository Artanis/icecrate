from icecrate import database

itemkey = "icecrate:items:{0}".format
tagkey =  "icecrate:tags:{0}".format
taginfo = "icecrate:tags:{0}.meta".format

def resolve_item_id(item_id):
    return database.hgetall(itemkey(item_id))

def resolve_item_ids(item_ids):
    yield from map(resolve_item_id, item_ids)

def get_item_tags(item_id):
    item = resolve_item_id(item_id)
    item_tags = split_item_tags(item.get("tags", ""))
    yield from map(resolve_tag_id, item_tags)

def resolve_tag_id(tag_id):
    return database.hgetall(taginfo(tag_id))

def resolve_tag_members(tag_id):
    yield from resolve_item_ids(database.smembers(tagkey(tag_id)))

def split_item_tags(tags_field):
    return set(filter(None, (tag.strip() for tag in tags_field.split(","))))
