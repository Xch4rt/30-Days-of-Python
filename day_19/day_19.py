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
def most_spoken_langauges(path):
    pass


#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries