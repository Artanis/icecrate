import bottle

app = bottle.Bottle()

@app.route("/")
@bottle.view("search_results")
def search():
    query = bottle.request.query.get("q", "")
    return {"q": query}
