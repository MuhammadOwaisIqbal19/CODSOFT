
#--------------------------------------------RANDOM PASSWORD GENERATOR---------------------------------------
#IMPORTING LIBRARIES
import string
import random

#TAKING INPUT FROM THE USER
PasswordLen=int(input('How much Characters your Password Should contain?\n: '))
password=''
for i in range(PasswordLen):
    password+=random.choice(string.printable)


print('Your Password generated is :',password)
