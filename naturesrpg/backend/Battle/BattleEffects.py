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

def additional_effects(observations[], p1_active_obs, p2_active_obs, move, player):
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
        if(player = 0):
            observations[0].stat_mod[HP_STAT] += move.get("team_hp_mod")
            observations[1].stat_mod[HP_STAT] += move.get("team_hp_mod")
            observations[2].stat_mod[HP_STAT] += move.get("team_hp_mod")
        elif(player = 1):
            observations[3].stat_mod[HP_STAT] += move.get("team_hp_mod")
            observations[4].stat_mod[HP_STAT] += move.get("team_hp_mod")
            observations[5].stat_mod[HP_STAT] += move.get("team_hp_mod")
    if(move != None and move.get("team_atk_mod") != None):
        if(player = 0):
            observations[0].stat_mod[ATK_STAT] += move.get("team_atk_mod")
            observations[1].stat_mod[ATK_STAT] += move.get("team_atk_mod")
            observations[2].stat_mod[ATK_STAT] += move.get("team_atk_mod")
        elif(player = 1):
            observations[3].stat_mod[ATK_STAT] += move.get("team_atk_mod")
            observations[4].stat_mod[ATK_STAT] += move.get("team_atk_mod")
            observations[5].stat_mod[ATK_STAT] += move.get("team_atk_mod")
    if(move != None and move.get("team_def_mod") != None):
        if(player = 0):
            observations[0].stat_mod[DEF_STAT] += move.get("team_def_mod")
            observations[1].stat_mod[DEF_STAT] += move.get("team_def_mod")
            observations[2].stat_mod[DEF_STAT] += move.get("team_def_mod")
        elif(player = 1):
            observations[3].stat_mod[DEF_STAT] += move.get("team_def_mod")
            observations[4].stat_mod[DEF_STAT] += move.get("team_def_mod")
            observations[5].stat_mod[DEF_STAT] += move.get("team_def_mod")
    if(move != None and move.get("team_acc_mod") != None):
        if(player = 0):
            observations[0].stat_mod[ACC_STAT] += move.get("team_acc_mod")
            observations[1].stat_mod[ACC_STAT] += move.get("team_acc_mod")
            observations[2].stat_mod[ACC_STAT] += move.get("team_acc_mod")
        elif(player = 1):
            observations[3].stat_mod[ACC_STAT] += move.get("team_acc_mod")
            observations[4].stat_mod[ACC_STAT] += move.get("team_acc_mod")
            observations[5].stat_mod[ACC_STAT] += move.get("team_acc_mod")
    if(move != None and move.get("team_eva_mod") != None):
        if(player = 0):
            observations[0].stat_mod[EVA_STAT] += move.get("team_eva_mod")
            observations[1].stat_mod[EVA_STAT] += move.get("team_eva_mod")
            observations[2].stat_mod[EVA_STAT] += move.get("team_eva_mod")
        elif(player = 1):
            observations[3].stat_mod[EVA_STAT] += move.get("team_eva_mod")
            observations[4].stat_mod[EVA_STAT] += move.get("team_eva_mod")
            observations[5].stat_mod[EVA_STAT] += move.get("team_eva_mod")
    if(move != None and move.get("team_spd_mod") != None):
        if(player = 0):
            observations[0].stat_mod[SPD_STAT] += move.get("team_spd_mod")
            observations[1].stat_mod[SPD_STAT] += move.get("team_spd_mod")
            observations[2].stat_mod[SPD_STAT] += move.get("team_spd_mod")
        elif(player = 1):
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
        for stat in obs.stat_mod:
            if(stat > 1.0):
                stat = 1.0
            if(stat < 0.5):
                stat = 0.5

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
        if(player = 0):
            observations[p1_active_obs].stat_mod[HP_STAT] -= move.get("team_heal") * observations[p1_active_obs].base_stats[HP_STAT]
            observations[0].stat_mod[HP_STAT] += move.get("team_heal") * observations[0].base_stats[HP_STAT]
            observations[1].stat_mod[HP_STAT] += move.get("team_heal") * observations[1].base_stats[HP_STAT]
            observations[2].stat_mod[HP_STAT] += move.get("team_heal") * observations[2].base_stats[HP_STAT]
        elif(player = 1):
            observations[p2_active_obs].stat_mod[HP_STAT] -= move.get("team_heal") * observations[p2_active_obs].base_stats[HP_STAT]
            observations[3].stat_mod[HP_STAT] += move.get("team_heal") * observations[3].base_stats[HP_STAT]
            observations[4].stat_mod[HP_STAT] += move.get("team_heal") * observations[4].base_stats[HP_STAT]
            observations[5].stat_mod[HP_STAT] += move.get("team_heal") * observations[5].base_stats[HP_STAT]
    if(move != None and move.get("ko_type") != None):
        if(observations[opp_active_obs].observation_type == move.get("ko_type")):
            observations[opp_active_obs].stats[HP_STAT] = 0

# More battle effects that need to be handled in BattleSys.py
# not yet implemented

# take effect after move
#"free_switch":0, - user switches with party member without using a turn – 0 or 1
#"force_switch":0, - forces opponent to switch with party member 0 or 1
#"revive_with_hp":0, - user revives after KO with specified health – 0 to 1
#"learn_opp_move":0 – learn an opponent’s move at random – 0 or 1

# take effect before move
#"rand_move":0, - uses a move at random – 0 or 1
#"no_retreat":0, - user cannot retreat – 0 or 1
#"use_opp_atk":0, - user uses opponent’s attack – 0 or 1
#"opp_move_lock":0, - locks opponent’s specified move – 0 to 4 (int)
#"single_move":0, - user can only use a single chosen move – 0 or 1
#"opp_single_move":0, - opponent can only use a single chosen move – 0 or 1

# take effect during move
#"next_atk_lock":0, - opponent can’t attack next turn – 0 or 1
#"ignore_def":0, - user ignores defense modifications on the opponent – 0 or 1
#"require_opp_contact":0, - opponent must make contact for move to work – 0 or 1
#"reduce_dmg_type":"", - reduce incoming damage from a specific type - string
#"require_move":”” – can only use after specified move – string
#"require_priority":0 – requires user to move first – 0 or 1
#"require_first_turn":0 – can only use on first turn – 0 or 1