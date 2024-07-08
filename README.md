# AlgoGame

AlgoBet Game
Overview
AlgoBet is a competitive bidding game designed to test different predictive strategies in a simulated environment. Players implement their predictive functions, which determine their actions based on the game's history and the decisions of other players.

Game Rules
Participation and Bidding
Each round, players submit their bids through a prediction function.
The prediction function returns a tuple (Bool, int), where:
Bool: A boolean indicating whether the player chooses to participate in the round (True for participating, False to decline).
int: The bid amount, which is considered only if Bool is True. If Bool is False, the bid amount is automatically set to 0.
Scoring
If all players except one decline (i.e., do not participate), the lone participant receives -10 points, second highest receives + 5.
If two or more players have the highest bid, those players are penalized by removing them from the bid consideration for that round.
If only one player or no player declines, each participating player receives points equal to their bid.
Game End
The game can be set to run for a predetermined number of rounds. After all rounds are completed, the player with the highest score is declared the winner.
Sample Strategies
1. Conservative Bidder
This strategy involves bidding conservatively, often increasing the bid slightly if the previous round's highest bid was low.

2. Aggressive Bidder
Starts with a high bid and decreases it if unsuccessful in previous rounds, aiming to intimidate other players into declining.

3. Random Bidder
Offers random bids within a specified range, making it difficult for other players to predict their actions.

4. Tactical Bidder
Analyzes the average bids of previous rounds and adjusts their bid based on this data, looking to optimize their score without overcommitting.

5. Incremental Bidder
Gradually increases their bid each round until a threshold is reached, then resets to a lower bid, aiming for consistent but cautious participation.

Installation
To run the game, clone this repository and ensure you have Python installed. Navigate to the directory containing the game files and run:

python main.py


Contributions to AlgoBet are welcome. Please feel free to fork the repository, make changes, and submit pull requests. You can also open issues for bugs you've found or features you think would be beneficial.
