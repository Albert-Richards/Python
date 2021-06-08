from programs import factorial

def test_factorial_0():
    assert factorial.fact(0) == 1
def test_factorial_1():
    assert factorial.fact(1) == 1
def test_factorial_4():
    assert factorial.fact(4) == 24