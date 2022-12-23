import random
class Cat:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True




    def to_sleep(self):
        print("Час спати")
        self.gladness+=3
    def to_play(self):
        print("Час гратись")
        self.progress+=5
        self.gladness+=10
    def to_chill(self):
        print("Час відпочивати")
        self.gladness+=5
        self.progress-0.1
    def is_alive(self):
        if self.progress<=0.5:
            print("Викид на вулицю...")
            self.alive=False
        elif self.gladness<=0:
            print("Скучно....")
            self.alive=False
        elif self.progress>5:
            print("Став дорослим")
            self.alive=False


    def end_of_day(self):
        print(f"Радість = {self.gladness}")
        print(f"Прогрес = {round(self.progress,2)}")
    def live(self,day):
        day ="Day" +str(day + "of" + self.name + "lafe")
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill
nick=Cat(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
