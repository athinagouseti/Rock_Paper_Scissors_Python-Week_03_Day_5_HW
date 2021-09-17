class Game:

    def __init__(self, player_choice, computer_choice):
        self.player_choice = player_choice
        self.computer_choice = computer_choice


    def determine_game(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            winner = None
        else:
            choice = [player_choice, computer_choice]
            if choice == ["rock", "paper"]:
                winner = "paper"
            elif choice ==["rock", "scissors"]:   
                winner = "rock"
            elif choice == ["paper", "scissors"]:
                winner = "scissors" 
        return winner
        
