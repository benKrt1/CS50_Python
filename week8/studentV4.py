#=========SINEXIA APO TO STUDENT V3=======

class Student:
    def __init__(self, name , house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):                                                               
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Athens", "Stockholm", "Skogås"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    #student = get_student()
    student = Student.get()
    print(student)
    



#def get_student():
    #name = input("Name: ")
    #house = input("House: ")
   # return Student(name, house)

if __name__ == "__main__":
    main()


