#Recursion
def factorial(x):
    if x == 1 or x==0:
        return 1 
    else:
        return (x * factorial(x-1))
num = 3
print( factorial(num))

#Lambda() inside an another function
def func(n):
      return lambda a : a * n

double = func(2)
triple = func(3)

print(double(4))
print(triple(5))

#Create a file and use read, write, open, with open and append functions

f=open("c.txt",'x')
f.write("How are you")
f.close()
f=open("c.txt",'a')
f.write("good")
f.close()
f =open("c.txt","r")
print(f.read())
f.close()
with open("c.txt") as f:
    print(f.read())