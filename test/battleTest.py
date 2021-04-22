# file: battleTest.py
# author: colin seifer
# description: test suite for battle system

import unittest

from ..src import Moves
from ..src import Observation
from ..battleSystem import BattleCalc
from ..battleSystem import BattleSys

class TestStats(unittest.TestCase):

    # test that moves are imported correctly
    def test_moves(self):
        test_move = Moves.Moves()
        move = test_move.RetMove("Nature's Wrath")
        # test import
        self.assertEqual(move.get("name"), "Nature's Wrath")
        # test that invalid move returns None
        move = test_move.RetMove("invalid_move")
        self.assertIsNone(move)

    # test that observation is created correctly
    def test_observation(self):
        stats = [100, 100, 100, 100, 100, 100]
        moves = ["Nature's Wrath", "Autotomy", "Spine Shield", "Mimesis"]
        obs_type = "Insecta"
        test_obs = Observation.Observation(obs_type, moves, stats)
        # test that values are non-empty
        self.assertEqual(test_obs.stats[0], 100)
        self.assertEqual(test_obs.moves[0].get("name"), "Nature's Wrath")
        self.assertEqual(test_obs.stat_mod[0], 0)
        self.assertEqual(test_obs.observation_type, "Insecta")

    # test that battle calculations are correctly computed
    def test_battleCalc(self):
        hit = 0
        miss = 0
        for i in range(1000):
            res = BattleCalc.Hit(80, 100, 100)
            if(res):
                hit += 1
            else:
                miss += 1
        # test that some moves hit and some missed
        self.assertTrue(hit > 0 and miss > 0)
        # test that damage is calculated correctly
        self.assertEqual(BattleCalc.Damage(100, 100, 80), 80)
        # test that speed is computed correctly
        self.assertTrue(BattleCalc.Speed(100, 0.2, 100, 0) > 0)
        self.assertTrue(BattleCalc.Speed(100, 0, 101, 0) < 0)
        self.assertEqual(BattleCalc.Speed(100, 0.5, 100, 0.5), 0)

    # test that battle system works properly
    def test_battle_sys(self):
        stats = [100, 100, 100, 100, 100, 100]
        moves = ["Nature's Wrath", "Autotomy", "Spine Shield", "Mimesis"]
        obs_type = "Insecta"
        observations = []
        # create list of 6 observations
        for i in range(6):
            observations.append(Observation.Observation(obs_type, moves, stats))
        # create battle object
        test_battle = BattleSys.Battle(observations)
        # test battle object observations size
        self.assertEqual(len(test_battle.observations), 6)
        # test that observations were imported correctly
        self.assertEqual(test_battle.observations[0].stats[0], 100)

        # test player turn switch
        test_battle.switch = 1
        test_battle.PlayerTurn()
        self.assertEqual(test_battle.p1_active_obs, 1)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        #test player turn move
        test_battle.move_choice = 4
        test_battle.PlayerTurn()
        self.assertEqual(test_battle.p1_move, test_battle.observations[1].moves[3])
        # test that move is reset
        self.assertEqual(test_battle.move_choice, 0)

        # test opponent not ai turn switch
        test_battle.switch = 4
        test_battle.OpponentTurn(False)
        self.assertEqual(test_battle.p2_active_obs, 4)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        #test opponent not ai turn move
        test_battle.move_choice = 4
        test_battle.OpponentTurn(False)
        self.assertEqual(test_battle.p2_move, test_battle.observations[4].moves[3])
        # test that move is reset
        self.assertEqual(test_battle.move_choice, 0)

        # test priority
        # p1_move should have higher priority
        test_battle.p1_move = test_battle.observations[1].moves[2]
        test_battle.p2_move = test_battle.observations[1].moves[3]
        # p1 priority indicated by return of 0
        self.assertEqual(test_battle.Priority(), 0)

        # p2_move should have higher priority
        test_battle.p1_move = test_battle.observations[1].moves[3]
        test_battle.p2_move = test_battle.observations[1].moves[2]
        # p2 priority indicated by return of 1
        self.assertEqual(test_battle.Priority(), 1)

        # test player switch
        test_battle.switch = 2
        test_battle.PlayerSwitch()
        self.assertEqual(test_battle.p1_active_obs, 2)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        # test opponent not ai switch
        test_battle.switch = 5
        test_battle.OpponentSwitch(False)
        self.assertEqual(test_battle.p2_active_obs, 5)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        # test attack not ai
        self.assertEqual(test_battle.observations[test_battle.p2_active_obs].stats[4], 100)
        test_battle.Attack(False)
        # test that p1 attack reduces HP of p2 observation by 60
        self.assertEqual(test_battle.observations[5].stats[0], 40)
        # knock out p2 observation
        test_battle.switch = 4
        test_battle.Attack(False)
        self.assertTrue(test_battle.observations[5].stats[0] <= 0)
        # test that p2 observation was switched to 4
        self.assertEqual(test_battle.p2_active_obs, 4)
        # knock out p2 observation 4
        test_battle.Attack(False)
        test_battle.switch = 3
        test_battle.Attack(False)
        self.assertTrue(test_battle.observations[4].stats[0] <= 0)
        self.assertEqual(test_battle.p2_active_obs, 3)
        # attack one more time to get p2 final observation to 40hp
        test_battle.Attack(False)

        # test final turn in BattleLoop with ai
        test_battle.move_choice = 4
        # player 1 should win which is returned as a 0
        self.assertEqual(test_battle.BattleLoop(True), 0)

if __name__ == '__main__':
    unittest.main()