from player import Player

playerss = [Player("PlayerName", None), Player("PlayerName", None), Player("PlayerName", None), Player("PlayerName", None)]

class Game:
    def __init__(self, players):
        self.rounds_played = 0
        self.players = players
        self.curr_scores = [0] * 4
        self.scoreboard = []

    def __repr__(self):
        return f'Game(players={self.players}, \n Leaderboard = {self.curr_scores},\n  rounds_played={self.rounds_played})'

    def play_round(self):
        current_bids = []
        declines = 0
        total_purse = 50  # Total available amount to be bid

        for i in range(4):
            playerss[i] = self.players[(self.rounds_played + i) % 4]
        self.players = playerss[:]

        for player in self.players:
            decision, bid = player.predict(self.scoreboard, current_bids)
            if not decision:
                print(f'{player.name} declines the offer')
                bid = 0
                declines += 1
            else:
                if bid > total_purse:
                    bid = total_purse  # Adjust bid to not exceed the remaining purse
                total_purse -= bid

            current_bids.append((player.name, bid))

        self.scoreboard.append(current_bids)
        self.rounds_played += 1
        self.evaluate_round(current_bids, declines)

    def evaluate_round(self, bids, declines):
        max_bid = sorted(bids, key=lambda x: x[1])[3]
        sec = sorted(bids, key=lambda x: x[1])[2]

        if declines >= len(self.players) - 2:
            for player_name, bid in bids:
                if bid == max_bid and bid > 0:
                    index = next(i for i, player in enumerate(self.players) if player.name == player_name)
                    self.curr_scores[index] -= 10
                    print(f"{player_name} gets -10 points")
                if bid == sec and bid > 0 and declines != 3:
                    index = next(i for i, player in enumerate(self.players) if player.name == player_name)
                    self.curr_scores[index] += 5
                    print(f"{player_name} gets +5 points")
        else:
            for player_name, bid in bids:
                if bid > 0:
                    index = next(i for i, player in enumerate(self.players) if player.name == player_name)
                    self.curr_scores[index] += bid
                    print(f"{player_name} gets exactly what they bid: {bid} points")

    def start_game(self, rounds):
        for r in range(rounds):
            self.rounds_played = r
            self.play_round()
