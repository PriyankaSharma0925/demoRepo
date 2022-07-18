import pytest

@pytest.mark.regression
def test_case1():
    print("\nthird test file")

@pytest.mark.skip
def test_case2():
    print("In the third file")
@pytest.mark.smoke
def test_case3():
    str="Today is monday."
    assert str== "Sunday","Both the strings donot match."


