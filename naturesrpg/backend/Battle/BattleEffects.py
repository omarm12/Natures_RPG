# file: BattleEffects.py
# author: colin seifer
# description: handles additional battle effects.

from . import LoadObservation

# constants
HP_STAT = 0
ATK_STAT = 1
DEF_STAT = 2
ACC_STAT = 3
EVA_STAT = 4
SPD_STAT = 5
NUM_OBS = 6

# player is 0 for user or 1 for opponent
# move is a move object, not a string
# active obs is an int
# observations is a list of observation objects
def additional_effects(observations, p1_active_obs, p2_active_obs, move, player):
    if(len(observations) != NUM_OBS):
        return

    active_obs = p1_active_obs
    opp_active_obs = p2_active_obs
    if(player == 1):
        active_obs = p2_active_obs
        opp_active_obs = p1_active_obs

    # individual stat modifications
    if(move != None and move.get("hp_mod") != None):
        observations[active_obs].stat_mod[HP_STAT] += move.get("hp_mod")
    if(move != None and move.get("atk_mod") != None):
        observations[active_obs].stat_mod[ATK_STAT] += move.get("atk_mod")
    if(move != None and move.get("def_mod") != None):
        observations[active_obs].stat_mod[DEF_STAT] += move.get("def_mod")
    if(move != None and move.get("acc_mod") != None):
        observations[active_obs].stat_mod[ACC_STAT] += move.get("acc_mod")
    if(move != None and move.get("eva_mod") != None):
        observations[active_obs].stat_mod[EVA_STAT] += move.get("eva_mod")
    if(move != None and move.get("spd_mod") != None):
        observations[active_obs].stat_mod[SPD_STAT] += move.get("spd_mod")

    # team stat modifications
    if(move != None and move.get("team_hp_mod") != None):
        if(player == 0):
            observations[0].stat_mod[HP_STAT] += move.get("team_hp_mod")
            observations[1].stat_mod[HP_STAT] += move.get("team_hp_mod")
            observations[2].stat_mod[HP_STAT] += move.get("team_hp_mod")
        elif(player == 1):
            observations[3].stat_mod[HP_STAT] += move.get("team_hp_mod")
            observations[4].stat_mod[HP_STAT] += move.get("team_hp_mod")
            observations[5].stat_mod[HP_STAT] += move.get("team_hp_mod")
    if(move != None and move.get("team_atk_mod") != None):
        if(player == 0):
            observations[0].stat_mod[ATK_STAT] += move.get("team_atk_mod")
            observations[1].stat_mod[ATK_STAT] += move.get("team_atk_mod")
            observations[2].stat_mod[ATK_STAT] += move.get("team_atk_mod")
        elif(player == 1):
            observations[3].stat_mod[ATK_STAT] += move.get("team_atk_mod")
            observations[4].stat_mod[ATK_STAT] += move.get("team_atk_mod")
            observations[5].stat_mod[ATK_STAT] += move.get("team_atk_mod")
    if(move != None and move.get("team_def_mod") != None):
        if(player == 0):
            observations[0].stat_mod[DEF_STAT] += move.get("team_def_mod")
            observations[1].stat_mod[DEF_STAT] += move.get("team_def_mod")
            observations[2].stat_mod[DEF_STAT] += move.get("team_def_mod")
        elif(player == 1):
            observations[3].stat_mod[DEF_STAT] += move.get("team_def_mod")
            observations[4].stat_mod[DEF_STAT] += move.get("team_def_mod")
            observations[5].stat_mod[DEF_STAT] += move.get("team_def_mod")
    if(move != None and move.get("team_acc_mod") != None):
        if(player == 0):
            observations[0].stat_mod[ACC_STAT] += move.get("team_acc_mod")
            observations[1].stat_mod[ACC_STAT] += move.get("team_acc_mod")
            observations[2].stat_mod[ACC_STAT] += move.get("team_acc_mod")
        elif(player == 1):
            observations[3].stat_mod[ACC_STAT] += move.get("team_acc_mod")
            observations[4].stat_mod[ACC_STAT] += move.get("team_acc_mod")
            observations[5].stat_mod[ACC_STAT] += move.get("team_acc_mod")
    if(move != None and move.get("team_eva_mod") != None):
        if(player == 0):
            observations[0].stat_mod[EVA_STAT] += move.get("team_eva_mod")
            observations[1].stat_mod[EVA_STAT] += move.get("team_eva_mod")
            observations[2].stat_mod[EVA_STAT] += move.get("team_eva_mod")
        elif(player == 1):
            observations[3].stat_mod[EVA_STAT] += move.get("team_eva_mod")
            observations[4].stat_mod[EVA_STAT] += move.get("team_eva_mod")
            observations[5].stat_mod[EVA_STAT] += move.get("team_eva_mod")
    if(move != None and move.get("team_spd_mod") != None):
        if(player == 0):
            observations[0].stat_mod[SPD_STAT] += move.get("team_spd_mod")
            observations[1].stat_mod[SPD_STAT] += move.get("team_spd_mod")
            observations[2].stat_mod[SPD_STAT] += move.get("team_spd_mod")
        elif(player == 1):
            observations[3].stat_mod[SPD_STAT] += move.get("team_spd_mod")
            observations[4].stat_mod[SPD_STAT] += move.get("team_spd_mod")
            observations[5].stat_mod[SPD_STAT] += move.get("team_spd_mod")
    
    # opponent stat modifications
    if(move != None and move.get("opp_hp_mod") != None):
        observations[opp_active_obs].stat_mod[HP_STAT] += move.get("opp_hp_mod")
    if(move != None and move.get("opp_atk_mod") != None):
        observations[opp_active_obs].stat_mod[ATK_STAT] += move.get("opp_atk_mod")
    if(move != None and move.get("opp_def_mod") != None):
        observations[opp_active_obs].stat_mod[DEF_STAT] += move.get("opp_def_mod")
    if(move != None and move.get("opp_acc_mod") != None):
        observations[opp_active_obs].stat_mod[ACC_STAT] += move.get("opp_acc_mod")
    if(move != None and move.get("opp_eva_mod") != None):
        observations[opp_active_obs].stat_mod[EVA_STAT] += move.get("opp_eva_mod")
    if(move != None and move.get("opp_spd_mod") != None):
        observations[opp_active_obs].stat_mod[SPD_STAT] += move.get("opp_spd_mod")
    
    # set stat mods within acceptible range
    for obs in observations:
        if(obs.stat_mod[HP_STAT] > 1.0):
            obs.stat_mod[HP_STAT] = 1.0
        elif(obs.stat_mod[HP_STAT] < -0.5):
            obs.stat_mod[HP_STAT] = -0.5
        if(obs.stat_mod[ATK_STAT] > 1.0):
            obs.stat_mod[ATK_STAT] = 1.0
        elif(obs.stat_mod[ATK_STAT] < -0.5):
            obs.stat_mod[ATK_STAT] = -0.5
        if(obs.stat_mod[DEF_STAT] > 1.0):
            obs.stat_mod[DEF_STAT] = 1.0
        elif(obs.stat_mod[DEF_STAT] < -0.5):
            obs.stat_mod[DEF_STAT] = -0.5
        if(obs.stat_mod[ACC_STAT] > 1.0):
            obs.stat_mod[ACC_STAT] = 1.0
        elif(obs.stat_mod[ACC_STAT] < -0.5):
            obs.stat_mod[ACC_STAT] = -0.5
        if(obs.stat_mod[EVA_STAT] > 1.0):
            obs.stat_mod[EVA_STAT] = 1.0
        elif(obs.stat_mod[EVA_STAT] < -0.5):
            obs.stat_mod[EVA_STAT] = -0.5
        if(obs.stat_mod[SPD_STAT] > 1.0):
            obs.stat_mod[SPD_STAT] = 1.0
        elif(obs.stat_mod[SPD_STAT] < -0.5):
            obs.stat_mod[SPD_STAT] = -0.5

    # set retreat and revive
    if(move != None and move.get("no_retreat") != None):
        observations[active_obs].retreat = 0
    if(move != None and move.get("revive_with_hp") != None and observations[active_obs].revive != -1):
        observations[active_obs].revive = move.get("revive_with_hp")

    # additional damage and healing effects
    # damage takes effect before healing
    if(move != None and move.get("user_dmg") != None):
        observations[active_obs].stats[HP_STAT] -= move.get("user_dmg") * observations[active_obs].base_stats[HP_STAT]
    if(move != None and move.get("opp_dmg") != None):
        observations[opp_active_obs].stats[HP_STAT] -= move.get("opp_dmg") * observations[opp_active_obs].base_stats[HP_STAT]
    if(move != None and move.get("opp_dot") != None):
        observations[opp_active_obs].stats[HP_STAT] -= move.get("opp_dot") * observations[opp_active_obs].base_stats[HP_STAT]
    if(move != None and move.get("heal_ot") != None):
        observations[active_obs].stats[HP_STAT] += move.get("heal_ot") * observations[active_obs].base_stats[HP_STAT]
    if(move != None and move.get("team_heal") != None):
        if(player == 0):
            observations[0].stats[HP_STAT] = int((1. + observations[0].stat_mod[HP_STAT]) * observations[0].base_stats[HP_STAT])
            observations[1].stats[HP_STAT] = int((1. + observations[1].stat_mod[HP_STAT]) * observations[1].base_stats[HP_STAT])
            observations[2].stats[HP_STAT] = int((1. + observations[2].stat_mod[HP_STAT]) * observations[2].base_stats[HP_STAT])
        elif(player == 1):
            observations[3].stats[HP_STAT] = int((1. + observations[3].stat_mod[HP_STAT]) * observations[3].base_stats[HP_STAT])
            observations[4].stats[HP_STAT] = int((1. + observations[4].stat_mod[HP_STAT]) * observations[4].base_stats[HP_STAT])
            observations[5].stats[HP_STAT] = int((1. + observations[5].stat_mod[HP_STAT]) * observations[5].base_stats[HP_STAT])
    if(move != None and move.get("ko_type") != None):
        if(observations[opp_active_obs].observation_type == move.get("ko_type")):
            observations[opp_active_obs].stats[HP_STAT] = 0
    
    # update stats
    for obs in observations:
        obs.stats[HP_STAT] = int((1. + obs.stat_mod[HP_STAT]) * obs.base_stats[HP_STAT]) - \
            (obs.base_stats[HP_STAT] - obs.stats[HP_STAT])
        obs.stats[ATK_STAT] = int((1. + obs.stat_mod[ATK_STAT]) * obs.base_stats[ATK_STAT])
        obs.stats[DEF_STAT] = int((1. + obs.stat_mod[DEF_STAT]) * obs.base_stats[DEF_STAT])
        obs.stats[ACC_STAT] = int((1. + obs.stat_mod[ACC_STAT]) * obs.base_stats[ACC_STAT])
        obs.stats[EVA_STAT] = int((1. + obs.stat_mod[EVA_STAT]) * obs.base_stats[EVA_STAT])
        obs.stats[SPD_STAT] = int((1. + obs.stat_mod[SPD_STAT]) * obs.base_stats[SPD_STAT])