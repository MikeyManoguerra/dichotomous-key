#Python CLI dichotomous key for Pinus genus

## What is this?

  This program is the result of my flex week self study of Python programming language. 


## What does it do?

  The program is a command line interface that is similar to a text adventure style game. The assumptions for successful use of this tool is that: 

  #### You are located in the Eastern Continental United States.

  #### The tree you are trying to identify is in the *Pinus* genus.

  #### The tree is a native species.

  If these things are true, You can run the program using ```python3 CLI-key.py``` in your terminal.

  The program will prompt you with binary statements, And you enter **a** or **b** depending on which is true. When the program leads you to an end node, it provides you with statements about the characteristics of the tree, and provides more information when you enter ```more```. If you have another pine to identify, or the key did not lead to correct result, ```back``` will allow you to traverse up the dichotomous key.

  ## Technologies 

  This app is written completely in python. The list of species came from  wikipedia's 
  [trees and shrubs](https://en.wikipedia.org/wiki/List_of_trees_and_shrubs_by_taxonomic_family)
  page.  I spent a decent amount of time seperating this list into a usable dictionary object, as the whole list was provided by the wiki scraping api as a single string. The code that I did this with is in the 'utils/wiki.py' file. This app only uses a small subset of the 'pinaceaeFile.json' file, with the characteristics added to the trees that exist 
  in the program are inserted in 'easternPinusBuilder.py'

  The summaries provided upon a ```more``` entry are also provided via the wiki api.

  The navigation is a binary tree data structure.

  ## Reflection

  I like python's direct, simple syntax. 
  Python seemed to constantly be directing me away from variables towards strings, and in some ways I feel like I was fighting it by creating variables that just equal the same thing as a string. 

  I did not embrace Classes early enough in this project, and thus I typed out alot more than necessary and then refactored, or realized that I could have done more data building programatically. 
  However, it was a good experience to basically have the app working with dictionaries as the species objects, then refactoring them into Classes with json seed data. I think it should be relatively easy to expand into other species to key.

  I wish I could have built the binary key programatically instead of typing out the parent/child relationships. The hardest part of this project might actually have been deciding and modelling the branch points for the questions, I am only a citizen naturalist! 

  I also originally planned to use the whole *Pinaceae* Family to do some sort of info navigation, but even if this program had been just informational instead a tool, It was too much data to process in one week. the final count for species is 15, instead of the 220+ in *Pinaceae* . It only covers a subset of the Genus *Pinus* even, as evidenced in the 'pinaceaeFile.json' 

  ## Thank Yous and Resources

  Chris Angelico (Rosuav), Mentor and python guide

  Peterson Field Guides: Eastern Trees by George A. Petrides/ Janet Wehr

  Used to pair down the huge *Pinaceae* family and provided guidance on the binary options

  [Wikipedia](https://www.wikipedia.org/)forever

  [this](https://inventwithpython.com/blog/2014/12/11/making-a-text-adventure-game-with-the-cmd-and-textwrap-python-modules/) guide to building a text adventure game got me started, and makes me want to add a tree combat feature!
  

