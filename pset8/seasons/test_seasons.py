from datetime import date

import pytest

from seasons import age_in_minutes, minutes_to_words, parse_date


def test_parse_date():
    assert parse_date("1999-01-01") == date(1999, 1, 1)


@pytest.mark.parametrize("value", ["1999/01/01", "1999-1-01", "January 1, 1999"])
def test_parse_date_rejects_invalid_format(value):
    with pytest.raises(ValueError):
        parse_date(value)


def test_age_in_minutes():
    assert age_in_minutes(date(2024, 1, 1), date(2024, 1, 2)) == 1_440
    assert age_in_minutes(date(2023, 1, 1), date(2024, 1, 1)) == 525_600


def test_minutes_to_words():
    assert minutes_to_words(1_440) == "One thousand, four hundred forty"
    assert minutes_to_words(525_600) == "Five hundred twenty-five thousand, six hundred"