class person: # the parent class
    #assigning attributes
    def __init__(self, name,age,CID):
        self.name= name
        self.age= age
        self.CID= CID

    # definig behaviours/ method  
    def walk(self):
        print(self.name, "is walking")

    def talk(self):
        print(self.name,"is talking")

    def sleep(self):
        print(self.name,"is sleeping")

    def eat(self):
        print(self.name,"is eating")

class Teacher(person):
    def __init__(self,name,age,CID,subject, salary, department, designation):
        super().__init__(name, age, CID)
        self.subject= subject
        self.salary= salary
        self.department= department
        self.designation= designation

    def teach(self):
        print(self.name,"is teaching")

    def grade_students(self):
        print(self.name,"is grading")

    def attend_meeting(self):
        print(self.name,"is attending meeting")




class Student(person):
    def __init__(self,name,age,CID,std_id, course, year, gpa):
        super().__init__(name, age, CID) 
        self.std_id= std_id
        self.course= course
        self.year= year
        self.gpa= gpa

    def study(self):
        print(self.name,"is studying")

    def attend_class(self):
        print(self.name,"is gattending class")

    def write_exam(self):
        print(self.name,"is writing exam")

    
t1= Teacher("tashi", 30, 12345, "accounts", 30000, "commerce","assistant teacher")
t2= Teacher("dorji", 31, 123456, "physics", 30000, "science","full teacher")

s1= Student("penjor", 18, 1111, 12345,"bbi",1,3)
s2= Student("karma", 19, 1112, 12346,"bbi",1,3.2)

if s1.gpa> s2.gpa:
    print(s1.name,"is better than", s2.name)
    student_information= "year:"+ s1.year +"course:" +s1.course
    print(student_information)

else:
    print(s2.name,"is better than", s1.name)
    student_information= "year:"+ str(s2.year) +"course:" +s2.course
    print(student_information)

Student_storage =[s1,s2]
for std in Student_storage:
    print(std.name)
    print(std.gpa)
    print(std.course)
    print("=======")