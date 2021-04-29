# file: BattleSys.py
# author: colin seifer
# description: handles battles on the backend.

from . import LoadObservation
from . import BattleCalc
import time
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
PERCENT = 100 # multiply by 100 to get percent

class Battle:
    def __init__(self, obs = []):
        self.observations = []
        self.observations.extend(obs)
        self.turn = 0
        self.p1_move = None
        self.p2_move = None
        self.p1_active_obs = 0
        self.p2_active_obs = 3
        self.p1_move_prev = None
        self.p2_move_prev = None
        self.move_choice = 0
        self.switch = -1

    # move index should be in range 1-4
    def GetFlavorText(self, move_index):
        if(move_index >= 1 and move_index <= 4):
            return self.observations[self.p1_active_obs].moves[move_index - 1].get("flavor_text")

    # move index should be in range 1-4
    def GetBP(self, move_index):
        if(move_index >= 1 and move_index <= 4):
            return self.observations[self.p1_active_obs].moves[move_index - 1].get("bp")

    # move index should be in range 1-4
    def GetACC(self, move_index):
        if(move_index >= 1 and move_index <= 4):
            return self.observations[self.p1_active_obs].moves[move_index - 1].get("acc")

    # switch should be in range 0-5
    def SetSwitch(self, switch):
        if(switch >= 0 and switch <= 5):
            self.switch = switch
    
    # move index should be in range 1-4
    def SetMoveChoice(self, move_index):
        if(move_index >= 1 and move_index <= 4):
            self.move_choice = move_index

    # handles first player's turn
    # assumes move choice and switch are valid values
    def PlayerTurn(self):
        # wait for user to select a move
        while(not (self.move_choice > 0 or (self.switch >= 0 \
            and self.observations[self.switch].stats[HP_STAT] > 0))):
            time.sleep(0.1)

        # update p1_active_obs
        if(len(self.observations) == NUM_OBS and self.switch >= 0):
            self.p1_active_obs = self.switch

        # call user selected move
        if(len(self.observations) == NUM_OBS and self.move_choice > 0):
            self.p1_move = self.observations[self.p1_active_obs].moves[self.move_choice - 1]

        # reset choices
        self.move_choice = 0
        self.switch = -1

    # handles second player (or AI turn)
    # assumes move choice and switch are valid values
    # TODO give AI sensible choices based on opponent
    def OpponentTurn(self, ai):
        if(not ai):
            # wait for opponent to select move
            while(not (self.move_choice > 0 or (self.switch >= 0 \
                and self.observations[self.switch].stats[HP_STAT] > 0))):
                time.sleep(0.1)
            if(len(self.observations) == NUM_OBS and self.switch >= 0):
                self.p2_active_obs = self.switch
        else:
            # switch on random value
            res = random.randrange(3, RAND_MAX)
            if(res < NUM_OBS and res != self.p2_active_obs \
                and self.observations[self.switch].stats[HP_STAT] > 0):
                self.p2_active_obs = res
            # otherwise, choose a move for current observation
            else:
                self.move_choice = random.randrange(4)

        # call opponent selected move
        if(len(self.observations) == NUM_OBS and self.move_choice > 0):
            self.p2_move = self.observations[self.p2_active_obs].moves[self.move_choice - 1]

        # reset choices
        self.move_choice = 0
        self.switch = -1

    # get player priority
    def Priority(self):
        if(self.p1_move != None and self.p2_move != None and self.p1_move.get("priority") == self.p2_move.get("priority")):
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
        elif(self.p1_move != None and self.p2_move != None and self.p1_move.get("priority") > self.p2_move.get("priority")):
            # player1 has priority
            return 0
        else:
            # player2 has priority
            return 1

    # player switch after knock out
    # assumes switch is valid value
    def PlayerSwitch(self):
        # if player has a remaining observation left
        if(self.observations[0].stats[HP_STAT] > 0 or self.observations[1].stats[HP_STAT] > 0\
            or self.observations[2].stats[HP_STAT] > 0):
            # wait for user to select an observation
            while(not (self.switch >= 0 and self.observations[self.switch].stats[HP_STAT] > 0)):
                time.sleep(0.1)
        else:
            self.switch = -1
            return

        # update p1_active_obs
        if(len(self.observations) == NUM_OBS and self.switch >= 0):
            self.p1_active_obs = self.switch

        # reset value
        self.switch = -1

    # opponent switch after knock out
    # assumes switch is valid value
    def OpponentSwitch(self, ai):
        # if opponent is not ai and has an observation left
        if(not ai and (self.observations[3].stats[HP_STAT] > 0 or self.observations[4].stats[HP_STAT] > 0\
            or self.observations[5].stats[HP_STAT] > 0)):
            # wait for opponent to select a move
            while(not (self.switch >= 0 and self.observations[self.switch].stats[HP_STAT] > 0)):
                time.sleep(0.1)
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
            self.switch = -1
            return

        # update p1_active_obs
        if(len(self.observations) == NUM_OBS and self.switch >= 0):
            self.p2_active_obs = self.switch

        # reset value
        self.switch = -1

    # performs attacks
    def Attack(self, ai):
        # check priority
        if(self.Priority() == 0):
            # player1 moves first
            # TODO handle battle effects
            reduce_dmg_p1 = 0
            reduce_dmg_p2 = 0
            if(self.p1_move_prev != None and self.p1_move_prev.get("next_reduce_dmg") != None):
                reduce_dmg_p1 = self.p1_move.get("next_reduce_dmg")
            if(self.p2_move_prev != None and self.p2_move_prev.get("next_reduce_dmg") != None):
                reduce_dmg_p2 = self.p2_move.get("next_reduce_dmg")
            if((self.p1_move != None and self.p1_move.get("sure_hit") != None) or (self.p1_move_prev != None \
                and self.p1_move_prev.get("next_sure_hit") != None)):
                # if move is damaging
                if(self.p1_move != None and self.p1_move.get("bp") != None):
                    # calculate damage
                    self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                        self.observations[self.p1_active_obs].stats[ATK_STAT]\
                        , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                        , self.p1_move.get("bp")) * (1 - reduce_dmg_p2)
            # if not a sure hit, get whether move hits
            elif(self.p1_move != None and self.p1_move.get("acc") != None and BattleCalc.Hit(self.p1_move.get("acc")\
                , self.observations[self.p1_active_obs].stats[ACC_STAT]\
                , self.observations[self.p2_active_obs].stats[EVA_STAT])):
                # if move hits, calculate damage
                self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                    self.observations[self.p1_active_obs].stats[ATK_STAT]\
                    , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                    , self.p1_move.get("bp")) * (1 - reduce_dmg_p2)
            if(self.p1_move != None and self.p1_move.get("reduce_dmg") != None):
                reduce_dmg_p1 = self.p1_move.get("reduce_dmg")

            # check to see if opponent was knocked out
            if(self.observations[self.p2_active_obs].stats[HP_STAT] > 0):
                if((self.p2_move != None and self.p2_move.get("sure_hit") != None) or (self.p2_move_prev != None \
                    and self.p2_move_prev.get("next_sure_hit") != None)):
                    # if move is damaging
                    if(self.p2_move != None and self.p2_move.get("bp") != None):
                        # calculate damage
                        self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                            self.observations[self.p2_active_obs].stats[ATK_STAT]\
                            , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                            , self.p2_move.get("bp")) * (1 - reduce_dmg_p1)
                # if not a sure hit, get whether move hits
                elif(self.p2_move != None and self.p2_move.get("acc") != None and BattleCalc.Hit(self.p2_move.get("acc")\
                    , self.observations[self.p2_active_obs].stats[ACC_STAT]\
                    , self.observations[self.p1_active_obs].stats[EVA_STAT])):
                    # check for additional hit modifiers
                    if(self.p1_move != None and self.p1_move.get("miss_rate") != None \
                        and random.randrange(PERCENT) < self.p1_move.get("miss_rate")):
                        # if move hits, calculate damage
                        self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                            self.observations[self.p2_active_obs].stats[ATK_STAT]\
                            , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                            , self.p2_move.get("bp")) * (1 - reduce_dmg_p1)
                    else:
                        self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                            self.observations[self.p2_active_obs].stats[ATK_STAT]\
                            , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                            , self.p2_move.get("bp")) * (1 - reduce_dmg_p1)
                
                # check to see if player was knocked out
                if(self.observations[self.p2_active_obs].stats[HP_STAT] <= 0):
                    self.PlayerSwitch()
            else:
                self.OpponentSwitch(ai)
        else:
            # player2 moves first
            # TODO handle battle effects
            reduce_dmg_p1 = 0
            reduce_dmg_p2 = 0
            if(self.p2_move_prev != None and self.p2_move_prev.get("next_reduce_dmg") != None):
                reduce_dmg_p2 = self.p2_move.get("next_reduce_dmg")
            if(self.p1_move_prev != None and self.p1_move_prev.get("next_reduce_dmg") != None):
                reduce_dmg_p1 = self.p1_move.get("next_reduce_dmg")
            if((self.p2_move != None and self.p2_move.get("sure_hit") != None) or (self.p2_move_prev != None \
                and self.p2_move_prev.get("next_sure_hit") != None)):
                # if move is damaging
                if(self.p2_move != None and self.p2_move.get("bp") != None):
                    # calculate damage
                    self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                        self.observations[self.p2_active_obs].stats[ATK_STAT]\
                        , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                        , self.p2_move.get("bp")) * (1 - reduce_dmg_p1)
            # if not sure hit, get whether move hits
            elif(self.p2_move != None and self.p2_move.get("acc") != None and BattleCalc.Hit(self.p2_move.get("acc")\
                , self.observations[self.p2_active_obs].stats[ACC_STAT]\
                , self.observations[self.p1_active_obs].stats[EVA_STAT])):
                # if move hits, calculate damage
                self.observations[self.p1_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                    self.observations[self.p2_active_obs].stats[ATK_STAT]\
                    , self.observations[self.p1_active_obs].stats[DEF_STAT]\
                    , self.p2_move.get("bp")) * (1 - reduce_dmg_p1)
            if(self.p2_move != None and self.p2_move.get("reduce_dmg") != None):
                reduce_dmg_p2 = self.p2_move.get("reduce_dmg")

            # check to see if player was knocked out
            if(self.observations[self.p1_active_obs].stats[HP_STAT] > 0):
                if((self.p1_move != None and self.p1_move.get("sure_hit") != None) or (self.p1_move_prev != None \
                    and self.p1_move_prev.get("next_sure_hit") != None)):
                    # if move is damaging
                    if(self.p1_move != None and self.p1_move.get("bp") != None):
                        # calculate damage
                        self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                            self.observations[self.p1_active_obs].stats[ATK_STAT]\
                            , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                            , self.p1_move.get("bp")) * (1 - reduce_dmg_p2)
                # if not sure hit, get whether move hits
                elif(self.p1_move != None and self.p1_move.get("acc") != None and BattleCalc.Hit(self.p1_move.get("acc")\
                    , self.observations[self.p1_active_obs].stats[ACC_STAT]\
                    , self.observations[self.p2_active_obs].stats[EVA_STAT])):
                    # check for additional hit modifiers
                    if(self.p2_move != None and self.p2_move.get("miss_rate") != None \
                        and random.randrange(PERCENT) < self.p2_move.get("miss_rate")):
                        # if move hits, calculate damage
                        self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                            self.observations[self.p1_active_obs].stats[ATK_STAT]\
                            , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                            , self.p1_move.get("bp")) * (1 - reduce_dmg_p2)
                    else:
                        self.observations[self.p2_active_obs].stats[HP_STAT] -= BattleCalc.Damage(\
                            self.observations[self.p1_active_obs].stats[ATK_STAT]\
                            , self.observations[self.p2_active_obs].stats[DEF_STAT]\
                            , self.p1_move.get("bp")) * (1 - reduce_dmg_p2)
                
                # check to see if opponent was knocked out
                if(self.observations[self.p2_active_obs].stats[HP_STAT] <= 0):
                    self.OpponentSwitch(ai)
            else:
                self.PlayerSwitch()

        # set current move as previous move
        self.p1_move_prev = self.p1_move
        self.p2_move_prev = self.p2_move

        # reset moves to None
        self.p1_move = None
        self.p2_move = None

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
            if(len(self.observations) == NUM_OBS and self.observations[0].stats[HP_STAT] <= 0\
                and self.observations[1].stats[HP_STAT] <= 0 and self.observations[2].stats[HP_STAT] <= 0):
                # returns 1 for player 2 win
                return 1

            elif(len(self.observations) == NUM_OBS and self.observations[3].stats[HP_STAT] <= 0\
                and self.observations[4].stats[HP_STAT] <= 0 and self.observations[5].stats[HP_STAT] <= 0):
                # returns 0 for player 1 win
                return 0

        # if max turns are reached, both players lose
        # return 1 for player 2 win
        # since both players are player 1 from their perspective, this is a loss for both
        return 1