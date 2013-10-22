from nose.tools import assert_equal
from unittest.mock import MagicMock, patch
from webtest import TestApp

from icecrate import web

@patch("icecrate.items.all_items")
@patch("icecrate.items.by_item_id")
def test_all_items(by_item_id, all_items):
    all_items.return_value = set(range(10))
    by_item_id.side_effect = (lambda a: {
        "name": "Test Web All Items",
        "upc": a,
        "tags": "unit test, web, items"})

    app = TestApp(web.app)

    reply = app.get("/items")

    assert_equal(reply.status, "200 OK")

@patch("icecrate.items.by_item_id")
def test_one_item(by_item_id):
    by_item_id.return_value = {
        "name": "Test Web Show One Item",
        "upc": "1234500000101",
        "tags": "unit test, web, items",
        "quantity": "23"}

    app = TestApp(web.app)

    reply = app.get("/items/1234500000101")

    assert_equal(reply.status, "200 OK")

@patch("icecrate.items.save_item_data")
def test_update_item(save_item_data):
    test_id = "1234500000101"
    test_data = {
        "name": "Test Web Update Item",
        "tags": "unit test, web, items",
        "quantity": "36"}
    
    app = TestApp(web.app)

    reply = app.post("/items/1234500000101", test_data)

    assert_equal(reply.status, "302 Found")

    save_item_data.assert_called_with(test_id, dict(test_data, upc=test_id))
