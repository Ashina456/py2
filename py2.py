import random

class Human:
    def __init__(self, name="no", years=0, home="no", car="no", job="no"):
        self.name = name
        self.years = years
        self.home = home
        self.car = car
        self.gladness = 50
        self.satiety = 50
        self.money = 100
        self.job = job

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            else:
                self.satiety += 5
                self.home.food -= 3

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 5

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Ви купили паливо")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Ви купили їжу")
            self.money -= 20
            self.home.food += 15
        elif manage == "delicacious":
            print("Ви купили паливо")
            self.gladness += 10
            self.satiety += 2
            self.money -= 50

    def chill(self):
        self.gladness += 10
        self.home.mess = 0
        self.money -= 10

    def clean_home(self):
        self.gladness -= 10
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def bathroom(self):
        self.gladness += 10

    def days_indexes(self, day):
        day = f"сьогодні {day} день життя {self.name}"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:=^50}", "\n")
        print(f"гроші {self.money}", "\n")
        print(f"ситість {self.satiety}", "\n")
        print(f"щастя {self.gladness}", "\n")
        home_indexes = "home indexes"
        print(f"{home_indexes:=^50}", "\n")
        print(f"їжа {self.home.food}", "\n")
        print(f"чистота {self.home.mess}", "\n")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:=^50}", "\n")
        print(f"паливо {self.car.fuel}", "\n")
        print(f"сила {self.car.strength}", "\n")

    def is_alive(self):
        if self.gladness < 0:
            print(":(")
        if self.satiety < 0:
            print("R.I.P")
        if self.money <=300:
            print("банкрот")
            return


    def birthday(self):

        pass

    def live(self, day):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.strength = brand_list[self.brand]["strength"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("заправся твар")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
    "Java developer": {"salary":50, "gladness_less":10},
    "food delivery": {"salary":30, "gladness_less":8},
    "C++": {"salary":60, "gladness_less":15},
    "cashier": {"salary":30, "gladness_less":10},
}

brands_of_car = {
    "BMW":{"fuel":100,"strength":100,"consumption":8},
    "Ferrari":{"fuel":90,"strength":120,"consumption":12},
    "Jaguar":{"fuel":110,"strength":90,"consumption":10},
}
class Job:
    def __init__(self):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]