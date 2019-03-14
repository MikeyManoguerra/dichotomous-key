import wikipedia
import pprint

family_list = wikipedia.WikipediaPage(
    "List of trees and shrubs by taxonomic family").content

split_list = family_list.split('====')
for string in split_list:
    if 'Pinaceae' in string:
        pinaceae_index = split_list.index(string)
temp_pinaceae = split_list[pinaceae_index: (pinaceae_index+2)]
genus_string = temp_pinaceae[1]

temp1 = genus_string.split('Cedrus', maxsplit=1)
fir_string = temp1[0]

temp2 = temp1[1].split('Larix', maxsplit=1)
cedar_string = 'Cedrus' + temp2[0]

temp3 = temp2[1].split('Picea', maxsplit=1)
larix_string = 'Larix' + temp3[0]

temp4 = temp3[1].split('Pinus', maxsplit=1)
picea_string = 'Picea' + temp4[0]

temp5 = temp4[1].split('Pseudotsuga', maxsplit=1)
pinus_string = 'Pinus' + temp5[0]

temp6 = temp5[1].split('Tsuga', maxsplit=1)
pseudotsuga_string = 'Pseudotsuga' + temp6[0]

tsuga_string = 'Tsuga' + temp6[1]

genus_string_list = [fir_string, cedar_string, larix_string, picea_string,
                     pinus_string, pseudotsuga_string, tsuga_string]

# print(pinus_string)

def splitLatinCommonNames(list_entry):
    """list of strings  formated 'taxonomic name - common name'
    and make a list of nested two item lists """
    parsed_genus = []
    for species in list_entry:
        if(species != ''):
            common_latin_list = species.split(' – ')
            parsed_genus.append(common_latin_list)
    return parsed_genus


def processGenusStringsList(lst_entry):
    """list of genus strings to nested lists"""
    parsed_family_list = []
    for string in lst_entry:
        string_list = string.splitlines()
        parsed_genus = splitLatinCommonNames(string_list)
        parsed_family_list.append(parsed_genus)
    return parsed_family_list

nested_names_list = processGenusStringsList(genus_string_list)
outlier = nested_names_list[4][39][0].split(' - ')
nested_names_list[4][39] = outlier

def buildNestedTaxonomy(nested_species):
    """takes genus nested list and builds a nested dictionary"""
    taxonomic_dict = {}
    index = 0
    this_genus = nested_species[0][0]
    taxonomic_dict[this_genus] = {'common name': nested_species[0][1]}
    taxonomic_dict[this_genus] = {'species': {}}
    for genus in nested_species:
        if index == 0:
            index += 1
        taxonomic_dict[this_genus]['species'][genus[0]] = {
            'scientific name': genus[0],
            'common name': genus[1], 'characteristics': []}
        index += 1
    return [this_genus, taxonomic_dict]

nested_family_dict ={}
for genus in nested_names_list:
    nested_genus = buildNestedTaxonomy(genus)
    nested_family_dict[nested_genus[0]] = nested_genus[1][nested_genus[0]]

print(nested_family_dict)

# pp = pprint.PrettyPrinter(depth=3)
# pp.pprint(nested_family_dict)


# Pinaceae = {
#  type: Family,
#  genus: ['Cedrus','Larix','Picea','Pinus','Pseudotsuga','Tsuga']
#   Cedrus:{
# common_name: 'cedars'
#    species:{
#       latin name:
#       common name:
#       description:
#       }
#    }
#   Larix:
#   Picea:
#   Pinus:
#   Pseudotsuga:
#   Tsuga:
# }
