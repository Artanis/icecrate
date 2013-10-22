from setuptools import setup, find_packages

def get_version():
    version_file = "icecrate/_version.py"
    loc = {}
    with open(version_file, "r") as f_version:
        code = compile(f_version.read(), "_version.py", "exec")
        exec(code, {}, loc)

    return loc.get("__version__")

setup(
    # package information
    name="icecrate",
    version=get_version(),

    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "bottle>=0.12-dev",
        "redis",
        "PyDispatcher",
        "Whoosh",
        "pyxdg"],

    dependency_links=[
        # get bottle 0.12 from github
        "https://github.com/defnull/bottle/tarball/master#egg=bottle-0.12-dev"],

    # metadata
    author="Erik Youngren",
    author_email="artanis.00@gmail.com",
    license="BSD 2-clause",
    url="https://github.com/Artanis/icecrate"
    ) 
