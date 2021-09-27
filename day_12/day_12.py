#Excersises Level 1
#Writ a function which generates a six digit/character random_user_id. 
import random
import string

def random_user_id(x):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(x)])

print(random_user_id(6))

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    length = int(input("How many characters do u want: "))
    ids = int(input("how many ids do u want generate: "))

    for i in range(0, ids):
        print(random_user_id(length))

user_id_gen_by_user()

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    rgb = list()
    for x in range(3):
        rgb.append(random.randint(0, 255))
    return 'rgb({},{},{})'.format(rgb[0],rgb[1],rgb[2])    
print(rgb_color_gen())

#Excersises Level 2

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
hexa = list()
def list_of_hexa_colors():
    for x in range(6):
        hexa.append("#{:06x}".format(random.randint(0,256**3)))
    print(hexa)
list_of_hexa_colors()

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
list_rgb = list()
def list_of_rgb_colors():
    for i in range(random.randint(1, 100)):
        list_rgb.append(rgb_color_gen())
    return list_rgb
print(list_of_rgb_colors())