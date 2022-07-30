import random

print("Password Generator")
print("========================")

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*().,?0123456789"

number = input("amount of passwords to generate: ")
number = int(number) 

length = input("password length: ")
length = int(length)

print("\n Here are your passwords: ")

for passw in range(number):
    password = ""
    for l in range(length):
        password += random.choice(chars) 
    print(password)