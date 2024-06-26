def conservative_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 5)
    highest_bid = max(bid for _, bid in previous_players)
    new_bid = highest_bid + 2 if highest_bid < 10 else 0  # Bids more if the highest is low
    return (True, new_bid) if new_bid > 0 else (False, 0)

def aggressive_predict(scoreboard, previous_players):
    initial_bid = 15
    if not previous_players:
        return (True, initial_bid)
    # Reduces bid if didn't win last round
    last_round_win = previous_players[-1][0] == 'PlayerName' and previous_players[-1][1] > 0
    return (True, initial_bid - 5) if not last_round_win else (True, initial_bid)
import random

def random_predict(scoreboard, previous_players):
    participate = random.choice([True, False])
    bid = random.randint(0, 10) if participate else 0
    return (participate, bid)

def tactical_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 10)
    average_bid = sum(bid for _, bid in previous_players) / len(previous_players)
    return (True, int(average_bid + 5)) if average_bid < 8 else (False, 0)


import math

def steady_increment_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 5)
    last_bid = previous_players[-1][1]
    new_bid = last_bid + 3 if last_bid < 20 else 5
    return (True, new_bid)
def cautious_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 4)
    average_bid = sum(bid for _, bid in previous_players) / len(previous_players)
    new_bid = average_bid + 1 if average_bid < 5 else 3
    return (True, new_bid)

def reactive_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 6)
    highest_bid = max(bid for _, bid in previous_players)
    new_bid = highest_bid + 1 if highest_bid < 8 else 0
    return (True, new_bid) if new_bid > 0 else (False, 0)

def average_seeker_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 7)
    average_bid = sum(bid for _, bid in previous_players) / len(previous_players)
    return (True, int(average_bid))

def opportunistic_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 8)
    highest_bid = max(bid for _, bid in previous_players)
    if highest_bid < 5:
        return (True, highest_bid + 3)
    elif highest_bid > 10:
        return (True, highest_bid - 5)
    else:
        return (True, highest_bid)
