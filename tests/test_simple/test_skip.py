import pytest


@pytest.mark.skip
def test_skip():
    assert False


@pytest.mark.skip
def test_skip2():
    assert False
