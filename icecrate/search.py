from pydispatch import dispatcher
import whoosh.index
import whoosh.fields
import whoosh.qparser

import icecrate.items
import icecrate.tags
from icecrate import INDEXDIR

schema = whoosh.fields.Schema(
    upc=whoosh.fields.ID(unique=True, stored=True),
    name=whoosh.fields.TEXT(stored=True),
    tags=whoosh.fields.KEYWORD(stored=True))

def _reindex(): # pragma: no cover
    """Indexes all items in the database.

    Calls ``icecrate.search.handle_postupdate()`` with all item_ids to
    update the entire index.

    Intended for the case where the database exists, but the index is
    missing. Potentially expensive.

    Use sparingly, if at all.

    """
    item_ids = icecrate.items.all_items()

    for item_id in item_ids:
        handle_postupdate(item_id)

def query(query_string): # pragma: no cover
    """Searches the index and yields matching item_ids.

    """
    with index.searcher() as searcher:
        q = parser.parse(query_string)
        results = searcher.search(q)

        for hit in results:
            yield hit.fields()

def handle_postupdate(item_id): # pragma: no cover
    """Insert item data into indexer.

    """
    item = icecrate.items.by_item_id(item_id)

    writer = index.writer()
    writer.update_document(
        upc=item_id,
        name=item.get("name"),
        tags=list(icecrate.tags._split_tags(item.get("tags", ""))))
    writer.commit()

dispatcher.connect(handle_postupdate, signal="icecrate.items.postupdate")

# make the index
try: # pragma no cover
    index = whoosh.index.open_dir(INDEXDIR)
    print("Opened existing index.")
except whoosh.index.EmptyIndexError: # pragma no cover
    print("Creating new index.")
    index = whoosh.index.create_in(INDEXDIR, schema)
    print("Populate index from database.")
    _reindex()

parser = whoosh.qparser.MultifieldParser(["upc", "name", "tags"], index.schema)

def main(): # pragma: no cover
    from pprint import pprint
    _reindex()

    import sys
    pprint(list(query(sys.argv[1])))

if __name__ == '__main__':
    main()
