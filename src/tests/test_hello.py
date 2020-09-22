# coding=utf-8

"""Test say hello."""


from app.hello import say_hello


def test_say_hello_print():
    """Test say hello function."""
    name = "Urapython"
    assert say_hello(name) == "Hello, Urapython!"
