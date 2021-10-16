class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("go")

    def stop(self):
        print("stop")

    def turn(self, direction):
        print(f"машина повернула {direction}")


    def show_speed(self):
        print(f"текущая скорость {self.speed}")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("привышение скоростного режима")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("привышение скоростного режима")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar(70, "black", "Town")
sport = SportCar(100,"blue", "Sport")
work = WorkCar(45, "green", "work")
police = PoliceCar(110, "grey", "Police")

town.show_speed()
work.show_speed()


police.turn("направо")


