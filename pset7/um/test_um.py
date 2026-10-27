from um import count


def test_count_single_um():
    assert count("hello, um, world") == 1


def test_count_case_insensitively():
    assert count("Um, UM, and um") == 3


def test_count_multiple_words():
    assert count("um... I mean, um!") == 2


def test_count_rejects_substrings():
    assert count("yummy, umbrella, hum") == 0