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

    tags = sorted(tags, key=itemgetter("name"), reverse=True)

    return {"tags": tags}

@app.route("/<tag_id>")
@bottle.view("tags_one.tpl")
def show_tag(tag_id):
    taginfo = icecrate.tags.by_tag_id(tag_id)

    # get tag members from indexer
    members = list(icecrate.search.query("tags:{0}".format(tag_id)))

    return {"taginfo": taginfo , "members": members}
