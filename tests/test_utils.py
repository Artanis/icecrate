from nose.tools import assert_equal

from icecrate import utils

def test_keygen_root():
    expected = "root"
    result = utils.keygen("root")
    assert_equal(result, expected)

def test_keygen_root_meta():
    expected = "root.meta"
    result = utils.keygen("root", meta="meta")
    assert_equal(result, expected)

def test_keygen_path():
    expected = "root:path:to:value"
    result = utils.keygen("root", "path", "to", "value")
    assert_equal(result, expected)

def test_keygen_path_meta():
    expected = "root:path:to:value.meta"
    result = utils.keygen("root", "path", "to", "value", meta="meta")
    assert_equal(result, expected)
