# file: TypeAssign.py
# author: colin seifer, Danielle Dishop
# description: assigns type and stat modifiers

# create static dict to keep track of taxa
# keys correspond to iNat taxon ID
TAXA_DICT = {
    47158: 'Insecta',
    26036: 'Reptilia',
    48222: 'Chromista',
    47178: 'Actinopterygii',
    40151: 'Mammalia',
    47170: 'Fungi',
    20978: 'Amphibia',
    47119: 'Arachnida',
    3: 'Aves',
    1: 'Animalia',
    47115: 'Mollusca',
    47126: 'Plantae',
    47686: 'Protozoa'
}

# sort by taxon ID and ancestor IDs
class Type:

    # initialize object with taxa ID list
    def __init__(self, taxon_id, ancestor_ids = []):
        self.ancestor_ids = []
        self.ancestor_ids.append(taxon_id)
        self.ancestor_ids.extend(ancestor_ids)

    # assign type
    def AssignType(self):
        # check taxa list for match with taxa dict
        for id in self.ancestor_ids:
            if(TAXA_DICT.get(id) != None):
                return TAXA_DICT.get(id)

        # otherwise, return -1 for error
        return -1