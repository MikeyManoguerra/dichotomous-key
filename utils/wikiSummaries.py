import wikipedia
from easternPinusBuilder import *
import json

description_object = {}
for tree in Eastern_American_Pines:

  summary = wikipedia.summary(tree)
  description_object[tree] = summary



#######Builds summary Json file#########
# with open('easternPinusSummaries.json', 'w') as write_file:
#   json.dump(description_object, write_file)


#enum class