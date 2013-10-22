from operator import itemgetter

import bottle

import icecrate.items
import icecrate.tags
from icecrate import database
# from icecrate import utils

app = bottle.Bottle()

@app.route("/")
@bottle.view("items_all.tpl")
def list_items(): # pragma: no cover
    # get all item keys
    item_ids = icecrate.items.all_items()

    # resolve keys
    items = map(icecrate.items.by_item_id, item_ids)

    # sort items by name
    items = sorted(items, key=itemgetter("name"))

    return {"items": items}

@app.route("/<upc>")
@bottle.view("items_one.tpl")
def show_item(upc):
    item = icecrate.items.by_item_id(upc)

    print(item.get("tags"))

    return {"item": dict(item, upc=upc)}

@app.route("/<upc>", method="POST")
def update_item(upc):
    # get the fields from the html form, and merge the upc into them
    fields = dict(bottle.request.forms, upc=upc)

    icecrate.items.save_item_data(upc, fields)

    bottle.redirect("/items/{0}".format(upc))
