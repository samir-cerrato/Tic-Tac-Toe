#!/usr/bin/python3
#
# Wesleyan University
# COMP 332, Computer Networks
# Homework 1: Tic-tac-toe game


#Samir Cerrato
#Feb. 4, 2024

import random

class Board():
    """
    TicTacToe game board
    """

    def __init__(self, n):
        self.n = n
        self.grid = [[' ' for _ in range(n)] for _ in range(n)]

    def display(self):
        for row in self.grid:
            print("|".join(row))
            print("-" * (self.n * 2 - 1))

class TicTacToe():
    """
    TicTacToe game
    """

    def __init__(self, n):
        self.n = n
        self.board = Board(n)

    def display(self):
        self.board.display()
    
    def make_move(self, player, row, col):
        if self.board.grid[row][col] == ' ':
            self.board.grid[row][col] = player
            return True
        else:
            print("Invalid move. Cell already taken.")
            return False
    
    def check_winner(self, player, row, col):
        if all(cell == player for cell in self.board.grid[row]):
            return True

        if all(self.board.grid[i][col] == player for i in range(self.n)):
            return True

        if row == col and all(self.board.grid[i][i] == player for i in range(self.n)):
            return True

        if row + col == self.n - 1 and all(self.board.grid[i][self.n - 1 - i] == player for i in range(self.n)):
            return True

        return False

class Server():
    """
    Server for TicTacToe game
    """

    def __init__(self):
        print('')

    def play(self):
        print("==================")
        print("| TicTacToe Game |")
        print("==================\n")

        while True:
            try:
                n = int(input("Enter the number of rows in TicTacToe board: "))
                if n < 3:
                    print("Please enter a number greater than or equal to 3.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        game = TicTacToe(n)

        players = ['X', 'O']
        current_player = random.choice(players)

        while True:
            print("Player", current_player, "'s turn:")
            #game.display()

            if current_player == 'X':
                while True:
                    try:
                        row = int(input(f"Enter the row (0 to {n-1}): "))
                        if 0 <= row < n:
                            break
                        else:
                            print(f"Invalid input. Row must be in the range 0 to {n - 1}.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                while True:
                    try:
                        col = int(input(f"Enter the column (0 to {n-1}): "))
                        if 0 <= col < n:
                            break
                        else:
                            print(f"Invalid input. Column must be in the range 0 to {n - 1}.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                
                if game.make_move(current_player, row, col):
                    game.display()
                    if game.check_winner(current_player, row, col):
                        print(f"Player {current_player} wins!")
                        break
                    else:
                        current_player = 'O'
                else:
                    continue

            else:
                available_moves = [(i, j) for i in range(n) for j in range(n) if game.board.grid[i][j] == ' ']
                if available_moves:
                    row, col = random.choice(available_moves)
                    if game.make_move(current_player, row, col):
                        game.display()
                        if game.check_winner(current_player, row, col):
                            print(f"Player {current_player} wins!")
                            break
                        else:
                            current_player = 'X'
                else:
                    game.display()
                    print("It's a tie!")
                    break



def main():
    s = Server()
    s.play()

if __name__ == '__main__':
    main()
