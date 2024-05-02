import pytest

from lib.album_parameters_validator import AlbumParametersValidator

def test_is_valid():
    validator = AlbumParametersValidator("My Title", "1990")
    assert validator.is_valid() == True

def test_is_not_valid_with_bad_title():
    validator_1 = AlbumParametersValidator("", "1990")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator("My Title", None)
    assert validator_2.is_valid() == False
    validator_3 = AlbumParametersValidator("My Title", "fred")
    assert validator_3.is_valid() == False


def test_generate_errors():
    validator_1 = AlbumParametersValidator("", "")
    assert validator_1.generate_errors() == [
        "Title must not be blank",
        "Release year must be a number"
    ]

    validator_2 = AlbumParametersValidator("Title", "")
    assert validator_2.generate_errors() == [
        "Release year must be a number"
    ]

    validator_3 = AlbumParametersValidator("", "1990")
    assert validator_3.generate_errors() == [
        "Title must not be blank"
    ]

def test_get_valid_title_if_title_valid():
    validator_1 = AlbumParametersValidator("Title", "")
    assert validator_1.get_valid_title() == "Title"

def test_get_valid_title_refuses_if_invalid():
    validator_1 = AlbumParametersValidator("", "")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_title()
    assert str(err.value) == "Cannot get valid title"


def test_get_valid_release_year_if_release_year_valid():
    validator_1 = AlbumParametersValidator("Title", "1990")
    assert validator_1.get_valid_release_year() == "1990"

def test_get_valid_release_year_refuses_if_invalid():
    validator_1 = AlbumParametersValidator("Title","")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_release_year()
    assert str(err.value) == "Cannot get valid release year"