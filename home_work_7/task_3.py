class Cell:
    def __init__(self, parts):
        self.psrts = parts

    def __add__(self, other):
        return Cell(self.psrts + other.parts)

    def __sub__(self,other):
        diff = self.parts - other.parts
        if diff >= 0:
            return Cell(diff)

        else:
            print(f"ошибка вычитания!")

    def __mul__(self, other):
        return Cell(self.parts * other.patrs)

    def __truediv__(self,other):
        return Cell(self.parts // other.parts)
    def __str__(self):
        return f'{self.parts}'

    cell = Cell(26)
    cell2 = Cell (18)
    print(cell - cell2)
    print(cell + cell2)
    print(cell * cell2)
    print(cell / cell2)
    print(cell2 - cell)

