print("Input number of students in a class:")
x =  int(input())
y = []
z = []
n = []
for i in range(x):
    y.append(i)
    z.append(i)
    n.append(i)
    print("Input students",i+1,"ID")
    y[i] = input()  
    print("Input students",i+1,"name:")
    z[i] = input()
    print("Student",i+1,"DoB")
    n[i] = input()

print("Input number of courses in a class:")
r =  int(input())  
d = []
q = [] 
for t in range(r):
    d.append(t)
    q.append(t)
    print("Input course",t+1,"id:")
    d[t] = input()
    print("Input course",t+1,"name:")
    q[t] = input()

print("Select a course name you want to input mark for student:")
e = input()
b = []
k = []
if e in q:
 for i in range(x):
  b.append(i)
  print("Input mark for student",i+1,":")
  b[i]= int(input())
else:
  print("Please select the course again.")

print("***************************************************************************************************************************************************************")
print("                              **                    1. Student's name.                                   **")
print("                              **                    2. Student's ID.                                     **")
print("                              **                    3. Student's DOB.                                    **")
print("                              **                    4. Course's name.                                    **")
print("                              **                    5. Course's ID.                                      **")
print("                              **                    6. Select a course to input mark.                    **")
print("                              **                    7. Input mark for student.                           **")
print("                              **                    8. Print the lists.                                  **")
print("****************************************************************************************************************************************************************")


for i in range(x):
 print('\n'"Student",i+1,"ID:",y[i],'\n'"Student",i+1,"name:",z[i],'\n'"Student",i+1,"DOB:",n[i])
for t in range(r):
 print('\n'"Course",t+1,"ID:",d[t],'\n'"Course",t+1,"name",q[t])

print('\n'"Student in course",q[t])
for i in range(x):
  print("Student",i+1,"mark:",b[i])
