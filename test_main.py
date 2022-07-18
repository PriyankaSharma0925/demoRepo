import pytest

@pytest.mark.regression
def test_firstMethod():
    print("\n Hello World \n")
    print("First pyTest")

@pytest.mark.smoke
def test_secondMethod():
    a=2
    b=4
    c=a+b
    print("\nThe value of c is :")
    print(c)
    assert c==19,"Because C=6 thats why this failed."
#adding commands for github
