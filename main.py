from NBA_game_simulator import *

def main():
    ############
    # Examples #
    ############
    # Simulate the Seattle Supersonics 1980 team at home against the 2018 6ers team.
    print("Simulating 1980 Seattle Supersonics at home against the 2018 Philly Sixers.")
    sea = Team('SEA', '1980')
    phi = Team('PHI', '2018')
    matchup = Matchup(sea, phi)
    s = Simulation(matchup)
    s.simulate_matchup(100000)

    # Simulate Toronto Raptors 2019 championship team at home against LA Lakers 2020 championship team
    print("Simulating the 2019 Toronto Raptors championship team at home against the 2020 LA Lakers Championship team.")
    tor = Team('TOR', '2019')
    lal = Team('LAL', '2020')
    matchup = Matchup(tor, lal)
    s = Simulation(matchup)
    s.simulate_matchup(100000)

    # Simulate Toronto Raptors 2019 championship team against LA Lakers 2020 championship team with no home court advantage
    print("Simulating the 2019 Toronto Raptors championship team against the 2020 LA Lakers Championship team with no home court advantage.")
    tor = Team('TOR', '2019')
    lal = Team('LAL', '2020')
    matchup = Matchup(tor, lal, 0)
    s = Simulation(matchup)
    s.simulate_matchup(100000)

    # Simulate Chicago Bulls 1991 championship team against LA Lakers 2020 championship team with no home court advantage
    print("Simulating the 1991 Bulls championship team against the LA Lakers 2020 championship team with no home court advantage.")
    chi = Team('CHI', '1991')
    lal = Team('LAL', '2020')
    matchup = Matchup(chi, lal, 0)
    s = Simulation(matchup)
    s.simulate_matchup(100000)

if __name__ == '__main__':
    main()