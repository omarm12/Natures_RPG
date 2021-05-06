# file: Observation.py
# author: colin seifer
# description: holds observation data.

from ..Utils import TypeAssign
from ..Utils import StatsAssign
from . import Moves

class LoadObservation:
    def __init__(self, obs_id, observation_type, move_names = [], stats = []):
        self.obs_id = obs_id
        self.observation_type = observation_type
        self.move_names = []
        self.move_names.extend(move_names)
        self.stats = []
        self.base_stats = []
        self.moves = []
        self.stats.extend(stats)
        self.base_stats.extend(stats)
        self.PopulateMoves()
        self.stat_mod = [0., 0., 0., 0., 0., 0.]
        self.dot = 0
        self.heal_ot = 0
        self.revive = 0
        self.retreat = 1

    # populate list of moves
    def PopulateMoves(self):
        move_obj = Moves.Moves()
        # for each move name, add the corresponding move
        for move in self.move_names:
            ret = move_obj.RetMove(move)
            if(ret != None):
                self.moves.append(ret)