def split_version(vs):
    import re
    for v in re.findall(r"[\w\d]+", vs):
        try:
            v = int(v)
        except ValueError:
            pass
        yield v

__version__ = "0.1.3-dev"
__version_info__ = tuple(split_version(__version__))
