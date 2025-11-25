#////////////////// FINAL PROJECT \\\\\\\\\\\\\\\\\\\\\\\\\\\
import random
from termcolor import colored,cprint
size = 3
def make_board(size):
    # create board using list of size (n x n)
    return [[" " for _ in range(size)] for _ in range(size)]

def print_board(board):
    #function to print the board
    
    # print colums
    print("\n    ",end="")
    #print colums numbers
    for i in range(size):
        print(i+1,end="   ")
    print()
    
    # print the dviding lines
    line = "  " + "-" * (size * 4 + 1)
    print(line)
    
    # print row
    for r in range(size):
         #print row numbers
        print(f"{r+1} | ",end="")
        print(" | ".join(board[r]),end=" |\n")
        print(line)
    print()


def player_move(board, symbol):
    while True:
        # get player's position choice
        cprint(f"\t////////// PLAYER",end="",attrs=["bold"])
        cprint(f" {symbol}","blue",attrs=["bold"],end="")
        cprint(" //////////",attrs=["bold"])   
        move = input(f"Enter a two numbers (x,y) from 1 to {size} :\n").replace(" ","")
        try:    
            x_str,y_str =  (move.split(","))
        except:
            cprint("Provide a valid format! Two numbers seperated by a comma: x,y ","yellow")
            continue
        #convert string to int
        x = int(x_str)
        y = int(y_str)
        # make sure it's within the right range (1-size) of the board
        if x < 1 or x > size or  y < 1 or y > size:
            cprint("Please provide two numbers between 1 and {size}.\n","yellow")
            continue
        
        # convert to zero index
        x -= 1
        y -= 1

        # check if the spot is free
        if board[x][y] != " ":
            cprint(f"The spot ({[x+1]},{[y+1]})  is taken!","red")
            continue

        # else place player symbol
        else:
            board[x][y] = colored(symbol,"blue")
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
    cprint("\t////////// Computer Thinking //////////","green",attrs=["bold"])
    x,y = random.choice(empty_space(board))
    cprint(f"\t\tComputer Plays ... ({x},{y})","green")
    board[x][y] = colored(symbol, "light_green")

    
def check_win(board):

 #///// check horizontal win conditions \\\\\   
   
    #check top rows if empty
    for x in range(size):
        first = board[x][0]
        if first == " ":
            continue

        match = True
        # check all cells  in this row to match first's symbol
        for y in range(size):
            if board[x][y] != first:
                match = False
                break
        if match:
            return True
        
 #///// check Vertical  win conditions \\\\\           
     
     #check top colums if empty
    for y in range(size):
        first = board[0][y]
        if first == " ":
            continue

        match = True
        # check all cells in this colum to match the first's symbol
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
        computer = colored("O","green")
    elif player == "O":
        computer = colored("X","green") 
    # start the game with the player's turn
    turn = player

    while True:
        print_board(board)

        # player always makes the first move
        if turn == player:
            player_move(board,player)
        else:
            # check mode to determine if  player 2 or computer turn
            if mode == 1:
                 player_move(board, computer)          
            else:
               computer_move(board, computer)
        # check win conditions        
        if check_win(board):
            print_board(board)
            if turn == "X":
                cprint(f"\t////// Player ",attrs=["bold"],end="")
                cprint(f"{turn} ","blue",attrs=["bold"],end="")
                cprint("WINS! ////// ",attrs=["bold"])
            elif turn == "O":
                cprint(f"\t////// Player ",attrs=["bold"],end="")
                cprint(f"{turn} ","green",attrs=["bold"],end="")
                cprint("WINS! ////// ",attrs=["bold"])
            return
        # check for a Tie
        if not empty_space(board):
            print_board(board)
            cprint("\t Its a Tie!","magenta",attrs=["bold"])
            return
        
        # change turns
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X" 
        
def main():
    while True:
        try:
            cprint("\_____________ TIC TAC TOE _____________/\n","cyan", attrs=["bold"])
            mode = int(input("1) Player 1 v/s Player 2 \n2) Play against Computer  \nMODE: "))
            if mode not in(1,2):
                cprint("Please provide a correct mode 1 or 2 ","light_red")
                continue
        except ValueError:
            cprint("Please provide a correct mode 1 or 2 ","light_red")
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