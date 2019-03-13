import textwrap, cmd, sys
import pinaceaeKey
import pprint


SCREEN_WIDTH = 80

location = 'start'
a_b_choices = []

welcome = 'Welcome! this program provides a Dichotomous key for identifiying pine trees in the North Eastern Contintental US. '

continent_question = 'Please choose a the continent you are located on'
continents = [
  'North America',
  'South America',
  'Australia',
  'Africa',
  'Europe',
  'Asia']

choose_a = pinaceaeKey.choose_a


next_binary = pinaceaeKey.pinus_binary_location[11][choose_a]
next_binary = pinaceaeKey.pinus_binary_location[next_binary]
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(next_binary) 

def defineLocation(loc):
  """defines where the user is in the binary tree"""
  print(loc.a, '\n', loc.b)

def chooseFromOptions(parent, new):
  """allows the user to pick which statement is true about their specimen"""
# binary tree item you chose
# if htis points to another option, display that, 
# if this points to an actuall result, run the build display result function



# print(PINACEAE['Pinus'])
# print(welcome, '\n', continent_question)
# print(continents)
# print(define_location)

