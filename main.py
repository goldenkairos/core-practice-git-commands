import pytest


def always_returns_true():
    return True
#change the return False to True
#adding additional change
def test_always_returns_true():
    assert always_returns_true()
