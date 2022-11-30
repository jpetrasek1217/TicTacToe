#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
#board = ["-","-","-",
  #       "-","-","-",
 #        "-","-","-"]
#play = True

def display_board():
    print(board[0]," | ",board[1]," | ",board[2])
    print("-------------")
    print(board[3]," | ",board[4]," | ",board[5])
    print("-------------")
    print(board[6]," | ",board[7]," | ",board[8])

def get_user_move(): 
    while True:
        user_move = int(input("What position would you like to play? (1-9)"))
        if user_move > 9:
            continue
        else:
            break
    while board[user_move - 1] != "-":
        user_move = int(input("What position would you like to play? (1-9)"))
        if board[user_move - 1] == "-":
            break
    board[user_move - 1] = "X"


def get_opponent_move():
    for p in range(3):
        check = []
        for letter1 in range(3*p, 3+3*p):
            check.append(board[letter1])
        if check.count("O")==2 and check.count("-")==1:
            for letter2 in range(3*p, 3+3*p):
                if board[letter2] == "-":
                    board[letter2] = "O"
                    return board
        elif check.count("X")==2 and check.count("-")==1:
            for letter3 in range(3*p, 3+3*p):
                if board[letter3] == "-":
                    board[letter3] = "O"
                    return board
    for q in range(3):
        check = []
        for letter4 in range(q, 9, 3):
            check.append(board[letter4])
        if check.count("O")==2 and check.count("-")==1:
            for letter4 in range(q, 9, 3):
                if board[letter4] == "-":
                    board[letter4] = "O"
                    return board
        elif check.count("X")==2 and check.count("-")==1:
            for letter4 in range(q, 9, 3):
                if board[letter4] == "-":
                    board[letter4] = "O"
                    return board
    for r in range(2):
        check = []
        for s in range(0+2*r, 9-2*r, 4-2*r):
            check.append(board[s])
        if check.count("O")==2 and check.count("-")==1:
            for letter5 in range(0+2*r, 9-2*r, 4-2*r):
                if board[letter5] == "-":
                    board[letter5] = "O"
                    return board
        elif check.count("X")==2 and check.count("-")==1:
            for letter5 in range(0+2*r, 9-2*r, 4-2*r):
                if board[letter5] == "-":
                    board[letter5] = "O"
                    return board
    opponent_move = random.randint(0,8)
    while board[opponent_move] != "-":
        opponent_move = random.randint(0,8)
        if board[opponent_move] == "-":
            break
    board[opponent_move] = "O"


def check_win():
    global wins
    global loss
    for i in range(3):
        check = []        
        for j in range(3*i, 3+3*i):
            check.append(board[j])
        if check.count("X")==3:
            print("You win!")
            wins += 1
            play = False
            return play
        elif check.count("O")==3:
            print("You lose...")
            loss += 1
            play = False
            return play
        else:
            check.clear()
            play = True
    for k in range(3):
        check = []
        for l in range(k, 9, 3):
            check.append(board[l])
        if check.count("X")==3:
            print("You win!")
            wins +=1
            play = False
            return play
        elif check.count("O")==3:
            print("You lose...")
            loss +=1
            play = False
            return play
        else:
            check.clear()
            play = True
    for m in range(2):
        check = []
        for n in range(0+2*m, 9-2*m, 4-2*m):
            check.append(board[n])
        if check.count("X")==3:
            print("You win!")
            wins += 1
            play = False
            return play
        elif check.count("O")==3:
            print("You lose...")
            loss += 1
            play = False
            return play
        else:
            check.clear()
            play = True
    return play

def check_tie():
    if board.count("-") > 0:
        play = True
    else:
        print("It's a Tie!")
        play = False
    return play
    
def main():
    global board
    global play
    global wins
    global loss
    wins = 0
    loss = 0
    while True:
        board = ["-","-","-","-","-","-","-","-","-"]
        play = True
        while play==True:
            display_board()
            get_user_move()
            if check_win() == False:
                display_board()
                break
            if check_tie() == False:
                display_board()
                break
            get_opponent_move()
            if check_win() == False:
                display_board()
                break
            if check_tie() == False:
                display_board()
                break
        print("Score:", wins, "-", loss)
        again = input("Play again? (y/n) ")
        if again == "y":
            continue
        elif again == "n":
            break
        else:
            while again != "y" or again != "n":
                again = input("Play again? (y/n) ")
                if again == "y":
                    break
                elif again == "n":
                    break
            if again == "y":
                continue
            if again =="n":
                break
main()


# In[ ]:




