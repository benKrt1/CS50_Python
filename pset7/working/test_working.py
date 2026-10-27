import pytest

from working import convert


def test_convert_full_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:30 AM to 12:45 PM") == "00:30 to 12:45"


def test_convert_times_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_convert_mixed_minute_formats():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


@pytest.mark.parametrize(
    "hours",
    [
        "9:60 AM to 5 PM",
        "13 AM to 5 PM",
        "9 AM - 5 PM",
        "9:0 AM to 5 PM",
        "9 am to 5 PM",
    ],
)
def test_convert_rejects_invalid_input(hours):
    with pytest.raises(ValueError):
        convert(hours)  