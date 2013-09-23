from setuptools import setup, find_packages

__VERSION__ = "0.1.1-dev"

setup(
    # package information
    name="icecrate",
    version=__VERSION__,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        # primary requires
        "dobbin", "pyxdg", "bottle>=0.12-dev",
        
        # dobbin requires
        "transaction", "zope.interface"],

    dependency_links=[
        # get bottle 0.12 from github
        "https://github.com/defnull/bottle/tarball/master#egg=bottle-0.12-dev"],

    # metadata
    author="Erik Youngren",
    author_email="artanis.00@gmail.com",
    license="BSD 2-clause",
    url="https://github.com/Artanis/icecrate"

    )
