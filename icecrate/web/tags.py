from operator import itemgetter

from pydispatch import dispatcher
import bottle

import icecrate.tags
from icecrate import database
from icecrate import utils

app = bottle.Bottle()

@app.route("/")
@bottle.view("tags_all")
def list_tags():
    tags = list(map(icecrate.tags.by_tag_id, icecrate.tags.all_tags()))

    print(tags)

    tags = sorted(tags, key=lambda a: len(a[1]), reverse=True)

    return {"tags": tags}

@app.route("/<tag_id>")
@bottle.view("tags_one.tpl")
def show_tag(tag_id):
    taginfo, members = icecrate.tags.by_tag_id(tag_id)

    members = map(icecrate.items.by_item_id, members)

    members = sorted(members, key=itemgetter("name"))

    return {"taginfo": taginfo, "members": members}
