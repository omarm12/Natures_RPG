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

    def update(self, move_names, stats, base_stats, stat_mod, dot, heal_ot, revive, retreat):
        self.move_names = move_names
        self.stats = stats
        self.base_stats = base_stats
        self.moves = []
        self.PopulateMoves()
        self.stat_mod = stat_mod
        self.dot = dot
        self.heal_ot = heal_ot
        self.revive = revive
        self.retreat = retreat

    # populate list of moves
    def PopulateMoves(self):
        move_obj = Moves.Moves()
        # for each move name, add the corresponding move
        for move in self.move_names:
            ret = move_obj.RetMove(move)
            if(ret != None):
                self.moves.append(ret)