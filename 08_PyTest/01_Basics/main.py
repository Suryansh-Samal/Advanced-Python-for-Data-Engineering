def weather_check(temp):
    if temp < 0 :
        return ' Its freezing outside!'

    elif temp < 15 :
        return 'Its cold outside'

    elif temp < 25 :
        return 'Its pleasant outside!'

    else :
        return 'Its hot outside'

print(weather_check(20))