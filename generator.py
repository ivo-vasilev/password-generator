#!/usr/bin/python3

import random

running = True

print("\n* * * Password Generator * * *\n")
print("(c)2022 Ivaylo Vasilev" + "\nTo exit the program enter 0\n")

def generator():
    low = "abcdefghijklmnopqrstuvwxyz"
    upp = "ABCDEFGHIJKLMNOPQRSTUVXXYZ"
    numb = "0123456789"
    symb = "@#!?-*."

    all = low + upp + numb + symb

    while True:
        length = int(input("Password length: "))
        if length >= 8 and length <= 32:
            break
        elif length == 0:
            global running
            print("Thank you for using Password Generator!\n")
            running = False
        else:
            print("Please specify a password length between 8 and 32 symbols!\n")

        return length

    password = "".join(random.sample(all, length))

    print("*" * 16)
    print("Your password is:", password)
    print("=" * (18 + length) + "\n")


while running:
    generator()
