from players import Me, RandomPlayer, Aggressive, AdaptivePlayer, ConservativePlayer, Sadist, Repeater

players = [Sadist(), Me(), AdaptivePlayer(), Aggressive()]

class Game:
    def __init__(self, players):
        self.rounds_played = 0
        self.players = [[player, 0] for player in players] # [player, score]

    def __repr__(self):
        leaderboard = sorted([[player[0].name, player[1]] for player in self.players], key=lambda x: x[1], reverse=True)
        return f'Leaderboard: {leaderboard}'
    
    def play_round(self):
        current_bids = []
        declines = 0
        purse = 50
        totalscores = [player[1] for player in self.players]
        print(f'Total Scores: {totalscores}')

        print(f'Round {self.rounds_played + 1}')

        for player in self.players:
            bid = player[0].bid(purse, current_bids, totalscores)
            print(f'{player[0].name} bids {bid}')
            if bid <= -1:
                bid = -1
                declines += 1
            else:
                if bid > purse:
                    bid = purse
                purse -= bid
            current_bids.append(bid)
        
        self.evaluate_round(current_bids, declines)

        self.rounds_played += 1
        self.players = self.players[1:] + self.players[:1]

    def evaluate_round(self, bids, declines):
        max_bid = max(bids)
        second_bid = sorted(bids, reverse=True)[1]
        results = [0]*4

        if declines >= 2:
            for i, bid in enumerate(bids):
                if bid == max_bid and bid >= 0: # if max = second, both get -10
                    results[i] = -10
                elif bid == second_bid and bid >= 0:
                    results[i] = 5
        else:
            for i, bid in enumerate(bids):
                if bid >= 0:
                    results[i] = bid

        for i, result in enumerate(results):
            self.players[i][1] += result

        for i in range(4):
            self.players[i][0].round_result(i+1, bids, results)

        print(f'Round results: {results}')

    def play_game(self, rounds):
        for _ in range(rounds):
            self.play_round()

start_game = Game(players)
start_game.play_game(200)
print(start_game)
