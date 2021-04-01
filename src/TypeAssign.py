# file: TypeAssign.py
# author: colin seifer
# description: assigns type and stat modifiers

# sort by taxon ID and ancestor IDs
class Type:

    # create static dict to keep track of taxa
    # keys correspond to iNat taxon ID
    class_dict = {
        47158: 'Insecta',
        26036: 'Reptilia',
        47178: 'Actinopterygii',
        40151: 'Mammalia',
        20978: 'Amphibia',
        47119: 'Arachnida',
        3: 'Aves'
    }

    phyla_dict = {
        47115: 'Mollusca'
    }

    kingdom_dict = {
        48222: 'Chromista',
        1: 'Animalia',
        47126: 'Plantae',
        47170: 'Fungi',
        47686: 'Protozoa'
    }

    # initialize object with taxa ID list
    def __init__(self, taxon_id, ancestor_ids = []):
        self.ancestor_ids = []
        self.ancestor_ids.append(taxon_id)
        self.ancestor_ids.extend(ancestor_ids)

    # assign type
    def AssignType():
        # check taxa list for match with taxa dict
        for id in self.ancestor_ids:
            if(class_dict.get(id) != None):
                return class_dict.get(id)

        for id in self.ancestor_ids:
            if(phyla_dict.get(id) != None):
                return phyla_dict.get(id)

        for id in self.ancestor_ids:
            if(kingdom_dict.get(id) != None):
                return kingdom_dict.get(id)

        # otherwise, return undefined
        return 'Undefined'