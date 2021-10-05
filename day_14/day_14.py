countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'MyLand','land']
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

#Use filter to filter out countries containing 'land'.
f_list = filter(lambda x: 'land' in x.lower(), countries)
print(list(f_list))

#Use filter to filter out countries having exactly six characters.
ff_list = filter(lambda x: len(x) == 6, countries)
print(list(ff_list))

#Use filter to filter out countries containing six letters and more in the country list.
fff_list = filter(lambda x: len(x) >= 6, countries)
print(list(fff_list))