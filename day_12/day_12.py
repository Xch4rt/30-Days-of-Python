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