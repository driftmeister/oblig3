import pytest as pt
from oblig3 import leapYear

#69
@pt.fixture()
def leap_year():
    return leapYear


def test_isYearDividableBy4(leap_year):
    year = leap_year(2024)
    assert year.isLeapYear() == True

    year = leap_year(2023)
    assert year.isLeapYear() == False

    year = leap_year(2000)
    assert year.isLeapYear() == True

def test_isDividableBy4ButNot100(leap_year):
    year = leap_year(2024)
    assert year.isLeapYear() == True

    year = leap_year(1996)
    assert year.isLeapYear() == True

def test_isDividableBy400(leap_year):
    year = leap_year(2000)
    assert year.isLeapYear() == True

    year = leap_year(2400)
    assert year.isLeapYear() == True

    year = leap_year(2300)
    assert year.isLeapYear() == False

