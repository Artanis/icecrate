from operator import itemgetter

import bottle

from icecrate import database

app = bottle.Bottle()

itemkeyfmt = "icecrate:items:{0}".format
itemtagfmt = "icecrate:tags:{0}".format

@app.route("/")
@bottle.view("list_items")
def list_items():
    # get all item keys
    item_ids = database.smembers("icecrate:items.all")

    # resolve keys
    items = list(map(database.hgetall, item_ids))

    # sort items by name
    items = sorted(items, key=itemgetter("name"))

    return {"items": items}

@app.route("/<upc>")
@bottle.view("show_item")
def show_item(upc):
    item = database.hgetall(itemkeyfmt(upc))

    return dict(item=item, upc=upc)

@app.route("/<upc>", method="POST")
def update_item(upc):
    # get the fields from the html form, and merge the upc into them
    fields = dict(bottle.request.forms, upc=upc)

    # split tags and filter empty strings
    tags = (tag.strip() for tag in fields.get("tags", "").split(","))
    tags = set(filter(None, tags))
    for tag in tags:
        # add tag to set of all tags
        database.sadd("icecrate:tags.all", tag)

        # add item key to set of items in the tag
        database.sadd(itemtagfmt(tag), itemkeyfmt(upc))

    # apply uniqueness to the tags field
    fields["tags"] = ", ".join(tags)

    # insert item into database
    database.hmset(itemkeyfmt(upc), fields)

    # add item to set of all items
    database.sadd("icecrate:items.all", itemkeyfmt(upc))

    bottle.redirect("/items/{0}".format(upc))
