
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title = "Tic Tac Toe"
        self.current_player = "X"
        self.cur_go = 0

        self.buttons = [[None, None, None] for x in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text="", width=10, height=4, command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        print(self.cur_go)
        self.cur_go += 1
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.cur_go==9:
                messagebox.showinfo("Draw", "The game is a draw!")
                self.reset_board()
            else:
                self.toggle_player()


    def toggle_player(self):
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        columnsums = [0, 0, 0]
        for row in self.buttons:
            sum_row = sum([1 if x["text"]== "X" else 2 if x["text"]=="O" else 100 for x in row])
            if sum_row==3 or sum_row==6:
                return True
            for x, item in enumerate(row):
                columnsums[x]+= 1 if item["text"]=="X" else 2 if item["text"]=="O" else 100
        if 6 in columnsums or 3 in columnsums:
            return True

        sum_first_diagonal = sum([(1 if self.buttons[i][i]["text"]=="X" else 2 if self.buttons[i][i]["text"]=="O" else 100) for i in range(3)])
        sum_second_diagonal = sum([(1 if self.buttons[i][2-i]["text"]=="X" else 2 if self.buttons[i][2-i]["text"]=="O" else 100) for i in range(3)])

        if sum_first_diagonal in [3,6] or sum_second_diagonal in [3,6]:
            return True

        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"
        self.cur_go=0



if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
