def keygen(*path, meta=None):
    """Creates a database key.

    Key schema is ``path:to:item[.metafield]``.

    """
    keypath = ":".join(map(str, path))
    key = ".".join(map(str, filter(None, [keypath, meta])))
    return key
