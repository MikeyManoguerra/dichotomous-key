import pprint

PINACEAE = {'Abies': {'species': {'Abies': {'scientific name': 'Abies', 'common name': 'fir trees', 'characteristics': []}, 'Abies amabilis': {'scientific name': 'Abies amabilis', 'common name': 'Pacific silver fir; amabilis', 'characteristics': []}, 'Abies balsamea': {'scientific name': 'Abies balsamea', 'common name': 'balsam fir', 'characteristics': []}, 'Abies concolor': {'scientific name': 'Abies concolor', 'common name': 'white fir', 'characteristics': []}, 'Abies fraseri': {'scientific name': 'Abies fraseri', 'common name': 'Fraser fir', 'characteristics': []}, 'Abies grandis': {'scientific name': 'Abies grandis', 'common name': 'grand fir', 'characteristics': []}, 'Abies guatemalensis': {'scientific name': 'Abies guatemalensis', 'common name': 'Guatemalan fir', 'characteristics': []}, 'Abies lasiocarpa': {'scientific name': 'Abies lasiocarpa', 'common name': 'alpine fir; mountain fir', 'characteristics': []}, 'Abies magnifica': {'scientific name': 'Abies magnifica', 'common name': 'California mountain fir', 'characteristics': []}, 'Abies nordmanniana': {'scientific name': 'Abies nordmanniana', 'common name': 'Nordmann fir', 'characteristics': []}, 'Abies pinsapo': {'scientific name': 'Abies pinsapo', 'common name': 'Spanish fir', 'characteristics': []}, 'Abies procera': {'scientific name': 'Abies procera', 'common name': 'noble fir', 'characteristics': []}, 'Abies sibirica': {'scientific name': 'Abies sibirica', 'common name': 'Siberian fir; fir needle', 'characteristics': []}}}, 'Cedrus': {'species': {'Cedrus': {'scientific name': 'Cedrus', 'common name': 'true cedars', 'characteristics': []}, 'Cedrus atlantica': {'scientific name': 'Cedrus atlantica', 'common name': 'Atlas cedar', 'characteristics': []}, 'Cedrus deodara': {'scientific name': 'Cedrus deodara', 'common name': 'deodar cedar', 'characteristics': []}, 'Cedrus libani': {'scientific name': 'Cedrus libani', 'common name': 'cedar of Lebanon', 'characteristics': []}, 'Cedrus brevifolia': {'scientific name': 'Cedrus brevifolia', 'common name': 'Cyprus cedar', 'characteristics': []}}}, 'Larix': {'species': {'Larix': {'scientific name': 'Larix', 'common name': 'larches', 'characteristics': []}, 'Larix decidua': {'scientific name': 'Larix decidua', 'common name': 'European larch', 'characteristics': []}, 'Larix gmelinii': {'scientific name': 'Larix gmelinii', 'common name': 'Dahurian larch', 'characteristics': []}, 'Larix kaempferi': {'scientific name': 'Larix kaempferi', 'common name': 'Japanese larch', 'characteristics': []}, 'Larix laricina': {'scientific name': 'Larix laricina', 'common name': 'tamarack', 'characteristics': []}, 'Larix lyallii': {'scientific name': 'Larix lyallii', 'common name': 'alpine larch', 'characteristics': []}, 'Larix occidentalis': {'scientific name': 'Larix occidentalis', 'common name': 'western larch', 'characteristics': []}, 'Larix sibirica': {'scientific name': 'Larix sibirica', 'common name': 'Siberian larch', 'characteristics': []}}}, 'Picea': {'species': {'Picea': {'scientific name': 'Picea', 'common name': 'spruces', 'characteristics': []}, 'Picea abies': {'scientific name': 'Picea abies', 'common name': 'Norway spruce', 'characteristics': []}, 'Picea breweriana': {'scientific name': 'Picea breweriana', 'common name': 'Brewer spruce', 'characteristics': []}, 'Picea engelmannii': {'scientific name': 'Picea engelmannii', 'common name': 'Engelmann spruce', 'characteristics': []}, 'Picea glauca': {'scientific name': 'Picea glauca', 'common name': 'white spruce', 'characteristics': []}, 'Picea mariana': {'scientific name': 'Picea mariana', 'common name': 'black spruce', 'characteristics': []}, 'Picea omorika': {'scientific name': 'Picea omorika', 'common name': 'Serbian spruce', 'characteristics': []}, 'Picea pungens': {'scientific name': 'Picea pungens', 'common name': 'blue spruce', 'characteristics': []}, 'Picea rubens': {'scientific name': 'Picea rubens', 'common name': 'red spruce', 'characteristics': []}, 'Picea sitchensis': {'scientific name': 'Picea sitchensis', 'common name': 'Sitka spruce', 'characteristics': []}, 'Picea smithiana': {'scientific name': 'Picea smithiana', 'common name': 'Morinda spruce; West Himalayan spruce', 'characteristics': []}}}, 'Pinus': {'species': {'Pinus': {'scientific name': 'Pinus', 'common name': 'pines', 'characteristics': []}, 'Pinus albicaulis': {'scientific name': 'Pinus albicaulis', 'common name': 'whitebark pine', 'characteristics': []}, 'Pinus aristata': {'scientific name': 'Pinus aristata', 'common name': 'bristlecone pine', 'characteristics': []}, 'Pinus banksiana': {'scientific name': 'Pinus banksiana', 'common name': 'jack pine', 'characteristics': []}, 'Pinus brutia': {'scientific name': 'Pinus brutia', 'common name': 'Calabrian pine', 'characteristics': []}, 'Pinus canariensis': {'scientific name': 'Pinus canariensis', 'common name': 'Canary Island pine', 'characteristics': []}, 'Pinus cembra': {'scientific name': 'Pinus cembra', 'common name': 'Swiss stone pine', 'characteristics': []}, 'Pinus cembroides': {'scientific name': 'Pinus cembroides', 'common name': 'Mexican pinyon', 'characteristics': []}, 'Pinus contorta contorta': {'scientific name': 'Pinus contorta contorta', 'common name': 'shore pine', 'characteristics': []}, 'Pinus contorta latifolia': {'scientific name': 'Pinus contorta latifolia', 'common name': 'lodgepole pine', 'characteristics': []}, 'Pinus coulteri': {
    'scientific name': 'Pinus coulteri', 'common name': 'Coulter pine; bigcone pine', 'characteristics': []}, 'Pinus echinata': {'scientific name': 'Pinus echinata', 'common name': 'shortleaf pine', 'characteristics': []}, 'Pinus edulis': {'scientific name': 'Pinus edulis', 'common name': 'pinyon; Colorado pinyon', 'characteristics': []}, 'Pinus elliotii': {'scientific name': 'Pinus elliotii', 'common name': 'slash pine', 'characteristics': []}, 'Pinus flexilis': {'scientific name': 'Pinus flexilis', 'common name': 'limber pine', 'characteristics': []}, 'Pinus glabra': {'scientific name': 'Pinus glabra', 'common name': 'spruce pine', 'characteristics': []}, 'Pinus halepensis': {'scientific name': 'Pinus halepensis', 'common name': 'Aleppo pine', 'characteristics': []}, 'Pinus jeffreyi': {'scientific name': 'Pinus jeffreyi', 'common name': 'Jeffrey pine', 'characteristics': []}, 'Pinus lambertiana': {'scientific name': 'Pinus lambertiana', 'common name': 'sugar pine', 'characteristics': []}, 'Pinus longaeva': {'scientific name': 'Pinus longaeva', 'common name': 'ancient bristlecone pine; Methuselah pine; long-lived pine', 'characteristics': []}, 'Pinus monophylla': {'scientific name': 'Pinus monophylla', 'common name': 'single-leaf pine', 'characteristics': []}, 'Pinus monticola': {'scientific name': 'Pinus monticola', 'common name': 'western white pine', 'characteristics': []}, 'Pinus mugo': {'scientific name': 'Pinus mugo', 'common name': 'mugho pine; Swiss mountain pine', 'characteristics': []}, 'Pinus muricata': {'scientific name': 'Pinus muricata', 'common name': 'bishop pine', 'characteristics': []}, 'Pinus nigra nigra': {'scientific name': 'Pinus nigra nigra', 'common name': 'European black pine; Austrian pine', 'characteristics': []}, 'Pinus nigra salzmannii': {'scientific name': 'Pinus nigra salzmannii', 'common name': 'Cevennes black pine', 'characteristics': []}, 'Pinus nigra salzmannii var. corsicana': {'scientific name': 'Pinus nigra salzmannii var. corsicana', 'common name': 'Corsican pine', 'characteristics': []}, 'Pinus palustris': {'scientific name': 'Pinus palustris', 'common name': 'longleaf pine', 'characteristics': []}, 'Pinus patula': {'scientific name': 'Pinus patula', 'common name': 'jelecote pine', 'characteristics': []}, 'Pinus pinaster': {'scientific name': 'Pinus pinaster', 'common name': 'maritime pine', 'characteristics': []}, 'Pinus pinea': {'scientific name': 'Pinus pinea', 'common name': 'European stone pine', 'characteristics': []}, 'Pinus ponderosa': {'scientific name': 'Pinus ponderosa', 'common name': 'ponderosa pine', 'characteristics': []}, 'Pinus pungens': {'scientific name': 'Pinus pungens', 'common name': 'table mountain pine', 'characteristics': []}, 'Pinus quadrifolia': {'scientific name': 'Pinus quadrifolia', 'common name': 'Parry pinyon', 'characteristics': []}, 'Pinus radiata': {'scientific name': 'Pinus radiata', 'common name': 'Monterey pine', 'characteristics': []}, 'Pinus resinosa': {'scientific name': 'Pinus resinosa', 'common name': 'red pine', 'characteristics': []}, 'Pinus rigida': {'scientific name': 'Pinus rigida', 'common name': 'pitch pine', 'characteristics': []}, 'Pinus sabiniana': {'scientific name': 'Pinus sabiniana', 'common name': 'gray pine', 'characteristics': []}, 'Pinus serotina': {'scientific name': 'Pinus serotina', 'common name': 'pond pine; swamp pine', 'characteristics': []}, 'Pinus strobiformis': {'scientific name': 'Pinus strobiformis', 'common name': 'southwestern white pine', 'characteristics': []}, 'Pinus strobus': {'scientific name': 'Pinus strobus', 'common name': 'eastern white pine', 'characteristics': []}, 'Pinus sylvestris': {'scientific name': 'Pinus sylvestris', 'common name': 'Scots pine; Scotch pine', 'characteristics': []}, 'Pinus taeda': {'scientific name': 'Pinus taeda', 'common name': 'loblolly pine', 'characteristics': []}, 'Pinus torreyana': {'scientific name': 'Pinus torreyana', 'common name': 'Torrey pine', 'characteristics': []}, 'Pinus virginiana': {'scientific name': 'Pinus virginiana', 'common name': 'Virginia pine', 'characteristics': []}, 'Pinus wallichiana': {'scientific name': 'Pinus wallichiana', 'common name': 'blue pine; Bhutan pine; Himalayan pine', 'characteristics': []}}}, 'Pseudotsuga': {'species': {'Pseudotsuga': {'scientific name': 'Pseudotsuga', 'common name': 'Douglas firs', 'characteristics': []}, 'Pseudotsuga macrocarpa': {'scientific name': 'Pseudotsuga macrocarpa', 'common name': 'bigcone Douglas fir', 'characteristics': []}, 'Pseudotsuga menziesii': {'scientific name': 'Pseudotsuga menziesii', 'common name': 'Douglas fir', 'characteristics': []}, 'Pseudotsuga menziesii glabra': {'scientific name': 'Pseudotsuga menziesii glabra', 'common name': 'blue Douglas fir', 'characteristics': []}}}, 'Tsuga': {'species': {'Tsuga': {'scientific name': 'Tsuga', 'common name': 'hemlocks', 'characteristics': []}, 'Tsuga canadensis': {'scientific name': 'Tsuga canadensis', 'common name': 'eastern hemlock; Canadian hemlock', 'characteristics': []}, 'Tsuga caroliniana': {'scientific name': 'Tsuga caroliniana', 'common name': 'Carolina hemlock', 'characteristics': []}, 'Tsuga heterophylla': {'scientific name': 'Tsuga heterophylla', 'common name': 'western hemlock', 'characteristics': []}, 'Tsuga mertensiana': {'scientific name': 'Tsuga mertensiana', 'common name': 'mountain hemlock', 'characteristics': []}}}}


