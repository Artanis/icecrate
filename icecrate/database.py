import transaction
from dobbin.database import Database
from dobbin.persistent import checkout, Persistent, PersistentDict

import icecrate

__all__ = ("inventory", )

db = Database(icecrate.DB_LOCATION)

if len(db) < 1:
    # empty/new database
    root = Persistent()

    # 'tables'
    root.inventory = PersistentDict()

    db.elect(root)
    transaction.commit()
    print("Creating new database.")
else:
    print("Using existing database.")

print("Database has {0} records from {1} transactions.".format(
    len(db), db.tx_count))

# expose tables
inventory = db.root.inventory
