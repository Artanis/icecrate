from operator import itemgetter

from pydispatch import dispatcher
import bottle

from icecrate import database
from icecrate import utils

app = bottle.Bottle()

@app.route("/")
@bottle.view("items_all.tpl")
def list_items():
    # get all item keys
    item_ids = database.smembers("icecrate:items.all")

    # resolve keys
    items = utils.resolve_item_ids(item_ids)

    # sort items by name
    items = sorted(items, key=itemgetter("name"))

    return {"items": items}

@app.route("/<upc>")
@bottle.view("items_one.tpl")
def show_item(upc):
    item = utils.resolve_item_id(upc)
    item_tags = utils.get_item_tags(upc)

    return {"item": dict(item, upc=upc), "tags": item_tags}

@app.route("/<upc>", method="POST")
def update_item(upc):
    # get the fields from the html form, and merge the upc into them
    fields = dict(bottle.request.forms, upc=upc)

    dispatcher.send(signal="icecrate.item.preupdate", item=fields)

    dispatcher.send(signal="icecrate.item.update", item=fields.items())

    bottle.redirect("/items/{0}".format(upc))

# handle events

def handle_item_update(item):
    item = dict(item)
    # insert item into database
    database.hmset(utils.itemkey(item.get("upc")), item)
    
    # add item to set of all items
    database.sadd("icecrate:items.all", item.get("upc"))

dispatcher.connect(handle_item_update,
    signal="icecrate.item.update")
