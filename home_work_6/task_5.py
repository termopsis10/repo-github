class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("начни рисовать")

class Pen(Stationery):
    def draw(self):
        print(f"начни рисовать ручкой {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"начни рисовать карандашом {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"начни рисовать маркером {self.title}")

pen = Pen("A")
pencil = Pencil("B")
handle = Handle("C")
for i in (pen, pensil, handle):
    i.draw()
    