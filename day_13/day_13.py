#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtering_neg = [x for x in numbers if x < 0]

print(filtering_neg)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list_ = [numbers for row in list_of_lists for numbers in row]
print(list_)

#Using list comprehension create the following list of tuples:

'''
[(0, 1, 0, 0, 0, 0, 0),
 (1, 1, 1, 1, 1, 1, 1),
 (2, 1, 2, 4, 8, 16, 32),
 (3, 1, 3, 9, 27, 81, 243),
 (4, 1, 4, 16, 64, 256, 1024),
 (5, 1, 5, 25, 125, 625, 3125),
 (6, 1, 6, 36, 216, 1296, 7776),
 (7, 1, 7, 49, 343, 2401, 16807),
 (8, 1, 8, 64, 512, 4096, 32768),
 (9, 1, 9, 81, 729, 6561, 59049),
 (10,1, 10, 100, 1000, 10000, 100000)]
'''
#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

f_countrie = [(i[0][0],str(i[0][0][:3]).upper(),i[0][1]) for i in countries ]
print(f_countrie)

#Change the following list to a list of dictionaries:
countries1 = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
d_countries = [{'country': i[0][0] , 'city' : i[0][1]} for i in countries1]
print(d_countries)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
conc_names = [str(i[0][0]+' '+ i[0][1] ) for i in names]
print(conc_names)