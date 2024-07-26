import random

def game():
    
    hand1 = ["rock", "paper", "scissors"]
    hand2 = ["rock", "paper", "scissors"]
    
    hand1 = random.choice(hand1)
    hand2 = random.choice(hand2)
    
    if hand1 == hand2:
        return(f"{player1} choose {hand1}, {player2} choose {hand2}: no one wins this round")
    
    elif hand1 == "rock" and hand2 == "scissors":
        return(f"{player1} choose {hand1}, {player2} choose {hand2}: {player1} wins this round")
        

player1 = input("Enter name: ")
player2 = input("Enter name: ")  

print(game())
