from seasons import convert
from seasons import convert_to_minutes
import pytest


def test_convert():
    
    assert convert("1970-02-19") == 20519
    assert convert("1999-12-31") == 9612
    assert convert("2000-02-29") == 9552


def test_convert_invalid():
    
    try:
        convert("1970-02-30")
    except SystemExit:
        pass
    else:
        raise AssertionError("Expected SystemExit")


def test_convert_invalid_format():
    
    try:
        convert("1970/02/19")
    except SystemExit:
        pass
    else:
        raise AssertionError("Expected SystemExit")
    try:
        convert("january 1, 2000")
    except SystemExit:
        print("Invalid format!")

    else:
        raise AssertionError("Expected SystemExit")

def test_convert_non_numeric():
    
    try:
        convert("1970-02-xx")
    except SystemExit:
        pass
    else:
        raise AssertionError("Expected SystemExit")


def test_convert_to_minutes():
    assert (
        convert_to_minutes(20519)
        == "Twenty-nine million, five hundred forty-seven thousand, three hundred sixty minutes"
    )
    assert (
        convert_to_minutes(9612)
        == "Thirteen million, eight hundred forty-one thousand, two hundred eighty minutes"
    )
    assert (
        convert_to_minutes(9552)
        == "Thirteen million, seven hundred fifty-four thousand, eight hundred eighty minutes"
    )
