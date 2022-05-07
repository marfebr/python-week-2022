from beerlog.core import get_beers, add_beer_database


def test_add_beer_to_database():
    assert add_beer_database("Blue Moon", "Witbier", 10, 3, 6)


def test_get_beers():
    # Arrange
    add_beer_database("Blue Moon", "Witbier", 10, 3, 6)
    # Actict
    results = get_beers()
    # Assert
    assert len(results) > 0
