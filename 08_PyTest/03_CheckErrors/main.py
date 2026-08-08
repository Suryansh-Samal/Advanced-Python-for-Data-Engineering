class Weather :

    def weather_check(self, temp):
        if temp < 0 :
            return "Its freezing outside1"

        elif temp < 15 :
            return "Its cold outside!"

        elif temp < 25 :
            return "Its pleasant outside!"

        else :
            return "Its hot outside!"

    def rain_check(self,PoP):
        if PoP > 0.7 :
            return "Its likely to rain outside. Dont forget your umbrella!"

        elif PoP > 0.3 :
            return "Theres a chance of rain outside. You might want to carry a umbrella"

        else :
            return "Its unlikely to rain outside"

    def divide(self, a : float, b : float):
        if b == 0 :
            raise ValueError("Cannot divide by zero")
        return a/b

