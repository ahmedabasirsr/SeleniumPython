
class Student:
##############################################################
#number objects of students=> start 0 this is atrbiut of class
##############################################################
    number_of_sutdents = 0
#############################################################
# initial method of class Student, it has 3 paremeters
#############################################################
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses # list courses
        Student.number_of_sutdents +=1  # sum of stuents number

stud1 = Student("Ahmed",32,["cs","html","python"])
stud2 = Student("Ali",35,["jscribt","os","math"])
print(stud1.name,stud1.age,stud1.courses)
print(stud2.name,stud2.age,stud2.courses)
print (Student.number_of_sutdents, " ====>access from class Student")
print (stud1.number_of_sutdents, " ====>access from any object class")
#change of value of object stud1, this is not cabsolation
stud1.name = "Husain"
print(stud1.name,stud1.age,stud1.courses)


        
