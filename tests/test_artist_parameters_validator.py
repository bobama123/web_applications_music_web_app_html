import pytest

from lib.artist_parameters_validator import ArtistParametersValidator

def test_is_valid():
    validator = ArtistParametersValidator("Roger", "pop")
    assert validator.is_valid() == True

def test_is_not_valid_with_bad_name():
    validator_1 = ArtistParametersValidator("", "pop")
    assert validator_1.is_valid() == False
    validator_2 = ArtistParametersValidator("Roger", None)
    assert validator_2.is_valid() == False


def test_generate_errors():
    validator_1 = ArtistParametersValidator("", "")
    assert validator_1.generate_errors() == [
        "Name must not be blank",
        "Genre must not be blank"
    ]

    validator_2 = ArtistParametersValidator("Roger", "")
    assert validator_2.generate_errors() == [
        "Genre must not be blank"
    ]

    validator_3 = ArtistParametersValidator("", "1990")
    assert validator_3.generate_errors() == [
        "Name must not be blank"
    ]

def test_get_valid_name_if_name_valid():
    validator_1 = ArtistParametersValidator("Roger", "")
    assert validator_1.get_valid_name() == "Roger"

def test_get_valid_name_refuses_if_invalid():
    validator_1 = ArtistParametersValidator("", "")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_name()
    assert str(err.value) == "Cannot get valid name"


def test_get_valid_genre_if_genre_valid():
    validator_1 = ArtistParametersValidator("Roger", "pop")
    assert validator_1.get_valid_genre() == "pop"

def test_get_valid_genre_refuses_if_invalid():
    validator_1 = ArtistParametersValidator("Roger","")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_genre()
    assert str(err.value) == "Cannot get valid genre"