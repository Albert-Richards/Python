from programs import vowels

def test_vowels_nonsense():
    assert vowels.vowels("AgdUieoCFDOIfxauE") == 10
