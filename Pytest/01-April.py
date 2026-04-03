import pytest

@pytest.mark.regression
def test_fname():
    actual = True
    expected = True
    assert actual == expected, "Wrong"


@pytest.mark.regression
def test_fname1():
    actual = True
    expected = True
    assert actual == expected, "Wrong"


def test_fname2():
    print("false")

