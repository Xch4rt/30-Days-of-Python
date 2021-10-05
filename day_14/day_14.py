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

#Use filter to filter out countries starting with an 'E'
firstE = filter(lambda x: x[0].lower() == 'e', countries)
print(list(firstE)) 

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_list(list_):
    return filter(lambda x: 'str' in str(type(x)), list_)
print(list(get_string_list((1,2,'as','asdf','fasd',3,'s'))))

#Use reduce to sum all the numbers in the numbers list.
#total = reduce((lambda x,y: x+y), numbers) actually reduce is deprecated, we need to install functools n import from this 

#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries import countries as c
commons = ['land','la','island','stan']

def categorize_countries():
    return list(filter(lambda x: commons[0] in x or commons[1] in x or commons[2] in x or commons[3] in x, c))
print(categorize_countries())

#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.