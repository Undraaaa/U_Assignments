
age=float(input('Please enter your age: '))
if age<=30:
    print("Less than 30 years old")
else:
    print("Greater than 30 years old")

################
x=float(input("Enter any x: "))
x_sqr=x**3
print(x)

#################
x = list(map(int, input().split()))
print(x)
y = list(map(int, input().split()))
print(y)

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()

##############
i=1
n=int(input("Input how many elements in array??"))
x = [ float(input()) for i in range(n)]

################
#load library
import matplotlib.pyplot as plt
vec_x=input()
vec_y=input()
plt.scatter(vec_x,vec_y)
plt.show()

################
#load library
import datetime #as dt # time, date, datetime
today=datetime.date.today()
#print("Today year is:", today.year)
#print("Today month is:", today.month)
#print("Today day is:", today.day)
todaydate=datetime.date(month=today.month, year=today.year, day=today.day)
print("Today date is: ", todaydate)

# Birth date
year1=int(input("birth year: "))
month1=int(input("birth month: "))
day1=int(input("birth day: "))
birthdate=datetime.date(month=month1, year=year1, day=day1)
print("Birth date is: ", birthdate)

age = todaydate.year - birthdate.year - ((todaydate.month, todaydate.day) < (birthdate.month, birthdate.day))
print(age) 

#################
#load library
import numpy as np
vector = np.array([1, 2, 3, 4, 5, 6])
print()
print("Original Vector:)


x=[1, 2, 3, 4, 5, 6, -10, -33, -11, -5, -2] 
pos_count=0
neg_count=0
for num in x:
    # checking condition
    if num >= 0:
        pos_count=pos_count+1
    else:
        neg_count=neg_count+1
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)



