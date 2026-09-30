students = ["Hermione", "Harry", "Ron"]

#gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
#gryffindors = {student: "Gryffindor" for student in students}
#print(gryffindors)

#for student in students:
    #print(student)

for i, student in enumerate(students):
    print(i +1, student)