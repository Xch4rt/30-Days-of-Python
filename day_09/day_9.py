#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.  
age = int(input("Enter your age: "))

print("Your ould enough to drive" if age >= 18 else "You need {} more years to learn to drive.".format(18 - age))

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 

my_age = 18
your_age = int(input("Enter your age: "))

dif = abs(your_age - my_age)

if my_age > your_age:
    print("im {} years older than you".format(dif))
elif my_age == your_age:
    print("We got the same age")
else:
    print("Im {} years youngest than u".format(dif))

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a,b = (input().split())

if int(a) > int(b):
    print(f"{a} is greater than {b}")
elif int(a) == int(b):
    print('both are equal')
else:
    print(f"{b} is greater than {a}")

#Write a code which gives grade to students according to theirs scores:
'''
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
grades = {
    'F' : [0, 49],
    'D' : [50, 59],
    'C' : [60, 69],
    'B' : [70, 89] ,
    'A' : [80, 100]
}
score = float(input())
if score in range(grades['F'][0], grades['F'][1]+1): print('F')
elif score in range(grades['D'][0], grades['D'][1]+1): print('D')
elif score in range(grades['C'][0], grades['C'][1]+1): print('C')
elif score in range(grades['B'][0], grades['B'][1]+1): print('B')
else: print('A')



#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input('Month: ').lower()

if month in ('january','february','december'): print('winter')
elif month in ('september','october','november'): print('autumn')
elif month in ('march','april','may'): print('spring')
elif month in ('june','july','august'): print('summer')


#The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input('Enter a fruit ').lower()

if fruit not in fruits: 
    fruits.append(fruit) 
    print(fruits)
else :
    print('That fruit already exist in the list')

#Exercises: Level 3

#Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

'''
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''
if 'skills' in person:
    print(person['skills'])
    print()
    if 'Python' in person['skills']:
        print('Yes')
    if ['JavaScript','React'] in person['skills'] and len(person['skills']) and len(person['skills']) == 2:
        print('Is a backend dev')
    elif ['Node','Python','MongoDB'] in person['skills'] and len(person['skills']) and len(person['skills']) == 3:
        print('Is a backend dev')
    elif ['React','Node','MongoDB'] in person['skills'] and len(person['skills']) == 3:
        print('Is a fullstack dev')
    else:
        print('unknown title')
if person['is_married'] and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')
        