# TODO add pinus thunbergi / clausa to above dict
STOUT = 'stout'
THIN = 'thin'
LACKING = 'lacking'
THIN_LACKING = 'thin to lacking'
ROUND = 'round'
NORTH = 'Northern states'
MIDDLE = 'Middle states'
SOUTH = 'south'
NORTH_MIDDLE = 'northern and middle states'
BOTH = 'Both'
MIDDLE_SOUTH = 'middle and southern states'

North_American_Pines = {
    'Pinus strobus': PINACEAE['Pinus']['species']['Pinus strobus'],
    'Pinus rigida': PINACEAE['Pinus']['species']['Pinus rigida'],
    'Pinus serotina': PINACEAE['Pinus']['species']['Pinus serotina'],
    'Pinus taeda': PINACEAE['Pinus']['species']['Pinus taeda'],
    'Pinus palustris': PINACEAE['Pinus']['species']['Pinus palustris'],
    'Pinus banksiana': PINACEAE['Pinus']['species']['Pinus banksiana'],
    'Pinus sylvestris': PINACEAE['Pinus']['species']['Pinus sylvestris'],
    'Pinus nigra nigra': PINACEAE['Pinus']['species']['Pinus nigra nigra'],
    'Pinus resinosa': PINACEAE['Pinus']['species']['Pinus resinosa'],
    'Pinus pungens': PINACEAE['Pinus']['species']['Pinus pungens'],
    'Pinus virginiana': PINACEAE['Pinus']['species']['Pinus virginiana'],
    'Pinus echinata': PINACEAE['Pinus']['species']['Pinus echinata'],
    'Pinus glabra': PINACEAE['Pinus']['species']['Pinus glabra'],
    # 'Pinus clausa'  : PINACEAE['Pinus']['species']['Pinus clausa'],
    'Pinus elliotii': PINACEAE['Pinus']['species']['Pinus elliotii'],
}


