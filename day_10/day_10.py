#Exercises: Level 1

#Iterate 0 to 10 using for loop, do the same using while loop.
i = 0
while (i <= 10):
    print(i)
    i += 1
for k in range(0, 11):
    print(k)

#Iterate 10 to 0 using for loop, do the same using while loop.
print('-'*94)
j = 10
while (j >= 0):
    print(j) 
    j -= 1
for k in range(10, -1,-1):
    print(k)

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print('-'*94)
'''
  #
  ##
  ###
  ####
  #####
  ######
  #######
'''
for k in range(1, 10):
    print('#'*k)


#Use nested loops to create the following:
'''
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''

for k in range(1, 8):
    for h in range(1,8):
        print('# ',end='') 
    print()

#Print the following pattern:
'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
for k in range(0, 11):
    print(f"{k} x {k} = ",k**2)

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
python = ['Python', 'Numpy','Pandas','Django', 'Flask']
for k in python:
    print(k)


#Use for loop to iterate from 0 to 100 and print only even numbers
a = (' '.join(str(x) for x in range(0, 100,2)  ))
print(a)

#Use for loop to iterate from 0 to 100 and print only odd numbers
b = ' '.join(str(x) for x in range(0,100) if x % 2 != 0)
print(b)

#Exercises: Level 2
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
c = 0
for x in range(0,101):
    c += x
print(c)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_odds, sum_evens = 0,0
for x in range(0,101):
    if x % 2 == 0:
        sum_evens += x
    else:
        sum_odds += x
print(sum_evens)
print(sum_odds)

#Exercises: Level 3

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from countries import countries
for x in countries:
    if 'land' in x:
        print(x)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in fruits[::-1]:
    print(i)

'''
Go to the data folder and use the countries_data.py file.

    What are the total number of languages in the data
    Find the ten most spoken languages from the data
    Find the 10 most populated countries in the world
'''
from countries_data import cd 
num_languages = 0
spoken_languages = []
population = {}
for x in range(len(cd)):
    num_languages += len(cd[x]['languages']) 
    spoken_languages.append(''.join(cd[x]['languages']))
    population[cd[x]['name']] = cd[x]['population']
print(num_languages)

#Find the ten most spoken languages from the data
from collections import Counter

Counter = Counter(spoken_languages)

top = Counter.most_common(10)
print(top)


#Find the 10 most populated countries in the world
sorted_population = {k: v for k, v in sorted(population.items(), key=lambda item: item[1], reverse=True)}
count = 0
for aa in sorted_population.items():
    print(aa)
    if count == 10: break
    count += 1
