########
Icecrate
########

Icecrate is a simple inventory system written in Python 3. The intention is to create an inventory hosted on the local network, accessible primarily by smartphones on that network.

As new items are added to the physical collection, they can be scanned with the barcode app on a smartphone, allowing the information stored on the server to be updated. Currently, this would be the quantity of the item.

==========
Installing
==========

Install Icecrate from the latest sources::
    
    pip install https://github.com/Artanis/icecrate/tarball/master

As Icecrate is still in development, stable sources are not currently available.

To launch Icecrate::
    
    BIND_TO="0.0.0.0:8080"
    bottle.py -b $BIND_TO icecrate.web:app
