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
