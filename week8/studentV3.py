#=========SINEXIA APO TO STUDENT V2=======

class Student:
    def __init__(self, name , house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Athens", "Skogås", "Stockholm"]:
            raise ValueError("Missing House")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        #return "a student"
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return ":O"
            case "Otter":
                return ";D"
            case "What is this":
                return "xD"
            case "_":
                return "/"

def main():
    student = get_student()
    #print(f"{student.name} from {student.house}")
    print("Expecto Patronum!")
    print(student.charm())



def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()


#==============SINEXIA STO V4=========