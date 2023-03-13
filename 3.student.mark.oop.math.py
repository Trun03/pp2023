import math
print("Input number of students in a class:")
x =  int(input())
class students:  #Class for student's information
 def __init__(self, z, y, n):
    self.name = z
    self.ID = y
    self.DoB = n

 def student(self):
     print("Student",i+1,"name:", self.name)
     print("Student",i+1,"ID:",  self.ID )
     print("Student",i+1,"DOB:", self.DoB) 
liststudent = []
for i in range(x):
    print("Input students",i+1,"ID")
    ID = input()  
    print("Input students",i+1,"name:")
    NAME  = input()
    print("Student",i+1,"DoB")
    DATEOFBIRTH = input()
    Information = students(ID,NAME,DATEOFBIRTH)
    liststudent.append(Information)


print("Input number of courses in a class:")
r =  int(input())  
class courses:   #Class for course's information
  def __init__(course, q, d):
    course.id = q
    course.name = d

  def mycourse(course):
     print("Course",t+1,"ID:", course.id)
     print("Course",t+1,"Name:", course.name)
listcourse = []
CoursesNAME = []
for t in range(r):
    CoursesNAME.append(t)
    print("Input course",t+1,"id:")
    CoursesID = input()
    print("Input course",t+1,"name:")
    CoursesNAME[t] = input()
    CoursesINFO = courses(CoursesID, CoursesNAME[t])
    listcourse.append(CoursesINFO)
print("Select a course name you want to input mark for student:")
e = input()
class mark:  #class for input mark
  def __init__(mark, b):
    mark.number = b

  def studentmark(mark):
    print("student",i+1,"mark:",math.floor(mark.number)) #Using floor()
Marklist = []

while e not in CoursesNAME:
  print("Please select the course again.")
  e = input()

for i in range(x):
       print("Input mark for student",i+1,":")
       marks = float(input())
       Studentmark = mark(marks)
       Marklist.append(Studentmark)
    
print('\n')
print("*******************************")
print("*** 1.Student's Information ***")
print("*******************************")
for i in range(x):
   print(' ')
   liststudent[i].student() 
print('\n')  
print("*******************************")
print(" ** 2.Course's Information  ** ")
print("*******************************")
for t in range(r):
   print(' ')
   listcourse[t].mycourse()
print('\n')  
print("*******************************")
print(" **    3.Student's mark     ** ")
print("*******************************")
print(' ')
print("Student'S mark in course", e,":")
for i in range(x):
  Marklist[i].studentmark()