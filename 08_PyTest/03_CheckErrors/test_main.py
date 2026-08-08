from main import Weather
import pytest
def test_weather_check():
    W = Weather()
    assert W.weather_check(-5) == "Its freezing outside1"
    assert W.weather_check(10) == "Its cold outside!"
    assert W.weather_check(20) == "Its pleasant outside!"
    assert W.weather_check(30) == "Its hot outside!"

def test_rain_check():
    rc = Weather()
    assert rc.rain_check(0) == "Its unlikely to rain outside"
    assert rc.rain_check(0.5) == "Theres a chance of rain outside. You might want to carry a umbrella"
    assert rc.rain_check(1) == "Its likely to rain outside. Dont forget your umbrella!"

def test_divide():
    d = Weather()
    assert d.divide(10,5) == 2
    assert d.divide(9,3) == 3

    with pytest.raises(ValueError, match="Cannot divide by zero"):
            d.divide(10,0)


test_weather_check()
test_rain_check()

#To run the test you need to write pytest + relative path in the terminal then hit enter 
