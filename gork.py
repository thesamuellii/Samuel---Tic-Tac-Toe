import random
import numpy as np
import os
class TicTacToe:
    def __init__(self, dimension):
        #Initializes the array and sets future parameters as part of self obj
        self.dimension = dimension
        self.array_dimension = dimension-1
        self.array = np.chararray((dimension,dimension), unicode = True)
        self.array[:] = "-"
    def array_filled(self):
        #Checks if array is filled, if it is it returns as true, else it returns as false.
        if ("-" in self.array):
            return False
        return True
    def array_check(self):
        #Logic statements for game win-cons (Returns as false if no win, true if there's a win)
        #Checking rows
        for i in range(self.dimension):
            win = True 
            if (''.join(set(self.array[i])) == self.player):
                win = True
                break
            else:
                win = False
        if win:
            return win
        #Checking columns
        for i in range(self.dimension):
            win = True
            S = self.array
            if (''.join(set(S[:,i])) == self.player):
                win = True
                break
            else:
                win = False
        if win:
            print("column win")
            return win
        #Checking diagonals
        win = True
        if (''.join(set(self.array.diagonal())) == self.player or ''.join(set(np.flip(self.array, 1).diagonal())) == self.player):
                win = True
        else:
            win = False
        if win:
            return win
        return False
    def assign_value_to_list(self):
        #Assigns element in array to current player and asks for value (X or O)
        while (True):
            value = input("Where do you want to move in the board? (ex. 1,3 for first row, third column.)")
            value = value.split(",")
            temp = value
            if (int(temp[0]) <= self.dimension and int(temp[1]) <= self.dimension):
                if (self.array[int(temp[0])-1,int(temp[1])-1] == "-"):
                    break
            print("Invalid position, please try again")
        self.x = int(value[0])
        self.y = int(value[1])
        self.array[self.x-1, self.y-1] = self.player
    def first_player(self):
        #Randomly selects a first player
        self.player = "X" if random.randint(0, 1) == 1 else "O"
    def print_array(self):
        #Prints array
        os.system('clear')
        print(str(self.array).replace(' [', '').replace('[', '').replace(']', ''))
    def pos_request(self):
        #Asks for user input as to where to move on the board as well as checking for invalid positions
        pos = input("Where do you want to move on the board? ex.(1, 3")
    def end_con_check(self, tie_con, win_con):
        #Checks if game is tied or won (True for win, False for tie, None(null) for no game end.))
        if (tie_con == True and win_con == False):
            return False
        if (win_con == True):
            return True
        return None
    def start_game(self):
        #Begins program and starts loop for game
        self.first_player()
        while (True):
                self.assign_value_to_list()
                tie_con = self.array_filled()
                win_con = self.array_check()
                self.print_array()
                end = self.end_con_check(tie_con, win_con)
                if (end == True):
                    print(self.player + " wins the game!")
                    break
                elif (end == False):
                    print("It's a tie!")
                    break
                self.player = "O" if self.player == "X" else "X"
#Asks for user input and initializes the class.
dimension = int(input("How large do you want the Tic-Tac-Toe board to be? "))
tt = TicTacToe(dimension)
tt.start_game()
