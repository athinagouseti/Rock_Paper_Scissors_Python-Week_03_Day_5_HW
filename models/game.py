class Game:

    def __init__(self):
        pass


    def determine_game(self, player_1, player_2):
        if player_1.choice == player_2.choice:
            winner = None
        else:
            choice = [player_1.choice, player_2.choice]
            if choice == ["rock", "paper"]:
                winner = player_2
            elif choice ==["rock", "scissors"]:   
                winner = player_1
            elif choice == ["paper", "scissors"]:
                winner = player_2 
            elif choice == ["paper", "rock"]:
                winner = player_2
            elif choice == ["scissors", "rock"]:
                winner = player_2
            elif choice == ["scissors", "paper"]:
                winner = player_1
        return winner
        
