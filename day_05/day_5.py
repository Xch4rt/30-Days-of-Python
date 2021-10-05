# Exercises: Level 1

#Declare an empty list
emptyList = list()

#Declare a list with more than 5 items
lst = ['a','b','c','d','e']

#Find the length of your list
print("""
    Lenght of an empty list: {}
    Lenght of a list with elements: {}
""".format(len(emptyList), len(lst)))

#Get the first item, the middle item and the last item of the list
print("""
    First item: {}
    Middle item: {}
    Last item: {}
""".format(lst[0], lst[int(len(lst) / 2)], lst[-1]))


#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['Pablo', 18,6.2,'Single','AVenida de las milicias, Moseñor lezcano']


#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#Print the list using print()
print(it_companies)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
print()
#Print the list after modifying one of the companies
print("""
    First item: {}
    Middle item: {}
    Last item: {}
""".format(it_companies[0], it_companies[int(len(lst) / 2)], it_companies[-1]))

#Add an IT company to it_companies
it_companies.append('Twitter')

#Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies) / 2), 'HP Enterprise')

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

#Join the it_companies with a string '#;  '
print(' #'.join(it_companies))

#Check if a certain company exists in the it_companies list.
print('IBM' in it_companies)

#Sort the list using sort() method
it_companies.sort()

#Reverse the list in descending order using reverse() method
it_companies.sort(reverse = True)

#Slice out the first 3 companies from the list
print(it_companies[0:3])

#Slice out the last 3 companies from the list
print(it_companies[6:])

#Slice out the middle IT company or companies from the list
print(it_companies)
print(it_companies[4:5])

#Remove the first IT company from the list
print(it_companies.remove(it_companies[0]))

#Remove the middle IT company or companies from the list
print(it_companies.remove(it_companies[int(len(it_companies)/2 - 1)]))
#Remove the last IT company from the list
print(it_companies.pop())
#Remove all IT companies from the list
print(it_companies.clear())
print(it_companies)

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
front_end = front_end + ['Python','SQL','Redux']
print(front_end)
full_stack = front_end + back_end
print(full_stack)

#Exercises: Level 2

#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
print(ages)
print("""
    min: {}
    max: {}
""".format(ages[0], ages[-1]))

#Find the median age (one middle item or two middle items divided by two)



#Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages) 
print(average)

#Find the range of the ages (max minus min)
print(ages[-1] - ages[0])


#Compare the value of (min - average) and (max - average), use abs() method
min_av = ages[0] - average
max_av = ages[-1] - average

print("""
    Min - average: {}
    Max - average: {}
""".format(max_av, max_av))


#Find the middle country(ies) in the countries list
from countries import countries
print(countries[int(len(countries) / 2)])

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
half1 = countries[0: int(len(countries) / 2)]
half2 = countries[int(len(countries) / 2):]
print(half2)
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

f_item, s_item, t_item, *rest = countries1