species_extended_info = {
    'Pinus rigida': {
        # ['Needles thin, conese slim, branches parallel']
        'dist': NORTH_MIDDLE,
        'needles per cluster': '3',
        'needle length': '2-4',
        'trunk sprouts after fire': True,
        'many old cones on tree': True,
        'cones longer than three inches': False,
        'cones longer than wide': ROUND,
        'cone prickle type': STOUT,
        'short description': '',
        'full description': ''
    },
    'Pinus strobus': {
        'dist': NORTH_MIDDLE,
        'needles per cluster': '3',
        'needle length': '3-6',
        'trunk sprouts after fire': False,
        'many old cones on tree': False,
        'cones longer than three inches': True,
        'cones longer than wide': True,
        'cone prickle type': LACKING,
        'short description': '',
        'full description': ''
    },
    'Pinus serotina': {
        'dist': SOUTH,
        'needles per cluster': '3',
        'needle length': '4-8',
        'trunk sprouts after fire': True,
        'many old cones on tree': True,
        'cones longer than three inches': False,
        'cones longer than wide': ROUND,
        'cone prickle type': THIN_LACKING,
        'short description': '',
        'full description': ''
    },
    'Pinus taeda': {
        'dist': SOUTH,
        'needles per cluster': '3',
        'needle length': '6-9',
        'trunk sprouts after fire': False,
        'many old cones on tree': True,
        'cones longer than three inches': True,
        'cones longer than wide': True,
        'cone prickle type': STOUT,
        'short description': '',
        'full description': ''
    },
    'Pinus palustris': {
        'dist': SOUTH,
        'needles per cluster': '3',
        'needle length': '8-18',
        'trunk sprouts after fire': False,
        'many old cones on tree': False,
        'cones longer than three inches': True,
        'cones longer than wide': True,
        'cone prickle type': THIN,
        'short description': '',
        'full description': ''
    },
    'Pinus banksiana': {
        'dist': NORTH,
        'needle length': '2-4',
        'needles per cluster': '2',
        'trunk sprouts after fire': None,
        'twigs rough near needle': True,
        'many old cones on tree': True,
        'cones longer than three inches': False,
        'cones longer than wide': True,
        'cone prickle type': THIN_LACKING,
        'short description': '',
        'full description': ''
    },
    'Pinus sylvestris': {
        'dist': NORTH,
        'needle length': '2-3',
        'needles per cluster': '2',
        'twigs rough near needle': False,
        'trunk sprouts after fire': None,
        'many old cones on tree': False,
        'cones longer than three inches': False,
        'cones longer than wide': ROUND,
        'cone prickle type': LACKING,
        'short description': '',
        'full description': ''
    },
    'Pinus nigra nigra': {
        'dist': NORTH,
        'needle length': '3-6',
        'needles per cluster': '2',
        'twigs rough near needle': True,
        'trunk sprouts after fire': None,
        'many old cones on tree': False,
        'cones longer than three inches': BOTH,
        'cones longer than wide': True,
        'cone prickle type': STOUT,
        'short description': '',
        'full description': ''
    },
    'Pinus resinosa': {
        'dist': NORTH,
        'needle length': '4-6',
        'needles per cluster': '2',
        'twigs rough near needle': BOTH,
        'trunk sprouts after fire': None,
        'many old cones on tree': False,
        'cones longer than three inches': False,
        'cones longer than wide': True,
        'cone prickle type': LACKING,
        'short description': '',
        'full description': ''
    },

    'Pinus pungens': {
        'dist': MIDDLE,
        'needle length': '2-3',
        'needles per cluster': '2',
        'twigs rough near needle': True,
        'trunk sprouts after fire': None,
        'many old cones on tree': True,
        'cones longer than three inches': BOTH,
        'cones longer than wide': ROUND,
        'cone prickle type': STOUT,
        'short description': '',
        'full description': ''
    },
    'Pinus virginiana': {
        'dist': MIDDLE,
        'needle length': '2-3',
        'needles per cluster': '2',
        'twigs rough near needle': False,
        'trunk sprouts after fire': None,
        'many old cones on tree': True,
        'cones longer than three inches': False,
        'cones longer than wide': BOTH,
        'cone prickle type': THIN,
        'short description': '',
        'full description': ''
    },
    'Pinus echinata': {
        'dist': MIDDLE_SOUTH,
        'needle length': '3-5',
        'needles per cluster': '2',
        'twigs rough near needle': True,
        'many old cones on tree': True,
        'trunk sprouts after fire': None,
        'cones longer than three inches': False,
        'cones longer than wide': True,
        'cone prickle type': THIN,
        'short description': '',
        'full description': ''
    },
    'Pinus glabra': {
        'dist': SOUTH,
        'needle length': '2-4',
        'needles per cluster': '2',
        'twigs rough near needle': False,
        'many old cones on tree': True,
        'trunk sprouts after fire': None,
        'cones longer than three inches': False,
        'cones longer than wide': True,
        'cone prickle type': THIN_LACKING,
        'short description': '',
        'full description': ''
    },
    'Pinus elliotii': {
        'dist': SOUTH,
        'needle length': '5-11',
        'needles per cluster': '2',
        'twigs rough near needle': True,
        'many old cones on tree': False,
        'cones longer than three inches': True,
        'cones longer than wide': True,
        'cone prickle type': STOUT,
        'trunk sprouts after fire': None,
        'short description': '',
        'full description': ''
    }
}


