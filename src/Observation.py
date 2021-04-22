# file: Observation.py
# author: colin seifer
# description: holds observation data.

from . import TypeAssign
from . import StatsAssign
from . import Moves

class Observation:
    def __init__(self, observation_type, move_names = [], stats = []):
        self.observation_type = observation_type
        self.move_names = []
        self.move_names.extend(move_names)
        self.stats = []
        self.moves = []
        self.stats.extend(stats)
        self.PopulateMoves()
        self.stat_mod = [0, 0, 0, 0, 0, 0]

    # populate list of moves
    def PopulateMoves(self):
        move_obj = Moves.Moves()
        # for each move name, add the corresponding move
        for move in self.move_names:
            ret = move_obj.RetMove(move)
            if(ret != None):
                self.moves.append(ret)