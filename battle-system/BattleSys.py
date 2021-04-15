# file: BattleSys.py
# author: colin seifer
# description: handles battles on the backend.

from ..src import Observation
import BattleCalc
import threading
import random

# constants
NUM_OBS = 6 # number of observations
MAX_TURN = 15 # max allowed number of turns
RAND_MAX = 64 # arbitrary value to determine switch
HP_STAT = 0
ATK_STAT = 1
DEF_STAT = 2
ACC_STAT = 3
EVA_STAT = 4
SPD_STAT = 5

# possible move effects
effect_dict = {
    "flavor_text",
    "priority",
    "bp",
    "acc",
    "hp_mod",
    "atk_mod",
    "def_mod",
    "acc_mod",
    "eva_mod",
    "spd_mod",
    "team_hp_mod",
    "team_atk_mod",
    "team_def_mod",
    "team_acc_mod",
    "team_eva_mod",
    "team_spd_mod",
    "opp_hp_mod",
    "opp_atk_mod",
    "opp_def_mod",
    "opp_acc_mod",
    "opp_eva_mod",
    "opp_spd_mod",
    "miss_rate",
    "user_dmg",
	"opp_dmg",
    "reduce_dmg",
    "opp_dot",
    "free_switch",
    "next_sure_hit",
    "force_switch",
    "heal_ot",
    "next_atk_lock",
    "ignore_def",
    "sure_hit",
    "rand_move",
    "next_reduce_dmg",
    "no_retreat",
    "team_heal",
    "require_opp_contact",
    "opp_move_lock",
    "ko_type",
    "use_opp_atk",
    "revive_with_hp",
    "reduce_dmg_type",
    "single_move",
    "opp_single_move",
    "learn_opp_move",
	"require_move",
    "require_priority",
	"require_first_turn"
}

