from programs import list_of_squares as squares

def test_squares_1():
    assert squares.list_of_squares(1) == {1: 1}
def test_squares_2():
    assert squares.list_of_squares(2) == {1: 1, 2: 4}