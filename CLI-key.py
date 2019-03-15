import textwrap
import cmd
import sys
import pinaceaeKey
import pprint
pp = pprint.PrettyPrinter(depth=4)


SCREEN_WIDTH = 80

a = pinaceaeKey.a
b = pinaceaeKey.b
c = pinaceaeKey.c
choose_a = pinaceaeKey.choose_a
choose_b = pinaceaeKey.choose_b
choose_c = pinaceaeKey.choose_c
parent = pinaceaeKey.parent
current = pinaceaeKey.current

location = pinaceaeKey.pinus_binary_location[11]
next_binary = pinaceaeKey.pinus_binary_location[42]  # [choose_a]
your_tree = None


welcome = 'Welcome! this program provides a Dichotomous key for identifiying pine trees in the Eastern Contintental US. '


def defineLocation(entry):
    """defines where the user is in the binary tree"""
    if entry == location:

        print(location[a] + ' ---press "a"',
              '\n\n', location[b] + ' ---press "b"')
    else:

        print(entry)


def getSpeciesInfo(species_string):
    """gets species information from data storage"""
    global your_tree
    your_tree = pinaceaeKey.Pinus_Class_Dictionary[species_string].display_characteristics(
    )


def checkForResult(route):
    """checks if chosen path is result or a route"""
    global location

    if type(route) == int:
        location = pinaceaeKey.pinus_binary_location[route]
        defineLocation(location)
    if type(route) == str and route != 'HEAD':
        getSpeciesInfo(route)
    if route=='HEAD':
        print('\n\n','This is the farthest back you can go! perhaps your tree is not in the genus Pinus?', '\n\n')
        defineLocation(location)

def chooseCharacteristics(chosen_path):
    """allows the user to pick which statement is true about their specimen"""
    if chosen_path == a:
        checkForResult(location[choose_a])
    if chosen_path == b:
        checkForResult(location[choose_b])
    if chosen_path == c and location == 22:  # not working yet
        print(location[choose_c])
# binary tree item you chose
# if htis points to another option, display that,
# if this points to an actuall result, run the build display result function


def goBackOneLevel():
    global location
    global your_tree
    if your_tree == None:
        checkForResult(location[parent])
    else:
        your_tree = None
        checkForResult(location[current])


class TreeIdCmd(cmd.Cmd):
    prompt = '\n>'
    # The default() method is called when none of the other do_*() command methods match.

    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')
    # A very simple "quit" command to terminate the program:

    def do_quit(self, arg):
        """Quit the game."""
        return True  # this exits the Cmd application loop in TextAdventureCmd.cmdloop()

    def help_combat(self):
        print('Combat is not implemented in this program.')

    # These direction commands have a long (i.e. north) and show (i.e. n) form.
    # Since the code is basically the same, I put it in the moveDirection()
    # function.
    def do_a(self, arg):
        """Go to the area to the north, if possible."""
        chooseCharacteristics('a')

    def do_b(self, arg):
        """Go to the area to the south, if possible."""
        chooseCharacteristics('b')

    def do_c(self, arg):
        """Go to the area to the east, if possible."""
        chooseCharacteristics('c')

    def do_back(self, arg):
        """go back a level"""
        goBackOneLevel()

    # def do_head(self, arg):


if __name__ == '__main__':
    print('Id a Pine Tree!')
    print('====================')
    print()
    print('(Type "help" for commands.)')
    print()
    defineLocation(location)
    TreeIdCmd().cmdloop()
    print('Thanks for playing!')