class Battle:
    def __init__(self, obs = []):
        self.observations = []
        self.observations.append(obs)
        self.turn = 0
        self.p1_move
        self.p2_move
        self.p1_active_obs = 0
        self.p2_active_obs = 3
        self.p1_move_prev
        self.p2_move_prev
        self.move_choice = 0
        self.switch = -1

    # handles first player's turn
    def PlayerTurn(self):
        # wait for user to select a move
        threading.Event.wait(self.move_choice > 0 or self.switch >= 0)

        # update p1_active_obs
        if(self.observations.count = NUM_OBS and self.switch >= 0):
            self.p1_active_obs = self.switch

        # call user selected move
        if(self.observations.count = NUM_OBS and self.move_choice > 0):
            self.p1_move = self.observations[self.p1_active_obs].moves[self.move_choice - 1]

        # reset choices
        self.move_choice = 0
        self.switch = -1

    # handles second player (or AI turn)
    # TODO give AI sensible choices based on opponent
    def OpponentTurn(self, ai):
        if(not ai):
            # wait for opponent to select move
            threading.Event.wait(self.move_choice > 0 or self.switch >= 0)
            if(self.observations.count = NUM_OBS and self.switch >= 0):
                self.p2_active_obs = self.switch
        else:
            # switch on random value
            res = random.randrange(3, RAND_MAX)
            if(res < NUM_OBS and res != self.p2_active_obs):
                self.p2_active_obs = res
            # otherwise, choose a move for current observation
            else:
                self.move_choice = random.randrange(4)

        # call opponent selected move
        if(self.observations.count = NUM_OBS and self.move_choice > 0):
            self.p2_move = self.observations[self.p2_active_obs].moves[self.move_choice - 1]

    # get player priority
    def Priority(self):
        if(self.p1_move.get("priority") == self.p2_move.get("priority")):
            # choose by speed
            if(BattleCalc.Speed(self.observations[self.p1_active_obs].stats[SPD_STAT]\
                , self.observations[self.p1_active_obs].stat_mod[SPD_STAT]\
                , self.observations[self.p2_active_obs].stats[SPD_STAT]\
                , self.observations[self.p2_active_obs].stat_mod[SPD_STAT] > 0)):
                # player1 has priority
                return 0
            elif(BattleCalc.Speed(self.observations[self.p1_active_obs].stats[SPD_STAT]\
                , self.observations[self.p1_active_obs].stat_mod[SPD_STAT]\
                , self.observations[self.p2_active_obs].stats[SPD_STAT]\
                , self.observations[self.p2_active_obs].stat_mod[SPD_STAT] < 0)):
                # player2 has priority
                return 1
            else:
                # choose randomly
                return random.randrange(2)
        elif(self.p1_move.get("priority") > self.p2_move.get("priority")):
            # player1 has priority
            return 0
        else:
            # player2 has priority
            return 1

    def PlayerSwitch(self):
        # if player has a remaining observation left
        if(self.observations[0].stats[HP_STAT] > 0 or self.observations[1].stats[HP_STAT] > 0\
            or self.observations[2].stats[HP_STAT] > 0):
            # wait for user to select a move
            threading.Event.wait(self.switch >= 0 and self.observations[switch].stats[HP_STAT] > 0)
        else:
            return

        # update p1_active_obs
        if(self.observations.count = NUM_OBS and self.switch >= 0):
            self.p1_active_obs = self.switch

        # reset value
        self.switch = -1

    def OpponentSwitch(self, ai):
        # if opponent is not ai and has an observation left
        if(not ai and (self.observations[3].stats[HP_STAT] > 0 or self.observations[4].stats[HP_STAT] > 0\
            or self.observations[5].stats[HP_STAT] > 0)):
            # wait for opponent to select a move
            threading.Event.wait(self.switch >= 0 and self.observations[switch].stats[HP_STAT] > 0)
        # select new observation at random if ai has an observation left
        elif(self.observations[3].stats[HP_STAT] > 0 or self.observations[4].stats[HP_STAT] > 0\
            or self.observations[5].stats[HP_STAT] > 0):
            res = random.randrange(3, NUM_OBS)
            # keep rolling until we get an observation with HP left
            while(self.observations[res].stats[HP_STAT] <= 0):
                res = random.randrange(3, NUM_OBS)
            
            # update switch
            self.switch = res
        else:
            return

        # update p1_active_obs
        if(self.observations.count = NUM_OBS and self.switch >= 0):
            self.p2_active_obs = self.switch

        # reset value
        self.switch = -1

    def Attack(self, ai):
        # check priority
        if(self.Priority() == 0):
            # player1 moves first
            # TODO handle battle effects
            if(self.p1_move.get("sure_hit") != None):
                # if move is damaging
                if(self.p1_move.get("bp") != None):
                    # calculate damage
                    self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                        self.observations[self.p1_active_obs].stats[ATK_STAT]\
                        , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                        , self.p1_move.get("bp"))
            # if not sure hit, get whether move hits
            elif(self.p1_move.get("acc") != None and BattleCalc.Hit(self.p1_move.get("acc")\
                , self.observations[self.p1_active_obs].stats[ACC_STAT]\
                , self.observations[self.p2_active_obs].stats[EVA_STAT])):
                # if move hits, calculate damage
                self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                    self.observations[self.p1_active_obs].stats[ATK_STAT]\
                    , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                    , self.p1_move.get("bp"))

            # check to see if opponent was knocked out
            if(self.observations[self.p2_active_obs].stats[HP_STAT] > 0):
                if(self.p2_move.get("sure_hit") != None):
                    # if move is damaging
                    if(self.p2_move.get("bp") != None):
                        # calculate damage
                        self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                            self.observations[self.p2_active_obs].stats[ATK_STAT]\
                            , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                            , self.p2_move.get("bp"))
                # if not sure hit, get whether move hits
                elif(self.p2_move.get("acc") != None and BattleCalc.Hit(self.p2_move.get("acc")\
                    , self.observations[self.p2_active_obs].stats[ACC_STAT]\
                    , self.observations[self.p1_active_obs].stats[EVA_STAT])):
                    # if move hits, calculate damage
                    self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                        self.observations[self.p2_active_obs].stats[ATK_STAT]\
                        , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                        , self.p2_move.get("bp"))
                
                # check to see if player was knocked out
                if(self.observations[self.p2_active_obs].stats[HP_STAT] <= 0):
                    self.PlayerSwitch()
            else:
                self.OpponentSwitch(ai)
        else:
            # player2 moves first
            # TODO handle battle effects
            if(self.p2_move.get("sure_hit") != None):
                # if move is damaging
                if(self.p2_move.get("bp") != None):
                    # calculate damage
                    self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                        self.observations[self.p2_active_obs].stats[ATK_STAT]\
                        , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                        , self.p2_move.get("bp"))
            # if not sure hit, get whether move hits
            elif(self.p2_move.get("acc") != None and BattleCalc.Hit(self.p2_move.get("acc")\
                , self.observations[self.p2_active_obs].stats[ACC_STAT]\
                , self.observations[self.p1_active_obs].stats[EVA_STAT])):
                # if move hits, calculate damage
                self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                    self.observations[self.p2_active_obs].stats[ATK_STAT]\
                    , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                    , self.p2_move.get("bp"))

            # check to see if player was knocked out
            if(self.observations[self.p1_active_obs].stats[HP_STAT] > 0):
                if(self.p1_move.get("sure_hit") != None):
                    # if move is damaging
                    if(self.p1_move.get("bp") != None):
                        # calculate damage
                        self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                            self.observations[self.p1_active_obs].stats[ATK_STAT]\
                            , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                            , self.p1_move.get("bp"))
                # if not sure hit, get whether move hits
                elif(self.p1_move.get("acc") != None and BattleCalc.Hit(self.p1_move.get("acc")\
                    , self.observations[self.p1_active_obs].stats[ACC_STAT]\
                    , self.observations[self.p2_active_obs].stats[EVA_STAT])):
                    # if move hits, calculate damage
                    self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                        self.observations[self.p1_active_obs].stats[ATK_STAT]\
                        , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                        , self.p1_move.get("bp"))
                
                # check to see if opponent was knocked out
                if(self.observations[self.p2_active_obs].stats[HP_STAT] <= 0):
                    self.OpponentSwitch(ai)
            else:
                self.PlayerSwitch()

        # set current move as previous move
        self.p1_move_prev = self.p1_move
        self.p2_move_prev = self.p2_move

    # handles one observation attacking another
    def BattleLoop(self, ai = False):
        # continue until max turns
        while(self.turn <= MAX_TURN):
            # update turn counter
            self.turn += 1

            # take player turns
            self.PlayerTurn()
            self.OpponentTurn(ai)
            self.Attack(ai)

            # check for winner
            # check hp of each observation
            if(self.observations.count() == NUM_OBS and self.observations[0].stats[0] == 0\
                and self.observations[1].stats[0] == 0 and self.observations[2].stats[0] == 0):
                # returns 1 for player 2 win
                return 1

            elif(self.observations.count() == NUM_OBS and self.observations[3].stats[0] == 0\
                and self.observations[4].stats[0] == 0 and self.observations[5].stats[0] == 0):
                # returns 0 for player 1 win
                return 0

        # if max turns are reached, both players lose
        # return 1 for player 2 win
        # since both players are player 1 from their perspective, this is a loss for both
        return 1