class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickels = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickels} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickels = self.sickels + other.sickels
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickels, knuts )      

potter = Vault(100, 50, 25)
print(potter)

arben = Vault(25, 50, 100)
print(arben)

#galleons = potter.galleons + arben.galleons
#sickels = potter.sickels + arben.sickels
#knuts = potter.knuts + arben.knuts

#total = Vault(galleons, sickels, knuts)
total = potter + arben
print(total)