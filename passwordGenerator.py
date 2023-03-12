#!/usr/bin/env python3

import string
import random
 
#input password length
length = int(input("Enter password length: "))

print('')
 
print('''Choose what options to include in password:
**Choose option 5 when done picking options**
    1. Lowercase Letters
    2. Numbers
    3. Special characters
    4. Uppercase Letters
    5. Done''')
 
pwOptions = ""
 
print('')
 
#get password options user wants to use and add them to pwOptions
while True:
    option = int(input("Pick an option (1-5): "))
    if(option == 1):
#add lowercase letters
        pwOptions += string.ascii_lowercase
    elif(option == 2):
#add numbers
        pwOptions += string.digits
    elif(option == 3):
#add special characters
        pwOptions += string.punctuation
    elif(option == 4):
#add uppercase letters
        pwOptions += string.ascii_uppercase
    elif(option == 5):
        break
    else:
        print("Pick an option 1-5 only")
 
password = []

for i in range(length):
   
#get random options from password options and add them to password
    randomoptions = random.choice(pwOptions)
    password.append(randomoptions)

print('')

#printing password as a string
print("Password: " + "".join(password))