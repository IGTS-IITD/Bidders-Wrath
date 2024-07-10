class RandomPlayer:
  def __init__(self):
    self.name = 'Random Player'
    self.score = 0
    self.data = []

  def bid(self, purse, current_bids, totalscores):
    import random
    return random.randint(-1, 10)
  
  def round_result(self, my_chance, bids, results):
    self.score += results[my_chance-1]
    if (my_chance==3):
      self.data.append(results[my_chance-1])

class Aggressive:
  def __init__(self):
    self.name = 'Aggressive Player'
    self.score = 0

  def bid(self, purse, bids, totalscores):
    if (purse<20): 
      return -1
    if len(bids) == 0:
      return 30
    if len(bids) == 1:
      return purse-5
    if len(bids) == 2:
      return purse
    if len(bids) == 3:
      return purse
    return -1
  
  def round_result(self, my_chance, bids, results):
    self.score += results[my_chance-1]
    
class ConservativePlayer:
    def __init__(self):
        self.name = 'Conservative Player'
        self.score = 0

    def bid(self, purse, current_bids, totalscores):
        if purse > 40:
            return 5
        elif purse > 20:
            return 3
        else:
            return -1  # Decline if purse is too low

    def round_result(self, my_chance, bids, results):
        self.score += results[my_chance-1]

class AdaptivePlayer:
    def __init__(self):
        self.name = 'Adaptive Player'
        self.score = 0
        self.round_count = 0

    def bid(self, purse, current_bids, totalscores):
        self.round_count += 1
        if self.round_count % 10 == 0:
            return 40  # Every 10 rounds, bid high
        if purse > 30:
            return 15
        elif purse > 10:
            return 10
        else:
            return -1

    def round_result(self, my_chance, bids, results):
        self.score += results[my_chance-1]
        