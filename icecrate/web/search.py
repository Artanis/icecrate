import bottle

import icecrate.search
import icecrate.items
from icecrate import database
from icecrate import utils

app = bottle.Bottle()

@app.route("/")
@bottle.view("search_results")
def search():
    q = bottle.request.query.get("q", "")

    items = list(map(lambda a: icecrate.items.by_item_id(a.get("upc")),
        icecrate.search.query(q)))

    return {"q": q, "results": items}
