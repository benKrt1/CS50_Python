import pytest

from jar import Jar


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


@pytest.mark.parametrize("capacity", [-1, "12", 2.5])
def test_init_rejects_invalid_capacity(capacity):
    with pytest.raises(ValueError):
        Jar(capacity)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(3)
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)


def test_deposit_and_withdraw_reject_negative_numbers():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.withdraw(-1)