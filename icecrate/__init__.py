import os.path

from xdg import BaseDirectory

DATA_HOME = BaseDirectory.save_data_path("icecrate")
# CONFIG_HOME = BaseDirectory.save_config_path("icecrate")

DB_LOCATION = os.path.join(DATA_HOME, "database.dobbin")
