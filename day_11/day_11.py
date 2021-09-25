#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(n1, n2):
    return n1+n2
print(add_two_numbers(43,12))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math
def area_of_circle(r):
    return math.pi * r ** 2
print(area_of_circle(4))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
booleand_values = list()
def add_all_nums(*args):
    for i in range(len(args)):  
        booleand_values.append('<class \'int\'>' == str(type(args[i])))
    if len(booleand_values) == len(args) and True in booleand_values:
        print(sum(args))
add_all_nums(1,2,3,4,4,5)

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(c):
    return c * (9/5) + 32
print(convert_celsius_to_fahrenheit(23))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month in ('january','february','december'): print('winter')
    elif month in ('september','october','november'): print('autumn')
    elif month in ('march','april','may'): print('spring')
    elif month in ('june','july','august'): print('summer')
check_season('february')

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(values):
    return (float)((values[3] - values[1])/(values[2] - values[0])) #values[0] = x1, values[1] = y1, values[2] = x2, values[3] = y2
print(calculate_slope((12,43,5,65)))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath
def solve_quadratic_eqn(values_eq):
    a,b,c = values_eq[0], values_eq[1], values_eq[2]
    d = (b**2) * (4 * a * c)

    sol1 = (-b-cmath.sqrt(d))/(2*a)  
    sol2 = (-b+cmath.sqrt(d))/(2*a) 
    return sol1, sol2
print(solve_quadratic_eqn((8,5,9)))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# 8
def print_list(plist):
    return ' '.join(plist)
print(print_list(('2','2','4','43','a','b','c','d','ee')))

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
#9
def reverse_list(rlist):
    for i in range(len(rlist),0,-1):
        print(i, end=" ")
reverse_list((1,2,3,4,5,6,7,8,9))

