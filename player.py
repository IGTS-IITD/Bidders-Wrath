class Player:
    def __init__(self, name, predict_func):
        self.name = name
        self.predict_func = predict_func
        
    def predict(self, scoreboard, previous_players):
        return self.predict_func(scoreboard, previous_players)
