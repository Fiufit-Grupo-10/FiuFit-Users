import pytest

from app.api.users import services


def test_haversine():
    location1 = services.Location(
        services.Latitude(-36.623237918303765), services.Longitude(-64.29505665365905)
    )
    location2 = services.Location(
        services.Latitude(-34.56434345739304), services.Longitude(-58.45399635927818)
    )
    assert 575.5 == pytest.approx(location1.distance(location2), 0.1)
