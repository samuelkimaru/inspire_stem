# arithmetic progression

a = float(input("enter the first term "))
d = float(input("enter the common difference"))
n = float(input("enter the number if terms"))

n_term =(a + d * (n-1))
print("the nth term of the sequence is:", n_term)


# this is a program to calculate surface area
# surface area of a cylinder
import math

r = int(input("enter the radiys : "))
pi = float(math.pi)
d = int((r * 2))
h = int(input('enter the height'))

c = ((pi * r **2) + (pi *d*h))
print = ((pi * r **2) + (pi * d *h))
print("the surface area of cylinder",c)
# print surface area of a sphere
r = int(input("enter the radius : "))
pi = float(math.pi)

s = ((pi * r **4))
print("the surface area of a sphere",s)
# geometric progression
a = float(input("enter the first term"))
r = float(input("enter the common ratio"))
n = float(input("enter the number of terms"))
n_term = (a * r ** (n-1))
print("the nth term of the sequence is :",n_term)
import matplotib.pyplot as plt
x = [i for i in range(-10,10)]
y1 = [(9 * x + 23)for x in x]
y2 = [((3 * x *x)+ (8 *x)+9) for x in x]
plt.plot(x,y1,'-r',label = 'linear equation')
plt.plot(x,y2,'-b',label = 'quadratic equation')
plt.legend(loc = 'upper right')
plt.show()
plt.plot(x,y1,'-r')
plt.plot(x,y2,'-g')
lst = ['linear equation','quadratic equation']
plt.legend(lst,loc = 'upper right')

