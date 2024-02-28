# this is a program to calculate salary increament
# date : 26/2/2024
# name : muchiri

employee_name = input(" enter your name :")
age = input(" enter your age :")
salary = int(input("enter your salary:"))
bonus = int(input("enter your bonus :"))
print("name: ",employee_name)
print("age:",age)
print ("salary:",salary)
print("bonnus",bonus)

if salary <= 100000 :
 salary = salary * 0.3 + salary
 print (salary)
elif salary <= 150000 :
 salary = salary * 0.15 + salary
 print(salary)
else :
 salary = salary * 0.05 + salary
 print(salary)

