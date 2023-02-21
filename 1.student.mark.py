import os

print("Input number of students in a class:")
x =  int(input())
qw = []
y = []
z = []
n = []
for i in range(x):
    y.append(i)
    z.append(i)
    n.append(i)
    print("Input students",i+1,"ID")
    y[i] = input()  
    print("INput students",i+1,"names:")
    z[i] = input()
    print("Student",i+1,"DoB")
    n[i] = input()
print(y,z,n)


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
print(d,q)

print("Select a course you want to input mark:")
e = input()
if e in q:
 print("Mark:")
 c = int(input())
else:
 print("Please select the course again.")


