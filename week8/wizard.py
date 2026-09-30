class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        
    ...

class Student(Wizard):
    def __init__(self, name, house):
        #if not name:
         #   raise ValueError("Missing name")
        #self.name = name
        super().__init__(name)
        self.house = house

    ...

    

class Professor(Wizard):
    def __init__(self, name, subject):
       # if not name:
        #    raise ValueError("Missing name")       
        #self.name = name
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Stefan")
student = Student("Arben", "Athens")
professor = Professor("Rafael" "Stockholm")