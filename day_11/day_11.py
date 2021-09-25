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

print()
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(items):
    print(' '.join(items).upper())
capitalize_list_items(('a','b','c','d','e','f','g'))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

def add_item(alist, value):
    return alist + [value] #i know append exists:)
print(add_item(food_staff,'Meat'))

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(rmlist, value):
    n = [x for x in rmlist if x != value]
    return n
print(remove_item(food_staff, 'Potato'))


#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(value):
    print(sum(range(0,value+1)))
sum_of_numbers(100)

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(value):
    print(sum(range(0,value+1,2)))
sum_of_odds(100)

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(value):
    list_even = [x for x in range(1, value + 1) if x % 2 != 0]
    print(sum(list_even))
sum_of_even(100)

#Exercises: Level 2
#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(value):
    list1 = [x for x in range(1, value +1)]
    odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))
    even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))
    return odd_count, even_count
print(evens_and_odds(100))


#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if num == 1:
        return num
    else:
       return num*factorial(num-1)
print(factorial(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(par):
    return len(par) == 0
print(is_empty(()))


#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
from collections import Counter as ct
class stadistic:
    def __init__(self, values):
        self.values = values
    def calculate_mean(self):
        print(sum(self.values)/len(self.values))

    def calculate_median(self):
        n = len(self.values)
        index = n // 2

        if n % 2 : return sorted(self.values)[index]
        return sum(sorted(self.values)[index -1 : index + 1]) / 2
    
    def calculate_mode(self):
        c = ct(self.values)
        mode = [x for x, z in c.items() if z == c.most_common(1)[0][1]]
        return mode
    def calculate_range(self):
        #idk what its range but...
        return [x for x in range(0, len(self.values))]
    def calculate_variance(self):
        m = sum(self.values) / len(self.values)
        var = sum((x - m)**2 for x in self.values) / len(self.values)
    def calculate_std(self):#standar deviation
        var = stadistic.calculate_variance(self)
        #std = math.sqrt(var)
        return var

s1 = stadistic([x for x in range(0, 100)])

print(s1.calculate_mean())
print(s1.calculate_median())
print(s1.calculate_mode())
print(s1.calculate_range())
print(s1.calculate_variance())
print(s1.calculate_std())

    

#Exercises: Level 3
#Write a function called is_prime, which checks if a number is prime.
#Write a functions which checks if all items are unique in the list.
#Write a function which checks if all the items of the list are of the same data type.
#Write a function which check if provided variable is a valid python variable

#Go to the data folder and access the countries-data.py file.
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.