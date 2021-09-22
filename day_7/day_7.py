# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Exercises: Level 1
#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')

#Insert multiple IT companies at once to the set it_companies
other_itCompanies = {'Alibaba','Intel','Tencent','Paypal'}
print(it_companies.union(other_itCompanies))

#Remove one of the companies from the set it_companies
it_companies.remove('Apple')
print(it_companies)


#Exercises: Level 2

#Join A and B
A.union(B)

#Find A intersection B
A.intersection(B)

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
A.update(B)
B.update(A)


#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#Delete the sets completely
del A

#Exercises: Level 3

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = set(age)
print(""" 
    Length of set ages: {}
    Length of list ages: {}
""".format(len(age), len(ages)))

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
string = 'I am a teacher and I love to inspire and teach people'.split()

set_string = set(string)
print(len(set_string))