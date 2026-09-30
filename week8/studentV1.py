def main():
    #name = get_name()
    #house = get_house()
    #name, house = get_student()
    student = get_student()
    #if student[0] == "arben":
        #student[1] = "Athens" 
    #print(f"{student[0]} from {student[1]}")
    if student["name"] == "Arben":
        student["house"] = "Skogås"
    print(f"{student['name']} from {student['house']}")

# 2 def gia na paro input name,house step 2
#def get_name():
    #return input("Name: ")
    #return name

#def get_house():
    #return input("House: ")
    #return house

#step 3 kanoume tuple gia na paroume input alla den boroume na alaksoume to inpout
#step 4 to lazoume se list gia na boroume na alaksoume/diorthosoume to input
# step 5 (dictionary / leksiko / array) gia na paroume san groume me key
def get_student():
    #name = input("Name: ")
    #house = input("House: ")
    #return (name, house)
    #return [name, house]
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House ")
    #return {"name": name, "house": house}
    return student

if __name__ == "__main__":
    main()

#======= SINEXIA STO STUDENTv2=======