class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def get_weigth(self, thick, spec_grav):
        return self._length * self._width * thick * spec_grav / 1000


r = Road(5000, 20)
print(r.get_weigth(25, 5))
