#Exercises: Level 1

#Create an empty tuple
empty = tuple()
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
names = ('Danisha','Quanisha','Quimisha','Dominic','Dionicio')

#How many siblings do you have?
print(len(names))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = names + ('Dua', 'Bua')


#Exercises: Level 2

#Unpack siblings and parents from family_members
s1,s2,s3,b1,b2,f,m = family_members

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Banana','Apple','Wattermelon','strawberries')
vegetables = ('lettuce','pumpkin','potato','onion')
animal = ('cheese','eggs','butter','bacon','milk')

food_stuff_tp = fruits + vegetables + animal

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[6:7])

#Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[10:13])

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
t = ('a','b')
print('a' in t)
#Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)