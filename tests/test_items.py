from unittest.mock import MagicMock, patch

from nose.tools import assert_equal

from icecrate import items

@patch("icecrate.items.dispatcher")
@patch("icecrate.items.database")
def test_save_item_data(database, dispatcher):
    test_item_id = "1234500000001"
    test_data = {
        "name": "Test Save Item Data",
        "upc":  "1234500000001",
        "tags": "unittest, items",
        "quantity": "12"}

    items.save_item_data(test_item_id, test_data)

    database.hmset.assert_called_with("icecrate:items:1234500000001", test_data)
    database.sadd.assert_called_with("icecrate:items.all", test_item_id)

    dispatcher.send.assert_any_call("icecrate.items.preupdate", item=test_data),
    dispatcher.send.assert_any_call("icecrate.items.postupdate", item_id=test_item_id)
