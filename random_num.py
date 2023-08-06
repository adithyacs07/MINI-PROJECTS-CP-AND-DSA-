# i have made a slight changes as this code wont ask total number of charecter; 
# insted this code directly asks the number charecters,numbers and symbols and generated a random password
import random as r

# input
n = int(input("How many numbers do you want in your password? "))
l = int(input("How many letters do you want in your password? "))
s = int(input("How many symbols do you want in your password? "))

# list of all the possible characters
characters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", ":", ";", ".", ",", "<", ">", "?", "/"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# random password
password = ""
for i in range(n):
    password += r.choice(characters[:30])
for i in range(l):
    password += r.choice(numbers[:30])
for i in range(s):
    password += r.choice(symbols[:30])

# Print the password to the user.
print("Your password as your requirement is: ", password,)