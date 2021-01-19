import unittest
from NBA_game_simulator import *

class TestTeam(unittest.TestCase):
    def setUp(self):
        self.bos = Team('BOS', '2001')
        self.sea = Team('SEA', '1980')
        self.phi = Team('PHI', '2018')
    
    def test_init(self):
        fields = ['Player', 'MPRatioAdj', 'eMP', 'ePPG']
        self.assertEqual(self.bos.team, 'BOS')
        self.assertEqual(self.bos.year, '2001')
        self.assertAlmostEqual(self.bos.pts_for, 94.6, places=1)
        self.assertAlmostEqual(self.bos.pts_for_std, 9.46, places=1)
        self.assertAlmostEqual(self.bos.pts_against, 96.75, places=1)
        self.assertAlmostEqual(self.bos.pts_against_std, 10.64, places=1)
        self.assertEqual(self.bos.pts_league_avg, 94.8)
        self.assertCountEqual(list(self.bos.team_stats), fields)

        self.assertEqual(self.sea.team, 'SEA')
        self.assertEqual(self.sea.year, '1980')
        self.assertAlmostEqual(self.sea.pts_for, 108.5, places=1)
        self.assertAlmostEqual(self.sea.pts_for_std, 11.34, places=1)
        self.assertAlmostEqual(self.sea.pts_against, 103.84, places=1)
        self.assertAlmostEqual(self.sea.pts_against_std, 10.80, places=1)
        self.assertEqual(self.sea.pts_league_avg, 109.3)
        self.assertCountEqual(list(self.sea.team_stats), fields)

        self.assertEqual(self.phi.team, 'PHI')
        self.assertEqual(self.phi.year, '2018')
        self.assertAlmostEqual(self.phi.pts_for, 109.8, places=1)
        self.assertAlmostEqual(self.phi.pts_for_std, 10.27, places=1)
        self.assertAlmostEqual(self.phi.pts_against, 105.3, places=1)
        self.assertAlmostEqual(self.phi.pts_against_std, 11.53, places=1)
        self.assertEqual(self.phi.pts_league_avg, 106.3)
        self.assertCountEqual(list(self.phi.team_stats), fields)
    
    @unittest.expectedFailure
    def test_init_fail(self):
        self.assertRaises(Team('TOR', ''), requests.exceptions.RequestException)
        self.assertRaises(Team('hello', '2001'), requests.exceptions.RequestException)
        self.assertRaises(Team('', ''), requests.exceptions.RequestException)
        self.assertRaises(Team('', '2014'), requests.exceptions.RequestException)
        self.assertRaises(Team('DEN', '8732'), requests.exceptions.RequestException)

class TestMatchup(unittest.TestCase):
    def setUp(self):
        self.lac = Team('LAC', '2005')
        self.chi = Team('CHI', '1999')
        self.den = Team('DEN', '2015')
        self.match1 = Matchup(self.lac, self.chi)
        self.match2 = Matchup(self.chi, self.den)
        self.match3 = Matchup(self.den, self.lac, 0)
    
    def test_init(self):
        self.assertAlmostEqual(self.match1.home_weighted_pts, 97.29, places=1)
        self.assertAlmostEqual(self.match1.away_weighted_pts, 80.94, places=1)
        self.assertEqual(self.match1.home_adv, 3)

        self.assertAlmostEqual(self.match2.home_weighted_pts, 88.62, places=1)
        self.assertAlmostEqual(self.match2.away_weighted_pts, 102.55, places=1)
        self.assertEqual(self.match2.home_adv, 3)

        self.assertAlmostEqual(self.match3.home_weighted_pts, 102.06, places=1)
        self.assertAlmostEqual(self.match3.away_weighted_pts, 99.27, places=1)
        self.assertEqual(self.match3.home_adv, 0)

class TestMatchup(unittest.TestCase):
    def setUp(self):
        self.cle = Team('CLE', '1994')
        self.hou = Team('HOU', '2000')
        self.mem = Team('MEM', '2020')
        self.match1 = Matchup(self.cle, self.hou)
        self.match2 = Matchup(self.hou, self.mem, 0)
        self.match3 = Matchup(self.mem, self.cle, 5)
        self.sim1 = Simulation(self.match1)
        self.sim2 = Simulation(self.match2)
        self.sim3 = Simulation(self.match3)
    
    def test_init(self):
        self.assertEqual(self.sim1.home_wins, 0)
        self.assertEqual(self.sim1.away_wins, 0)

        self.assertEqual(self.sim2.home_wins, 0)
        self.assertEqual(self.sim2.away_wins, 0)

        self.assertEqual(self.sim3.home_wins, 0)
        self.assertEqual(self.sim3.away_wins, 0)

    def test_simulate_single_game(self):
        self.assertEqual(self.sim1._simulate_single_game(self.sim1.matchup.home_weighted_pts, self.sim1.matchup.home_team.pts_for_std, 1), 120.93744408529281)
        self.assertEqual(self.sim2._simulate_single_game(self.sim2.matchup.home_weighted_pts, self.sim2.matchup.home_team.pts_for_std, 5), 89.05369935224415)
        self.assertEqual(self.sim3._simulate_single_game(self.sim3.matchup.home_weighted_pts, self.sim3.matchup.home_team.pts_for_std, 10), 103.91700414838357)

if __name__ == '__main__':
    unittest.main()