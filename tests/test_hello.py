from dojo.hello import greet


def test_greets_name_when_name_provided():
    assert greet("Jorge") == "Hi, Jorge!"

def test_greets_no_name_when_name_empty():
    assert greet("") == "Hi!"

def test_greets_no_name_when_name_null():
    assert greet(None) == "Hi!"

