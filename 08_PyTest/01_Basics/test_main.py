from main import weather_check

#Test cases for weather_check function:
def test_weather_check():
    assert weather_check(-5) == ' Its freezing outside!'
    assert weather_check(10) == 'Its cold outside'
    assert weather_check(20) == 'Its pleasant outside!'
    assert weather_check(30) == 'Its hot outside'

test_weather_check()