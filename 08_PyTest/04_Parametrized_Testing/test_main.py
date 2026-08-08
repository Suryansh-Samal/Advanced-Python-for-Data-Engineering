from main import weather_check
import pytest

@pytest.mark.parametrize("temp, expected" , [
       (-5, 'Its freezing outside!'),
       (10, 'Its cold outside'),
       (20, 'Its pleasant outside!'),
       (30, 'Its hot outside')
])

#Test cases for weather_check function:
def test_weather_check(temp , expected):
    assert weather_check(temp) == expected

if __name__ == '__main__':
    test_weather_check()