def addCharacteristicsToSpecies(species_dict, characteristics):
    """it adds data to characteristics key"""
    species_main = species_dict.keys()
    species_chars = characteristics.keys()
    # print(species_main, species_chars)
    for species in species_main:
        for chars in species_chars:
            if species == chars:
                species_dict[species]['characteristics'] = characteristics[chars]
    return species_dict


addCharacteristicsToSpecies(North_American_Pines,  species_extended_info)


needle_length = 'needle length'
distribution = 'dist'
needle_count = 'needles per cluster'
fire_resislience = 'trunk sprouts after fire'
twig_texture = 'twigs rough near needle'
old_cones = 'many old cones on tree'
cone_length = 'cones longer than three inches'
cone_shape = 'cones longer than wide'
cone_prickles = 'cone prickle type'
short_desc = 'short description'
long_desc = 'full description'


class PinusSpecies:
    kind = 'Pinus'

    def __init__(self, species):
        self.species = species
        self.common_name = ''
        self.scientific_name = ''
        self.characteristics = {}

    def define_common_name(self, name):
        self.common_name = name

    def define_scientific_name(self, name):
        self.scientific_name = name

    def define_characteristics(self, characteristics):
        for key, value in characteristics.items():
            self.characteristics[key] = value

    def display_characteristics(self):
        print('The tree your entries keyed out is ' +
              '\n\n' + self.scientific_name + '\n')
        print('Its common name is ' + self.common_name)
        print('The distribution of this tree is ' +
              self.characteristics[distribution])
        print('There are '+self.characteristics[needle_count] +
              ' needles per cluster and the needle length is ' + self.characteristics[needle_length]+' inches.')
        if self.characteristics[cone_length] == True:
            print('Cones are longer than three inches')
        if self.characteristics[cone_length] == False:
            print('Cones are shorter than three inches')
        if self.characteristics[cone_length] == BOTH:
            print('Cones can be larger or smaller than three inches')
        if self.characteristics[cone_shape] == True:
            print('Cones are longer than they are wide')
        if self.characteristics[cone_shape] == False:
            print('cones are wider than they are long')
        if self.characteristics[cone_shape] == ROUND:
            print('Cones are fairly round in shape')
        if self.characteristics[cone_prickles] == STOUT:
            print('The cones have stout prickles')
        if self.characteristics[cone_prickles] == THIN:
            print('The cones have thin prickles')
        if self.characteristics[cone_prickles] == THIN_LACKING:
            print('The cones range thin prickles to lacking prickles')
        if self.characteristics[cone_prickles] == LACKING:
            print('The cones lack prickles')
        if self.characteristics[old_cones] == True:
            print('There may be many old cones on the tree')
        else:
            print('old cones do not persist on the tree')
        if self.characteristics.get(twig_texture) != None:
            if self.characteristics[twig_texture] == True:
                print('Twigs are textured or rough near the needle attachment')
            else:
                print('Twigs lack texture or are smooth near needle attachment')
        if self.characteristics[fire_resislience] == True:
            print('The trunk may sprout again after a fire')
        if self.characteristics[fire_resislience] == False:
            print('This species is not known to sprout again after fire damage')
