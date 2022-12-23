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
            print("Відрахування...")
            self.alive=False
        elif self.gladness<=0:
            print("Скучно....")
            self.alive=False
        