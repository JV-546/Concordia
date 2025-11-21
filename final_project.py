#////////////////// FINAL PROJECT \\\\\\\\\\\\\\\\\\\\\\\\\\\
import random
size = 3
def make_board(size):
    #function the create board of any size (n x n)
    return [[" " for _ in range(size)] for _ in range(size)]

def print_board(board):
    #function to print the board
    # print colums
    print("\n    ",end="")
    for i in range(size):
        print(i+1,end="   ")
    print()
    # print the dviding lines
    line = "  " + "-" * (size * 4 + 1)
    print(line)
    # print row
    for r in range(size):
        print(f"{r+1} | ",end="")
        print(" | ".join(board[r]),end=" |\n")
        print(line)
    print()


def player_move(board, symbol):
    while True:
        # get player's position choice   
        move = input(f"Player {symbol}, enter a two numbers (x,y) from 1 to {size} : ").replace(" ","")
        try:    
            x_str,y_str =  (move.split(","))
        except:
            print("Provide a valid format! Two numbers seperated by a comma: x,y ")
            continue
        x = int(x_str)
        y = int(y_str)
        # make sure its within the right range 1 to the size of the board
        if x < 1 or x > size or  y < 1 or y > size:
            print("Please provide two numbers between 1 and {size}.")
            continue
        
        # convert to zero index
        x -=1
        y -=1

        # check if the spot is free
        if board[x][y] != " ":
            print("That spot is taken!")
            continue

        # else place player symbol
        else:
            board[x][y] = symbol
            break


def empty_space(board):
    #check empty spot the computer can play
    empty=[]
    for x in range (size):
        for y in range(size):
            if board[x][y] == " ":
                empty.append((x,y))
    return empty

def computer_move(board, symbol):
    print("computer places ...")
    x,y = random.choice(empty_space(board))
    board[x][y] = symbol

    
def check_win(board):
    #check horizontal lines
    for x in range(size):
        first = board[x][0]
        if first == " ":
            continue

        match = True
        # check all colums for this row
        for y in range(size):
            if board[x][y] != first:
                match = False
                break
        if match:
            return True
        
     #check vertical lines
        for y in range(size):
            first = board[0][y]
            if first == " ":
                continue

            match = True
            # check all colums for this row
            for x in range(size):
                if board[x][y] != first:
                    match = False
                    break
            if match:
                return True
    # if no one has won yet
    return False




def game(mode):
    # create the board at a given size
    board = make_board(size)
    #ask player for the symbole they wish to play as (X or O)
    while True:
        player = input("Choose you symbol X or O: ").upper() 
        if player in ("X","O"):
            break

    #assign the opposite symbol to the computer     
    if player == "X":
        computer = "O"
    elif player == "O":
        computer = "X" 
    # start the game with the player's turn
    turn = player

    while True:
        print_board(board)

        if turn == player:
            player_move(board,player)
        else:
            if mode == 1:
                 player_move(board, computer)          
            else:
               computer_move(board, computer)
                
        if check_win(board):
            print_board(board)
            print(f"{turn} WINS! ")
            return
        if not empty_space(board):
            print_board(board)
            print("Its a Tie! ")
            return
        
        # change turns
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X" 
        


def main():
    while True:
        try:
            mode = int(input("1) Player 1 v/s Player 2 \n2) Play against Computer  \nMODE: "))
            if mode not in(1,2):
                print("Please provide a correct mode 1 or 2")
                continue
        except ValueError:
            print("Please provide a correct mode 1 or 2")
            continue
        game(mode)
        while True:
            restart = input("Do you want to restart the game? (y/n)\n").lower()
            if restart in ("y", "n"):
                break
        if restart != "y":
            break
            

    
if __name__ == "__main__":
    main()