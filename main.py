import random
from time import sleep as slp

def type(text):
    for char in text:
        print(char, end='', flush=True)
        slp(0.075)

slp(1)
type("Hello there! :)")
slp(1)
print(" ")
type("Welcome to My 21 Days of Python Challenge!")