# 'short description'
# TODO 'full description'


def buildClassDictionary(data_object, empty_di):
    """builds dictionary of classes with pre built data object"""
    for key, value in data_object.items():
        new_species = value
        species_name = key
        species_name = PinusSpecies(new_species['scientific name'])
        species_name.define_common_name(new_species['common name'])
        species_name.define_scientific_name(new_species['scientific name'])
        species_name.define_characteristics(new_species['characteristics'])
        empty_di[key] = species_name
    built_di = empty_di
    return built_di


Pinus_Class_Dictionary = {}
buildClassDictionary(North_American_Pines, Pinus_Class_Dictionary)

# print(Pinus_Class_Dictionary['Pinus nigra nigra'].display_characteristics())

a = 'a'
b = 'b'
c = 'c'
choose_a = 'choose_a'
choose_b = 'choose_b'
choose_c = 'choose_c'
parent = 'parent'
current = 'current'


pinus_binary_location = {
    11: {
        a: '2 neeedles per cluster (if mix of two and three pick this)',
        b: 'more than two needles per cluster',
        choose_a: 21,
        choose_b: 22,
        parent: 'HEAD',
        current: 11
    },
    21: {
        a: 'cone prickles stout, all or some cones larger than 3 inches',
        b: ' cones smaller three inches, cone prickles thin or lacking ',
        choose_a: 31,
        choose_b: 32,
        parent: 11,
        current: 21

    },
    31: {
        a: 'cones longer than wide',  # elliotii
        b: 'cones wider than long or round on average',
        choose_a: 'Pinus elliotii',
        choose_b: 41,
        parent: 21,
        current: 31
    },
    41: {
        a: 'many old cones on tree',  # pungens
        b: ' not many old cones on tree',  # nigra
        choose_a: 'Pinus pungens',
        choose_b: 'Pinus nigra nigra',
        parent: 31,
        current: 41
    },
    32: {
        a: 'twigs rough near needles',
        b: ' twigs more smooth near needles',
        choose_a: 42,
        choose_b: 43,
        parent: 21,
        current: 32
    },
    42: {
        a: 'needles very short 1.5 -2 inches',  # banksiana
        b: 'needles 3-5 inches',  # echinata
        choose_a: 'Pinus banksiana',
        choose_b: 'Pinus echinata',
        parent: 32,
        current: 42
    },
    43: {
        a: 'many old cones on tree',
        b: 'not many old cones on tree',
        choose_a: 51,
        choose_b: 52,
        parent: 32,
        current: 43
    },
    51: {
        a: 'middle states,branches very fiberous, tough to break',  # virginiana
        b: 'southern state, broad leaf forest',  # glabra
        choose_a: 'Pinus virginiana',
        choose_b: 'Pinus glabra',
        parent: 43,
        current: 51
    },
    52: {
        a: 'tree needles 2-3 inches long',  # sylvestris
        b: 'tree needles 4-6 inches long',  # resinosa
        choose_a: 'Pinus sylvestris',
        choose_b: 'Pinus resinosa',
        parent: 43,
        current: 52
    },
    22: {
        a: 'Needles in bundles of 5',  # strobis
        b: 'Needles in bundles of 3-4',
        c: 'Needles in bundles of more than 5',
        choose_a: 'Pinus strobus',
        choose_b: 33,
        choose_c: 'uhoh',  # TODO point this backwards
        parent: 11,
        current: 22
    },
    33: {
        a: 'cones more than three inches long',
        b: 'cones less than three inches long',
        choose_a: 44,
        choose_b: 45,
        parent: 22,
        current: 33
    },
    44: {
        a: 'needles 6-9 inches long, end buds brown',  # taeda
        b: 'needles 8-18 inches long, end buds white',  # paulustis
        choose_a: 'Pinus taeda',
        choose_b: 'Pinus palustris',
        parent: 33,
        current: 44
    },
    45: {
        a: 'cone prickles stout, located in northern or middle states',  # rigida
        b: 'cone prickles this or absent, located southern states',  # serotina
        choose_a: 'Pinus rigida',
        choose_b: 'Pinus serotina',
        parent: 33,
        current: 45
    }
}


# 'Pinus clausa
# {'dist': SOUTH,
#  'needle length': 2-4,
#  'twigs rough near needle': False,
#  'many old cones on tree': True,
#  'cones longer than three inches': False,
#  'cones longer than wide': ROUND,
#  'cone prickle type': STOUT
#  }
