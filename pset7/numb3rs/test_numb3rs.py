from numb3rs import validate

def test_format():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_range():
    assert validate("255.255.255.256") == False
    assert validate("512.1.1.1") == False
    assert validate("1.2.3.444") == False

def test_string():
    assert validate("cat.dog.bird.fish") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False