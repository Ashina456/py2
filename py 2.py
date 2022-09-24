import random


class Human:
    def __init__(self, name="Human", money = 100, gladness = 50, job=None, home=None, car=None, self_mood = random.randint(0,100),man = None, wife = None, state = False, country = None):
        self.name = name
        self.money = money
        self.gladness = gladness
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.good = 0
        self.self_mood = self_mood
        self.wife = wife
        self.man = man
        self.state = state
        self.country = country
        self.days = 1
        self.dice = 0

    def get_home(self):
        if self.state == False:
            self.home = House()
        if self.state == True:
            self.home = self.man.home

    def get_car(self):
        if self.state == False:
            self.car = Auto(brands_of_car)
        if self.state == True:
            self.car = self.man.car

    def get_wife(self):
        if(self.state == False):
            self.good = 0
            if self.self_mood <= random.randint(0,100):
                self.wife = Human(name="Alina",state=True, man=self, money=5000)
                print(f"{self.name} has a girl!!!")
            else:
                print(f"{self.name} was not liken by girl")

    def get_job(self):
        if self.car == None:
            self.get_car()
            return
        if self.car.drive():
            self.car.strength -= 10
        else:
            self.repair()
            return
        self.job = Job(list_of_jobs)

    def get_country(self):
        if self.state == False:
            self.country = Country(names_of_countries)
        if self.state == True:
            self.country = self.man.country

    def repair(self):
        self.car.strength += 100
        self.money -= (self.country.payment / 50) / (self.country.payment / 10000)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 3

    def shopping(self, manage):
        if self.car.drive():
            self.car.strength -= 10
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.repair()
                return
        if manage == "fuel":
            print("Fuel bought")
            self.money -= (self.country.payment / 100) / (self.country.payment / 10000)
            self.car.fuel += self.country.fuelnes / 1000
        elif manage == "food":
            print("Food bought")
            self.money -= (self.country.payment / 25) / (self.country.payment / 10000)
            self.home.food += self.country.foodnes / 1000
        elif manage == "dedicates":
            print("YooHoo!! DELICIOUS!!!")
            self.gladness += 10 + self.country.gladnesser / 10
            self.satiety += 2
            self.money -= (self.country.payment / 75) / (self.country.payment / 10000)

    def work(self):
        if self.car.drive():
            self.car.strength -= 10
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.repair()
                return
        self.money += (self.country.payment * self.job.salary) / 35000
        self.gladness -= self.job.gladness_less + self.country.gladnesser / 10
        self.satiety -= 5

    def chill(self):
        self.dice = random.randint(1, 3)
        if self.dice == 1:
            self.gladness += 10 + self.country.gladnesser / 10
            self.home.mess += 5
            self.money -= (self.country.payment / 10) / (self.country.payment / 10000)
        elif self.dice == 2:
            print("Time for shopping!!!")
            self.shopping("dedicates")

    def clean(self):
        self.gladness -= 5 + self.country.gladnesser / 10
        self.home.mess = 0

    def bathroom(self):
        self.gladness += 10 + self.country.gladnesser / 10

    def index_days(self):
        day_text = f"Today the {self.days} of {self.name}'s life"
        print(f"{day_text:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:=^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        if self.wife != None:
            wife_indexes = self.wife.name + "'s indexes"
            print(f"Wife {wife_indexes:=^50}", "\n")
            print(f"Wife Money - {self.wife.money}")
            print(f"Wife Satiety - {self.wife.satiety}")
            print(f"Wife Gladness - {self.wife.gladness}")
            self.wife.days += 1
        home_indexes = "Home indexes"
        print(f"{home_indexes:=^50}", "\n")
        print(f"Food = {self.home.food}")
        print(f"Mess = {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:=^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")
        self.days += 1


    def is_alive(self):
        if self.gladness < self.country.gladnesser / 10:
            print("Dead inside")
            return False
        if self.satiety < 0:
            print(" R.I.P")
            return False
        if self.money <= self.country.payment / 10000:
            print("Bankrot")
            return False

    def live(self):
        if self.state == False:

            if self.home is None:
                print("Settled down in the house")
                self.get_home()
            if self.country is None:
                print("Gotten a country")
                self.get_country()
            if self.car is None:
                self.get_car()
                print(f"I bought a car! {self.car.brand}")
            if self.job is None:
                self.get_job()
                print(f"I don't have a job. I must get a job! {self.job.job} With salary: {self.job.salary}")
            if self.wife is None:
                print(f"I don't have a wife. I must get a wife!")
                self.get_wife()
            else:
                self.wife.live()
            self.dice = random.randint(1, 3)
            if self.satiety < 20:
                print("Im gonna eat")
                self.eat()
            elif self.gladness < self.country.gladnesser / 5:
                if self.home.mess > 15:
                    print("I wanna chill, but there is so much mess  So I will clean the house")
                    self.clean()
                else:
                    print("Let's chill!")
                    self.chill()
            elif self.money <= self.country.payment / 5000:
                print("Start working...")
                self.work()
            elif self.home.food <= 0:
                print("I'm very hungry!!!")
                self.shopping("food")
            elif self.car.strength < 100:
                print("I need to repair my car")
                self.repair()
            elif self.dice == 1:
                print("Let's chill!")
                self.chill()
            elif self.dice == 2:
                print("Statrt working...")
                self.work()
            elif self.dice == 3:
                print("Cleaning time!")
                self.clean()
            self.index_days()
            if self.is_alive() == False:
                return False
            else:
                return True
        else:
            if self.home is None:
                print("Girl Settled down in the house")
                self.get_home()
            if self.country is None:
                print("Girl Settled down in the house")
                self.get_country()
            if self.car is None:
                print("Girl Settled down in the house")
                self.get_car()
            self.dice = random.randint(1, 6)
            if self.satiety < 20:
                print("Im gonna eat")
                self.eat()
            elif self.money < 100 + self.country.payment / 10000:
                print("MAAAAAAAAAN i need MONEY!!!!")
                self.dice = random.randint(1, 2)
                if self.dice == 1:
                    print("Okay i will give you money")
                    self.money += self.country.payment / 5000
                    self.man.money -= self.country.payment / 5000
                    self.man.gladness += self.country.gladnesser / 10
                if self.dice == 2:
                    self.man.gladness -= self.country.gladnesser / 10
                    print("Okay i will give you money")
            elif self.gladness < self.country.gladnesser / 3:
                print("Let's chill!")
                self.chill()
            elif self.home.food <= 0:
                print("Man i'm very hungry!!!")
                self.man.shopping("food")
            elif self.car.strength < 100:
                print("You need to repair my car")
                self.man.repair()
            elif self.dice == 1:
                print("Let me chill!")
                self.chill()
            elif self.dice == 2:
                print("Lets Eat")
                self.eat()
            elif self.dice >= 3:
                self.man.gladness += 40 + self.country.gladnesser / 10
                self.clean()
            return True




class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.strength = brand_list[self.brand]["strength"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.consumption -= 1
            return True
        else:
            print("The car can't move")
            return False

class Country:
    def __init__(self, country_list):
        self.name = random.choice(list(country_list))
        self.payment = country_list[self.name]["payment"]
        self.gladnesser = country_list[self.name]["gladnesser"]
        self.foodnes = country_list[self.name]["foodnes"]
        self.fuelnes = country_list[self.name]["fuelnes"]

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

list_of_jobs = {
    "It developer": {"salary": 100, "gladness_less": 15},
    "Car driver": {"salary": 50, "gladness_less": 10},
    "Fireman": {"salary": 100, "gladness_less": 25},
    "Doctor": {"salary": 25, "gladness_less": 5}
}

names_of_countries = {
    "Ukraine": {"payment": 250000, "gladnesser": 70, "foodnes": 500000, "fuelnes": 20000},
    "Sweden": {"payment": 750000, "gladnesser": 100, "foodnes": 200000, "fuelnes": 50000},
    "Italy": {"payment": 500000, "gladnesser": 90, "foodnes": 600000, "fuelnes": 15000},
    "Poland": {"payment": 300000, "gladnesser": 80, "foodnes": 250000, "fuelnes": 25000}
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Mercedes": {"fuel": 100, "strength": 150, "consumption": 8},
    "Tesla": {"fuel": 100, "strength": 175, "consumption": 5},
    "Ferrari": {"fuel": 80, "strength": 200, "consumption": 10}
}

andriy = Human(name="Andriy", money=1000)

while andriy.live():
    pass
