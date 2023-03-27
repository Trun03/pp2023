import curses
import math
import numpy as np

class students:  #Class for student's information
 def __init__(self, z, y, n):
    self.name = z.decode('utf-8')
    self.ID = y.decode('utf-8')
    self.DoB = n.decode('utf-8')
 def student(self): 
     return f"Student Full Name: {self.name}\nStudent ID: {self.ID}\nStudent DOB: {self.DoB}"


class courses:   #Class for course's information
  def __init__(course, q, d, credit):
    course.mark = credit 
    course.id = q.decode('utf-8')
    course.name = d.decode('utf-8')

  def mycourse(course):
     return f"Course ID: {course.id}\nCourse Name: {course.name}\nCourse Credit: {course.mark} "

class mark(courses, students):  #class for input mark
  def __init__(mark, b,course, self):
    mark.self = self.name
    mark.course= course.name
    mark.number = b
  def studentmark(mark):
     return f"Student Mark: {math.floor(mark.number)}" #Using math module

def main(UI): #Using UI to decorate
   UI.clear()
   curses.echo()
   UI.addstr("\nInput number of students in a class:")
   x =  int(UI.getstr())
   liststudent = []
   for i in range(x):
      UI.clear()
      UI.addstr(f"Input student {i+1} ID:")
      ID = UI.getstr()
      UI.clear()
      UI.addstr(f"Input student {i+1} name:")
      NAME  = UI.getstr() 
      UI.clear()
      UI.addstr(f"Student {i+1} DoB:")
      DATEOFBIRTH = UI.getstr()
      Information = students(ID,NAME,DATEOFBIRTH)
      liststudent.append(Information)

   UI.clear()
   UI.addstr("Input number of courses in a class:")
   r =  int(UI.getstr())
   listcourse = []
   CoursesNAME = []
   for t in range(r):
      CoursesNAME.append(t)
      UI.clear()
      UI.addstr(f"Input course {t+1} id:")
      CoursesID = UI.getstr()
      UI.clear()
      UI.addstr(f"Input course {t+1} name:")
      CoursesNAME[t] = UI.getstr()
      UI.clear()
      UI.addstr(f"Input course's credit {t+1} :")
      c = float(UI.getstr())
      credit = np.array(c) 
      CoursesINFO = courses(CoursesID, CoursesNAME[t],credit)
      listcourse.append(CoursesINFO)

   Marklis = []
   UI.clear()
   for t in range(r):
      UI.addstr(f"Student's mark in course {t+1}")
      for i in range(x):
         UI.clear()
         UI.addstr(f"Input mark for student {i+1} :")
         m = float(UI.getstr()) 
         Studentmark = mark(m,listcourse[t], liststudent[i])
         Marklis.append(Studentmark)
   UI.clear()
   UI.addstr('\n')
   UI.addstr("\n")
   UI.addstr('\n')
   UI.addstr("*******************************")
   UI.addstr("*** 1.Student's Information ***")
   UI.addstr("*******************************")
   UI.addstr('\n')
   for i in range(x):
      UI.addstr('\n')
      UI.addstr(f"\n{liststudent[i].student()}") 
   UI.addstr('\n')
   UI.addstr('\n')  
   UI.addstr("*******************************")
   UI.addstr(" ** 2.Course's Information  ** ")
   UI.addstr("*******************************")
   UI.addstr('\n')
   for t in range(r):
      UI.addstr('\n')
      UI.addstr(f"{listcourse[t].mycourse()}")
   UI.addstr('\n')  
   UI.addstr('\n')  
   UI.addstr("*******************************")
   UI.addstr(" **    3.Student's mark     ** ")
   UI.addstr("*******************************")
   UI.addstr('\n')
   for t in range(r): 
      for i in Marklis: 
         if i.course == listcourse[t].name:
            UI.addstr(f'\nStudent {t+1} : {i.number} ')
         else:
            pass


   markslist = [mark.number for mark in Marklis]
   marksarray = np.array(markslist)

   creditslist = [course.mark for course in listcourse]
   creditsarray = np.array(creditslist)

   gpalist = [] #Calculate student
   for i in range(x):
      marksforstudent = marksarray[i*r:(i+1)*r]
      creditsforstudent = creditsarray

      gpaforstudent = np.sum(marksforstudent * creditsforstudent) / np.sum(creditsforstudent)
      gpalist.append(gpaforstudent)

   sortgpa = np.argsort(gpalist)[::-1]
   sortgpa = np.round(sortgpa,1)
   UI.addstr('\n')  
   UI.addstr('\n')  
   UI.addstr("**************************")
   UI.addstr(" ** 4.Student's GPA in descending order ** ")
   UI.addstr("**************************")
   UI.addstr('\n')
   UI.addstr("Sorted Student List by GPA Descending:")
   UI.addstr('\n')
   for i in sortgpa: #Sort student list by GPA descending
      UI.addstr(f"\nStudent {i + 1}: {liststudent[i].name} with GPA {gpalist[i]}")
   UI.getkey()

curses.wrapper(main)