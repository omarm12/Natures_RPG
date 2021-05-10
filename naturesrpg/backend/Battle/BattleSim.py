# file: BattleSim.py
# author: colin seifer
# description: shows off backend battle system
##############################################
# THIS IS NOT TESTED OR PART OF THE CODEBASE
# THIS IS JUST FOR FUN
##############################################

from multiprocessing.pool import ThreadPool
import time
from . import Moves
from . import LoadObservation
from . import BattleCalc
from . import BattleSys
from . import BattleEffects
from . import MoveDicts
from ..Utils import StatsAssign

type_set = {
    'Insecta',
    'Reptilia',
    'Actinopterygii',
    'Mammalia',
    'Amphibia',
    'Arachnida',
    'Aves',
    'Mollusca',
    'Chromista',
    'Animalia',
    'Plantae',
    'Fungi',
    'Protozoa'
}

observations = []

for i in range(3):
    moves = []
    user_in = ''

    # get obs types
    print()
    print("Please choose a type for observation " + str(i) + ":")
    for a_type in type_set:
        print(a_type)

    user_in = input("Enter choice: ")
    while(user_in not in type_set):
        user_in = input("Invalid choice. Please choose a type for observation " + str(i) + ": ")

    obs_type = user_in

    for j in range(4):
        move_choice = ''

        # get move choices
        print()
        print("Please choose the observation's move " + str(j) + ":")
        if(obs_type == "Insecta"):
            for move in MoveDicts.animalia_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.animalia_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Reptilia"):
            for move in MoveDicts.reptilia_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.reptilia_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Actinopterygii"):
            for move in MoveDicts.actinopterygii_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.actinopterygii_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Mammalia"):
            for move in MoveDicts.mammalia_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.mammalia_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Amphibia"):
            for move in MoveDicts.amphibia_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.amphibia_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Arachnida"):
            for move in MoveDicts.arachnida_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.arachnida_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Aves"):
            for move in MoveDicts.aves_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.aves_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Mollusca"):
            for move in MoveDicts.mollusca_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.mollusca_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Chromista"):
            for move in MoveDicts.chromista_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.chromista_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Animalia"):
            for move in MoveDicts.animalia_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.animalia_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Plantae"):
            for move in MoveDicts.plantae_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.plantae_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Fungi"):
            for move in MoveDicts.fungi_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.fungi_dict):
                move_choice = input("Invalid choice. Please choose a move: ")
        elif(obs_type == "Protozoa"):
            for move in MoveDicts.protozoa_dict:
                print(move)
            move_choice = input("Enter choice: ")
            while(move_choice not in MoveDicts.protozoa_dict):
                move_choice = input("Invalid choice. Please choose a move: ")

        moves.append(move_choice)

    stats = StatsAssign.Stats(obs_type, "needs_id")
    stats_dict = stats.AssignStats()
    num_stats = [stats_dict.get("Health"), stats_dict.get("Attack"), stats_dict.get("Defense"), stats_dict.get("Accuracy"), stats_dict.get("Evasion"), stats_dict.get("Speed")]
    if(len(num_stats) != 6):
        num_stats = [100, 100, 100, 100, 100, 100]
    # create observation
    observations.append(LoadObservation.LoadObservation(obs_type, moves, num_stats))

# create opponent observations
obs_type = "Chromista"
moves = ["Extra Membrane", "Cilia", "Dazzle", "Nature's Beauty"]
stats = StatsAssign.Stats(obs_type, "needs_id")
stats_dict = stats.AssignStats()
num_stats = [stats_dict.get("Health"), stats_dict.get("Attack"), stats_dict.get("Defense"), stats_dict.get("Accuracy"), stats_dict.get("Evasion"), stats_dict.get("Speed")]
if(len(num_stats) != 6):
    num_stats = [100, 100, 100, 100, 100, 100]
observations.append(LoadObservation.LoadObservation(obs_type, moves, num_stats))

obs_type = "Insecta"
moves = ["Nature's Wrath", "Spine Shield", "Explosive Reaction", "Stinging Venom"]
stats = StatsAssign.Stats(obs_type, "needs_id")
stats_dict = stats.AssignStats()
num_stats = [stats_dict.get("Health"), stats_dict.get("Attack"), stats_dict.get("Defense"), stats_dict.get("Accuracy"), stats_dict.get("Evasion"), stats_dict.get("Speed")]
if(len(num_stats) != 6):
    num_stats = [100, 100, 100, 100, 100, 100]
observations.append(LoadObservation.LoadObservation(obs_type, moves, num_stats))

obs_type = "Arachnida"
moves = ["Spidey Sense", "Den Trap", "Stinger", "Sclerotised Pharynx"]
stats = StatsAssign.Stats(obs_type, "needs_id")
stats_dict = stats.AssignStats()
num_stats = [stats_dict.get("Health"), stats_dict.get("Attack"), stats_dict.get("Defense"), stats_dict.get("Accuracy"), stats_dict.get("Evasion"), stats_dict.get("Speed")]
if(len(num_stats) != 6):
    num_stats = [100, 100, 100, 100, 100, 100]
