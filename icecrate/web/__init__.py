import os.path

import bottle

from icecrate.web import items, search, tags

SERVER_ROOT = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(SERVER_ROOT, "static")
VIEW_ROOT = os.path.join(SERVER_ROOT, "views")
FRAGMENT_ROOT = os.path.join(SERVER_ROOT, "fragments")

bottle.TEMPLATE_PATH.insert(0, FRAGMENT_ROOT)
bottle.TEMPLATE_PATH.insert(0, VIEW_ROOT)

app = bottle.Bottle()

@app.route("/")
@bottle.view("icecrate_home.tpl")
def index():
    return {}

@app.route("/help")
@bottle.view("icecrate_help.tpl")
def help():
    return {"upc": bottle.request.query.get("upc", None)}

@app.route("/about")
@bottle.view("icecrate_about.tpl")
def about():
    return {}

@app.route("/static/<filename:path>")
def static_files(filename):
    return bottle.static_file(filename, STATIC_ROOT)

app.mount("/items", items.app)
app.mount("/search", search.app)
app.mount("/tags", tags.app)

if __name__ == '__main__':
    usage = """Please use the bottle.py command to run Icecrate.

For example:
    $ bottle.py -b 0.0.0.0:8080 icecrate.web:app

    """
    print(usage)
