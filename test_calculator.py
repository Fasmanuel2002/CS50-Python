import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
    
def zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):# its going to call this whenever you write a code that has a TypeError
        square("cat")