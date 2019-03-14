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

location = pinaceaeKey.pinus_binary_location[11]
next_binary = pinaceaeKey.pinus_binary_location[42]  # [choose_a]
your_tree = ''
print(location)

welcome = 'Welcome! this program provides a Dichotomous key for identifiying pine trees in the North Eastern Contintental US. '


def defineLocation(loc):
    """defines where the user is in the binary tree"""
    # print(loc)
    if not your_tree:
      print(loc[a], '\n', loc[b])

    print(your_tree)


def getSpeciesInfo(species_string):
    """gets species information from data storage"""
    global your_tree
    your_tree = pinaceaeKey.North_American_Pines[species_string]
    defineLocation('yay')
  


def checkForResult(route):
    """checks if chosen path is result or a route"""
    global location
    if type(route) == int:
        location = pinaceaeKey.pinus_binary_location[route]
        defineLocation(location)
    elif type(route) == str:
        getSpeciesInfo(route)


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



class TreeIdCmd(cmd.Cmd):
  prompt ='\n>'
  # The default() method is called when none of the other do_*() command methods match.
  def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')
  # A very simple "quit" command to terminate the program:
  def do_quit(self, arg):
      """Quit the game."""
      return True # this exits the Cmd application loop in TextAdventureCmd.cmdloop()
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


if __name__ == '__main__':
    print('Id a Pine Tree!')
    print('====================')
    print()
    print('(Type "help" for commands.)')
    print()
    defineLocation(location)
    TreeIdCmd().cmdloop()
    print('Thanks for playing!')