countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use for to print each name in the names list.
for x in countries:
    print(x)

#Use for to print each number in the numbers list.
for x in numbers:
    print(x)

#Excercises Level 2
#Use map to create a new list by changing each country to uppercase in the countries list
n_list = map(lambda x: x.upper(), countries)
print(list(n_list))

#Use map to create a new list by changing each number to its square in the numbers list
nn_list = map(lambda x: x**2, numbers)
print(list(nn_list))

#Use map to change each name to uppercase in the names list
nnn_list = map(lambda x: x.upper(), names)
print(list(nnn_list))