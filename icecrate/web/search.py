import bottle

from icecrate import database
from icecrate import utils

app = bottle.Bottle()

@app.route("/")
@bottle.view("search_results")
def search():
    # item_ids = database.smembers("icecrate:items.all")

    # items = utils.resolve_item_ids(item_ids)

    query = bottle.request.query.get("q", "")
    return {"q": query}
