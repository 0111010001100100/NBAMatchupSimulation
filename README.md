# NBA Game Simulator

This project scrapes data from basketball-reference.com to predict the outcome of a matchup. Predictions are made based on a teams mean points for and against for a given season, the opponents mean points for and against for a given season, as well as the individual players points and minutes played for the season. The code to be reviewed is in NBA_game_simulator.py. They test.py file contains the unittests and main.py contains runnable examples. The simulation only considers regular season game statistics.

## Usage

This project was made and tested with Python 3.8.

From the NBAMatchupSimulationDirectory:
```
$ pip install -r requirements.txt
```

The following command will run the examples:
```
$ python main.py
```

Alternatively, this repository contains a dockerfile.

From the NBAMatchupSimulationDirectory:
```
$ docker build -t nbamatchupsimulation .
```

The following command will run the examples:
```
$ docker run nbamatchupsimulation
``` 

### Example of running your own matchups:
```python
chi = Team('CHI', '1991')
det = Team('DET', '1986')
matchup = Matchup(chi, det, 0)
s = Simulation(matchup)
s.simulate_matchup(100000)
```

This example tests the matchup of the 'Bad Boy' Pistons against Michael Jordan's 1991 Championship Bulls.

### Example output:
```
Simulated 100000 games...
CHI won 75.274% of the games as the home team.
DET won 24.726% of the games as the away team.
```

## Testing

I have written some unittests for this project. To run the tests:
```
$ python test.py
```