observations.append(LoadObservation.LoadObservation(obs_type, moves, num_stats))

# create battle
battle = BattleSys.Battle(observations)
battle_thread = ThreadPool(processes=1)
async_res = battle_thread.apply_async(battle.BattleLoop, (True,))

in_progress = True
turn = 0
# as long as the battle is not over
while(in_progress):
    # display observation stats
    print()
    print("Your active observation: (>*w*)>")
    print(observations[battle.p1_active_obs].observation_type)
    print("HP: " + str(int(battle.observations[battle.p1_active_obs].stats[0])) + " / " + str(int(float(battle.observations[battle.p1_active_obs].base_stats[0]) * 1. + battle.observations[battle.p1_active_obs].stat_mod[0])))
    print("Atk: " + str(battle.observations[battle.p1_active_obs].stats[1]))
    print("Def: " + str(battle.observations[battle.p1_active_obs].stats[2]))
    print("Acc: " + str(battle.observations[battle.p1_active_obs].stats[3]))
    print("Eva: " + str(battle.observations[battle.p1_active_obs].stats[4]))
    print("Spd: " + str(battle.observations[battle.p1_active_obs].stats[5]))
    print()
    print("Opponent's active observation: <(*w*<)")
    print(observations[battle.p2_active_obs].observation_type)
    print("HP: " + str(int(battle.observations[battle.p2_active_obs].stats[0])) + " / " + str(int(float(battle.observations[battle.p2_active_obs].base_stats[0]) * 1. + battle.observations[battle.p2_active_obs].stat_mod[0])))
    print("Atk: " + str(battle.observations[battle.p2_active_obs].stats[1]))
    print("Def: " + str(battle.observations[battle.p2_active_obs].stats[2]))
    print("Acc: " + str(battle.observations[battle.p2_active_obs].stats[3]))
    print("Eva: " + str(battle.observations[battle.p2_active_obs].stats[4]))
    print("Spd: " + str(battle.observations[battle.p2_active_obs].stats[5]))

    choice = 0
    while(choice < 1 or choice > 5):
        # get user move choice
        print()
        print("choose an option:")
        for i in range(4):
            print(str(i + 1) + ". [" + observations[battle.p1_active_obs].moves[i].get("name") + "]")
            print(observations[battle.p1_active_obs].moves[i].get("flavor_text"))
        print("5. [Switch]")
        choice = int(input(": "))

    if(choice != 5):
        battle.move_choice = choice
    else:
        choice = 0
        valid_choices = []
        # get switch choice
        while(choice not in valid_choices):
            print("choose an observation to switch to:")
            for i in range(3):
                if(battle.observations[i].stats[0] > 0):
                    print(str(i) + ". " + battle.observations[i].observation_type)
                    valid_choices.append(i)
            choice = int(input(": "))
        battle.switch = choice
    
    # wait to make sure attack finished
    time.sleep(0.3)

    # output moves
    print()
    if(battle.Priority() == 0):
        if(battle.p1_move_prev == None):
            print("Your observation failed to make a move.")
        else:
            print("Your observation used " + battle.p1_move_prev.get("name") + ".")
        if(battle.p2_move_prev == None):
            print("Your opponent's observation failed to make a move.")
        else:
            print("Your opponent's observation used " + battle.p2_move_prev.get("name") + ".")
    else:
        if(battle.p2_move_prev == None):
            print("Your opponent's observation failed to make a move.")
        else:
            print("Your opponent's observation used " + battle.p2_move_prev.get("name") + ".")
        if(battle.p1_move_prev == None):
            print("Your observation failed to make a move.")
        else:
            print("Your observation used " + battle.p1_move_prev.get("name") + ".")

    # check to see if user observation was knocked out
    if(battle.observations[battle.p1_active_obs].stats[0] <= 0):
        # check if user has observations remaining
        in_progress = False
        for i in range(3):
            if(battle.observations[i].stats[0] > 0):
                in_progress = True
        if(in_progress):
            print("Your observation was knocked out. Please choose a new observation to battle.")
            choice = 0
            valid_choices = []
            # get switch choice
            while(choice not in valid_choices):
                print("choose an observation to switch to:")
                for i in range(3):
                    if(battle.observations[i].stats[0] > 0):
                        print(str(i) + ". " + battle.observations[i].observation_type)
                        valid_choices.append(i)
                choice = int(input(": "))
            battle.switch = choice

    # check to see if opponent observation was knocked out
    if(battle.observations[battle.p2_active_obs].stats[0] <= 0):
        # check if opponent has observations remaining
        in_progress = False
        if(battle.observations[3].stats[0] > 0):
            in_progress = True
        if(battle.observations[4].stats[0] > 0):
            in_progress = True
        if(battle.observations[5].stats[0] > 0):
            in_progress = True

    # wait to make sure switch finished and for user to read text
    time.sleep(1.5)
    turn += 1
    if(turn > 14):
        in_progress = False

winner = async_res.get()
if(winner == 0):
    print("You and your team of observations emerge from battle victorious!")
else:
    print("You were defeated this time. Keep training and don't stop reaching for victory.")