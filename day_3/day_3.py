#Declare your age as integer variable
my_age = 18

#Declare your height as a float variable
my_height = 6.2 #feets

#Declare a variable that store a complex number
complx_num = 1 + 2j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b, h = input().split() 
print('Area is ', (0.5 * float(b) * float(h)))

print('-' * 120)
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a, b, c = input().split()

print('Perimeter of the triangle is: ', int(a) + int(b) + int(c))

print('-' * 120)
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

l, w = input().split()
area = float(l) * float(w)
perimeter = 2 * (float(l) + float(w))
print("""The are of the rectangle is: {}
        The perimeter of the rectangle is: {}
    """.format(area, perimeter))

print('-'*120)
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

import math
r_cirlce = float(input())

area = math.pi * r_cirlce ** 2
circumference = 2 * math.pi * r_cirlce

print(""" 
        The area of the circle is: {}
        The circumference is: {}
    """.format(area, circumference))
print('-' * 120)
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_int = 1
y_int = -2
slope = 2
print("""
    x-intercept is {}
    y-intercept is {}
    slop is {}
    """.format(x_int, y_int, slope))
print('-'*120)
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
coords = [[2,2], [6,10]]
slope1 = (coords[1][1] - coords[0][1]) / (coords[1][0] - coords[0][0])
euc_dist = (coords[1][0] - coords[0][0])**2 + (coords[1][1] - coords[0][1])**2
print(euc_dist)

print('-' * 120)
#Compare the slopes in tasks 8 and 9.
print(""" 
== {}
!= {}
>  {}
<  {}
>= {}
<= {}
""".format(
    slope == slope1,
    slope != slope1,
    slope > slope1,
    slope < slope1,
    slope >= slope1,
    slope <= slope1
))

print('-'*120)
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
a, b, c = 1, 6 ,9

d = (b**2) - (4 * a * c)
sol1 = (-b-math.sqrt(d)) / (2 * a)
sol2 = (-b+math.sqrt(d)) / (2 * a)

print(sol1 if ((sol1)**2 + 6 * (sol1) + 9) == 0 else sol2 )

print('-'*120)
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python')
print('on' in 'dragon')

print('-'*120)
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
word = 'jargon'
print(word in sentence)

print('-'*120)
#Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))

print('-'*120)
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

number = 4
print(number % 2 == 0)

print('-'*120)
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == 2.7)

print('-'*120)
#Check if type of '10' is equal to type of 10
a, b = '10', 10
print(type(a) == type(b))

print('-'*120)
#Check if int('9.8') is equal to 10
a = int('9.8')
print( a == 10)

print('-'*120)
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours, rate_per_hour = input().split()

print("Your weekly earning is: ", float(hours) * float(rate_per_hour))

print('-'*120)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = int(input("Years you have lived: "))

print((year * 365) * 86400) #seconds in a day

print('-'*120)
#Write a Python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

for x in range(1, 6):
    for y in range(1, 6):
        if y == 0:
            print(1)
        













