#Day 2: 30 Days of python programming

# Exercises: Level 1
# Declare a first name variable and assign a value to it
first_name = 'Pablo'


# Declare a last name variable and assign a value to it
last_name = 'Gutierrez'

# Declare a full name variable and assign a value to it
full_name = first_name + last_name

# Declare a country variable and assign a value to it
country = 'Nicaragua'

# Declare a city variable and assign a value to it
city = 'Managua'

# Declare an age variable and assign a value to it
age = 18

# Declare a year variable and assign a value to it
year = 2021

# Declare a variable is_married and assign a value to it
is_married = False

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = False

# Declare multiple variable on one line
a, b, c = 1, 'a', 12.2

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print("""
    Type String: city is {}
    Type Boolean: is_married is {}
    Type Float: c is {}
    Type Int: age is {}
    """.format(type(city), type(is_married), type(c), type(age)))

# Using the len() built-in function, find the length of your first name
print("The length of my first name is {}".format(len(first_name)))

# Compare the length of your first name and your last name
print("Comparing my first name length with my last name lenght")
print("""
        Length of my first name = {}
        Length of my last name = {}
        """.format(len(first_name), len(last_name)))

# Declare 5 as num_one and 4 as num_two 
num_one, num_two = 5, 4

    # i.Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

    # ii.Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

    # iii.Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

    # iv.Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two

    # v.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

    # vi.Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

    # vii.Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters. 
r_circle = 30
    # i.Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
print("The area of the circle is {:.2f}".format(math.pi * r_circle**2))

    # ii.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
print("The circumference is {:.2f}".format(2 * math.pi * r_circle))

r_circle2 = input("The radios of the circle: ")
print("The area is {:.2f}".format(math.pi * float(r_circle2) ** 2))

print('-' * 120)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

name = input("Your name: ")
l_name = input("Your last name: ")
countrY = input("Your country: ")
age1 = input("Your age: ")


















