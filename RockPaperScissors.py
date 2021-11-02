import random
import time
import sys, select

def play():
    poss = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    while player_score < 5 and computer_score < 5:
        #build up
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        
        computer = random.randint(1,3)

        #
        #i, o, e = select.select( [sys.stdin], [], [], 2 )
        #if (i):
        #    player = sys.stdin.readline().strip()
        #else:
        #    continue
        player = input()
        print("player", player)
        if player == "r":
            if computer == 2:
                computer_score+=1
            if computer == 3:
                player_score+=1
        elif player == "p":
            if computer == 1:
                player_score+=1
            if computer == 3:
                computer_score+=1
        elif player == "s":
            if computer == 1:
                computer_score+=1
            if computer == 2:
                player_score+=1
        else:
            print("Input not valid")
            
        print(poss[computer-1])
        print("computer ", computer_score)
        print("You ", player_score)
                
        
        
        
    if player_score == 5:
        print("You won!")

    if computer_score == 5:
        print("You lost!")


play()
