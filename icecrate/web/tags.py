from operator import itemgetter

from pydispatch import dispatcher
import bottle

from icecrate import database
from icecrate import utils

app = bottle.Bottle()

alltags = "icecrate:tags.all"

@app.route("/")
@bottle.view("tags_all")
def list_tags():
    tags = database.smembers("icecrate:tags.all")

    tags = sorted(tags)

    return {"tags": tags}

@app.route("/<tag_id>")
@bottle.view("tags_one.tpl")
def show_tag(tag_id):
    tag = utils.resolve_tag_id(tag_id)
    members = list(utils.resolve_tag_members(tag_id))

    return {"tag": tag, "members": members}

# handle events
def handle_item_preupdate(item):
    tags = item.get("tags", "")

    # filter duplicates and empties out of tag list
    tags = utils.split_item_tags(tags)

    # echo filtered tag list back to item
    item["tags"] = ", ".join(tags)

    for tag in tags:
        # save tag name
        database.hset(utils.taginfo(tag), "name", tag)

        # add item upc to tag members
        database.sadd(utils.tagkey(tag), item.get("upc"))

        # add tag to set of all tags
        database.sadd(alltags, tag)

dispatcher.connect(handle_item_preupdate,
    signal="icecrate.item.preupdate")
