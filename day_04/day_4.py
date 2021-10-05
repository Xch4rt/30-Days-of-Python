#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

t, d, o, p = 'Thirty', 'Days', 'Of', 'Python'
print(t+' '+d+' '+o+' '+p)

print('-'*120)
#Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#Print the variable company using print().
print(company)

print('-'*120)
#Print the length of the company string using len() method and print().
print(len(company))

print('-'*120)
#Change all the characters to uppercase letters using upper() method.
upperC = company.upper()

#Change all the characters to lowercase letters using lower() method.
lowerC = company.lower()

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string = 'coding for all'
cap = string.capitalize()
tit = string.title()
swpcase = string.swapcase()


#Cut(slice) out the first word of Coding For All string.
cut = string[0:6]
print(cut)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(string.index('coding'))

#Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('Coding','Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
string1 = 'Python for Everyone'
print(string1.replace('for Everyone', 'for All'))


#Split the string 'Coding For All' using space as the separator (split()) .
print(string.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
a = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(a.split(','))

#What is the character at index 0 in the string Coding For All.

print(string[0])

#What is the last index of the string Coding For All.
print(string[-1])

#What character is at index 10 in "Coding For All" string.

print(string[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.

print ("".join(e[0] for e in string1.split()))

#Create an acronym or an abbreviation for the name 'Coding For All'.
print ("".join(e[0] for e in string.split()))


#Use index to determine the position of the first occurrence of C in Coding For All.
print(string.index('c'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
string2 = 'Coding For All People'
print(string2.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string3 = 'You cannot end a sentence with because because because is a conjunction'
print(string3.index('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(string3.rindex('because'))


#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(string3[31:55])

#Does ''Coding For All' start with a substring Coding?
print(string.index('coding') == 0)

#Does 'Coding For All' end with a substring coding?
print(string.index('coding') == -1)

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
space = '   Coding For All      '

print(space.strip(' '))

#Which one of the following variables return True when we use the method isidentifier():

f = '30DaysOfPython' #false
t = 'thirty_days_of_python' #true

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(libraries))

