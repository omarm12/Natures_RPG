# file: BattleCalc.py
# author: colin seifer
# description: performs calculations needed for battle

import random
import math

# determines whether a move hits
# simulates confidence interval curve
def Hit(move_acc, acc, eva):
    PERCENT = 100 # div by 100 to get 0 to 1

    # one-sided confidence interval
    ci = float(move_acc) / float(PERCENT)

    # find range max and min
    range_max = PERCENT
    range_min = PERCENT - (eva / math.sqrt(acc))

    # get random value in range
    rand = random.uniform(range_min, range_max)

    # determine if move hits
    if(rand > PERCENT - ci * (acc / math.sqrt(eva))):
        return True
    else:
        return False

# returns damage dealt from a move as a raw integer
def Damage(atk, defense, bp):
    return int((atk / defense) * bp)

# returns difference between modified speed stats
def Speed(speed, speed2):
    # return diff between bspeed and bspeed2
    return speed - speed2