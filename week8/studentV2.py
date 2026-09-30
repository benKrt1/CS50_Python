#=========== SINEXIA APO TO studentV2====
#=========== poio katharogrameni ekdosi me tou "class"

#step 1 ftiaxno ena class gia tous 

class Student:
    def __init__(self, name , house):
        #an o xristis den vali kapoio onoma...
        if not name:
            raise ValueError("Missing name")
        if house not in ["Athens", "Skogås", "Stockholm"]:
            raise ValueError("Missing House")
        self.name = name
        self.house = house
    

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")



def get_student():
    #student = Student()
    #student.name = input("Name: ")
    #student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    #student = Student(name, house)
    #return student
    return Student(name, house)

if __name__ == "__main__":
    main()


