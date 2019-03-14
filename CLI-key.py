import textwrap
import cmd
import sys
import pinaceaeKey
import pprint
pp = pprint.PrettyPrinter(depth=4)


SCREEN_WIDTH = 80


choose_a = pinaceaeKey.choose_a
a = pinaceaeKey.a
b = pinaceaeKey.b
c = pinaceaeKey.c
choose_a = pinaceaeKey.choose_a
choose_b = pinaceaeKey.choose_b
choose_c = pinaceaeKey.choose_c

location = pinaceaeKey.pinus_binary_location[22]
next_binary = pinaceaeKey.pinus_binary_location[42]  # [choose_a]


welcome = 'Welcome! this program provides a Dichotomous key for identifiying pine trees in the North Eastern Contintental US. '


def defineLocation(loc):
    """defines where the user is in the binary tree"""
    # print(loc)
    print(loc[a], '\n', loc[b])


def chooseCharacteristics(chosen_path):
    """allows the user to pick which statement is true about their specimen"""
    if chosen_path == a:
        print(location[choose_a])
    if chosen_path == b:
        print(location[choose_b])
    if chosen_path == c and location == 22: # not working yet
        print(location[choose_c])
# binary tree item you chose
# if htis points to another option, display that,
# if this points to an actuall result, run the build display result function



print(defineLocation(location))
# TEMPORARY CODE:
while True:
    defineLocation(location)
    response = input()
    if response == 'quit':
        break
    if response in (a, b):
        chooseCharacteristics(response)
