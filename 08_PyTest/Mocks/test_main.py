from main import api_calls
import pytest

def test_api_calls(mocker):

    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.json.return_value = {'main': {'key': "value"}}

    result = api_calls("https://api.openweathermap.org/data/2.5/weather")
    assert result == {"data": {'main': {'key': "value"}}}