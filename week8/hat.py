import random

class Hat:
    #def __init__(self):
       # self.houses = ["Athens", "Stockholm", "Ath"]
    houses = ["Athens", "Stockholm", "Ath"] 

    #def sort(self, name):
    @classmethod
    def sort(cls, name):
        print(name, "is in",random.choice(cls.houses))

#hat = Hat()
Hat.sort("Arben")
