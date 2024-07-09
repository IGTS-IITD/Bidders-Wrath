class RandomPlayer:
  def __init__(self):
    self.name = 'Demo Player'
    self.score = 0

  def add_score(self, score):
    self.score += score

  def bid(self, purse, current_bids):
    import random
    return random.randint(-10, 10)
  def round_result(self, my_index,  bids, results):
    self.add_score(results[my_index-1])