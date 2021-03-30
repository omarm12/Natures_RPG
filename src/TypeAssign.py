# file: TypeAssign.py
# author: colin seifer
# description: assigns type and stat modifiers

# sort by taxon ID and ancestor IDs
class Type:

    # create static dict to keep track of taxa
    # keys correspond to iNat taxon ID
    taxa_dict = {
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

    # initialize object with taxa ID list
    def __init__(self, taxon_id, ancestor_ids = []):
        self.ancestor_ids = []
        self.ancestor_ids.append(taxon_id)
        self.ancestor_ids.extend(ancestor_ids)

    # assign type
    def AssignType():
        # check taxa list for match with taxa dict
        for id in self.ancestor_ids:
            if(taxa_dict.get(id) != None):
                return taxa_dict.get(id)

        # otherwise, return -1 for error
        return -1