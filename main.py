from game import Game
from player import Player
import itertools
import matplotlib.pyplot as plt
import re
from strategies import *
# Define players with different strategies
strategies = {
    "Conservative": conservative_predict,
    "Aggressive": aggressive_predict,
    "Random": random_predict,
    "Tactical": tactical_predict,
    "Steady Increment": steady_increment_predict,
    "Cautious": cautious_predict,
    "Reactive": reactive_predict,
    "Average Seeker": average_seeker_predict,
    "Opportunistic": opportunistic_predict
}

# Generate all possible permutations of four strategies
strategy_names = list(strategies.keys())
strategy_permutations = list(itertools.permutations(strategy_names, 4))

results = []

# Run simulation for each permutation of four players
for permutation in strategy_permutations:
    players = [Player(name, strategies[name]) for name in permutation]
    game = Game(players)
    game.start_game(50)  # Assuming each match consists of 50 rounds
    results.append((permutation, game.curr_scores))

# Extract scores and determine winners
scoreboard = {name: 0 for name in strategies}

for permutation, scores in results:
    max_score = max(scores)
    winners = [permutation[i] for i, score in enumerate(scores) if score == max_score]
    for winner in winners:
        scoreboard[winner] += 1

# Plot results
labels, values = zip(*scoreboard.items())
indexes = range(len(labels))
width = 0.5

plt.bar(indexes, values, width, color=['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'gray', 'brown'])
plt.xticks(indexes, labels, rotation=90)
plt.title('Strategy Dominance in Simulation')
plt.xlabel('Strategy')
plt.ylabel('Number of Wins')
plt.show()
