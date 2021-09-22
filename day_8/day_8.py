#Create an empty dictionary called dog

dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name' : 'Pinky',
    'color' : 'White',
    'breed' : 'French puddle',
    'legs' : 4,
    'age' : 7
}

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name' : 'Pablo',
    'last_name' : 'Gutierrez',
    'gender' : 'Male',
    'age' : 18,
    'marital_status' : 'Single',
    'skills' : ['Teamwork','Problem solving','Data Science Jr Skills', 'Organization', 'Analytical Abilities'],
    'country' : 'Nicaragua',
    'city' : 'Managua',
    'address' : 'Av. Milicias 19'
}

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student['skills'])

#Modify the skills values by adding one or two skills
student['skills'].append(['Programming with python','Leadership'])

#Get the dictionary keys as a list
print(student.keys())
print()
#Get the dictionary values as a list
print(student.values())
print()
#Change the dictionary to a list of tuples using items() method
print(student.items())
print()
#Delete one of the items in the dictionary
del student['address']
print()
#Delete one of the dictionaries
del student