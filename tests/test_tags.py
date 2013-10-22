from operator import itemgetter
from unittest.mock import MagicMock, patch

from nose.tools import assert_equal

from icecrate import tags

def test_split_tags():
    assert_equal(
        tags._split_tags("a, b, c, d, e"),
        {"a", "b", "c", "d", "e"})

def test_split_tags_with_spaces():
    assert_equal(
        tags._split_tags("a b   ,  c d, e   f    "),
        {"a b", "c d", "e   f"})

def test_split_tags_with_commas():
    assert_equal(
        tags._split_tags("a,,,b    ,, c,, d,, e,,,f,,"),
        {"a", "b", "c", "d", "e", "f"})

def test_split_tags_with_duplicates():
    assert_equal(
        tags._split_tags("a, a, b,,c, c, d"),
        {"a", "b", "c", "d"})

@patch("icecrate.items.by_item_id")
@patch("icecrate.tags.by_tag_id")
def test_by_item_id(by_tag_id, by_item_id):
    by_tag_id.side_effect = lambda a: {"name": a}
    by_item_id.return_value = {
        "name": "Test Tags By Item ID",
        "upc":  "1234500000011",
        "tags": "unittest, tags",
        "quantity": "30"}
    expected = sorted([{"name": "unittest"}, {"name": "tags"}], key=itemgetter("name"))


    result = sorted(tags.by_item_id("1234500000011"), key=itemgetter("name"))

    assert_equal(result, expected)

@patch("icecrate.items.by_item_id")
@patch("icecrate.tags.by_tag_id")
def test_by_missing_item_id(by_tag_id, by_item_id):
    by_tag_id.side_effect = lambda a: {"name": a}
    by_item_id.return_value = {}
    expected = []

    retult = list(tags.by_item_id("definitely missing"))

    assert_equal(retult, expected)

@patch("icecrate.tags.database")
def test_item_preupdate(database):
    test_data = {
        "name": "Test Item Preupdate",
        "upc": "1234500000012",
        "tags": "unittest, tags",
        "quantity": "44"}

    tags.handle_item_preupdate(test_data)

    database.sadd.assert_any_call("icecrate:tags.all", "unittest"),
    database.sadd.assert_any_call("icecrate:tags.all", "tags")
    
    database.hset.assert_any_call("icecrate:tags:unittest", "name", "unittest")
    database.hset.assert_any_call("icecrate:tags:tags", "name", "tags")
