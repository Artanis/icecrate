from operator import itemgetter

import bottle
import transaction
from dobbin.persistent import checkout, PersistentDict

from icecrate.database import inventory

app = bottle.Bottle()

@app.route("/")
@bottle.view("list_items")
def list_items():
    # print("="*40)
    # for upc, row in inventory.items():
    #     try:
    #         print(upc, dict(row))
    #     except ValueError:
    #         print(upc, row)
    #     print("="*40)

    items = (dict(row, upc=upc) for upc, row in inventory.items())
    return {"items": sorted(items, key=itemgetter("name"))}

@app.route("/<upc>")
@bottle.view("show_item")
def show_item(upc):
    try:
        item = dict(inventory[upc])
        in_db = True
    except KeyError:
        item = dict()
        in_db = False

    return dict(item=item, upc=upc, in_db=in_db)

@app.route("/<upc>", method="POST")
def update_item(upc):
    try:
        item = inventory[upc]
        checkout(item)
    except KeyError:
        item = PersistentDict()

    name, tags, qty = map(bottle.request.forms.get, ("name", "tags", "quantity"))

    # print(repr(upc), repr(name), repr(tags), repr(qty))
    
    item["name"] = name
    item["tags"] = tags
    item["quantity"] = qty

    checkout(inventory)
    inventory[upc] = item
    transaction.commit()

    bottle.redirect("/items/{0}".format(upc))
