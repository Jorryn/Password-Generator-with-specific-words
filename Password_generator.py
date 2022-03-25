#import the necessary modules!
import random
import string
import re

def strongweak():
    f = open('D:\Python\MyFile.txt','r')
    v = f.read()
# checking condition for string found or not
    if v == "\n" or v == " ":
        return "Password cannot be a newline or space!"
    
    # the password length should be in
    # between 9 and 20
    if 9 <= len(v) <= 25:
   
        # checks for occurrence of a character 
        # three or more times in a row
        if re.search(r'(.)\1\1', v):
            return "Weak Password: Same character repeats three or more times in a row"
   
        # checks for occurrence of same string 
        # pattern( minimum of two character length)
        # repeating
        if re.search(r'(..)(.*?)\1', v):
            return "Weak password: Same string pattern repetition"
   
        else:
            return "Strong Password!"
   
    else:
        return "Password length must be 9-20 characters!"

def listToString(s): 
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

print('Password Generator. Prediction of Strong and Weak Password!')

#input the length of password
words = input('\nEnter word that you want to use in password: ')

length = int(input('\nEnter the length of password: ')) 
length = length-len(words)                     

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols 

#use random 
temp = random.sample(all,length)

#create the password
password = "".join(temp)

r=random.randint(0, length)
possible = []
for i in range(length):
    possible.append(password[i])
possible.insert(r,words)
pword=listToString(possible)

#print the password
print(pword)

#store the password in a text file
f = open("D:\Python\MyFile.txt","w+")
f.write(pword)
f.close()

#check if the password is strong or weak
print(strongweak())
