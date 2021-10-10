#Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
def words_lines(path):
    file = open(path,'r')
    file1 = open(path,'rt')
    line_count = 0
    
    for line in file:
        if line != '\n':
            line_count += 1
    data = file1.read()
    words = data.split()
    file.close()
    file1.close()
    return  (''' 
        Number of lines: {}
        Number of words: {}
    '''.format(line_count,len(words)))

# a) Read obama_speech.txt file and count number of lines and words 
print(words_lines("obama_speech.txt"))



# b) Read michelle_obama_speech.txt file and count number of lines and words 
print(words_lines('michelle_obama_speech.txt'))

# c) Read donald_speech.txt file and count number of lines and words 
print(words_lines('donald_speech.txt'))
# d) Read melina_trump_speech.txt file and count number of lines and words
print(words_lines('melina_trump_speech.txt'))

#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
from collections import Counter
import json

def most_spoken_languages(path, n):
    with open(path, encoding="utf8") as json_f:
        data_j = json.load(json_f)
    spoken_languages = []
    for x in range(len(data_j)):     
        spoken_languages.append(''.join(data_j[x]['languages']))
     
    return Counter(spoken_languages).most_common(n)

print(most_spoken_languages('countrie_data.json', 10))


#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries(path,n):
    with open(path, encoding='utf8') as json_f:
        data_j = json.load(json_f)
    populated_c = {}
    for x in range(len(data_j)):
        populated_c[data_j[x]['name']] = data_j[x]['population']
        #population[cd[x]['name']] = cd[x]['population']
    sorted_population = {k: v for k, v in sorted(populated_c.items(), key=lambda item: item[1], reverse=True)}
    count = 0
    countries = []
    for aa in sorted_population.items():
        countries.append(aa)
        if count == n: break
        count += 1
    return countries
print(most_populated_countries('countrie_data.json',3))

