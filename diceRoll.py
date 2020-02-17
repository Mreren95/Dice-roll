import random


def main() :
    Player1= 0
    Player1wins= 0
    Player2= 0
    Player2wins = 0
    rounds=1
#can change name of player easily but make sure you go and chnage it below so everything matches 
    
    while rounds != 11:
        print("Round" + str(rounds))
        Player1 = dice_roll()
        Player2 = dice_roll()
        print("Player 1 Roll: " + str(Player1))
        print("Player 2 Roll: " + str(Player2))
        
        
        if Player1 == Player2:
            print("Draw!!")
        elif Player1 > Player2:
            Player1wins = Player1wins + 1
            print("Player 1 Wins!!")
            
        else:
                Player2wins = Player2wins + 1
                print("Player 2 Wins!!")
                
            
        
                
        
        rounds = rounds + 1

    if Player1wins == Player2wins:
        print("Draw!!")
    elif Player1wins > Player2wins:
        print("Player 1 Wins!!")
        
    else: 
            print("Player 2 Wins!!")
            

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()
