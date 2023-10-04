# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:30:31 2023

@author: Eeduardo
"""

import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
 
# sign variable to decide the turn of which player
sign = 0
 
# Creates an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]
 
# Check l(O/X) won the match or not
# according to the rules of the game
 
 
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
 
# Check if the player can push the button or not
 
 
def isfree(i, j):
    return board[i][j] == " "
  
 
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
 
# Create the GUI of game board for play along with another player
 
# Decide the next move of system
 
def pc():
    sec = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                sec.append([i, j])
                                    
    num = []
    i = 1
    j = 'O'
    Tabla = deepcopy(board)
    while(len(num) == 0 ):
        if i==1:
            s = [[0,0], [0,1], [0,2]]
        elif i==2:
            s = [[1,0], [1,1], [1,2]]
        elif i==3:
            s = [[2,0], [2,1], [2,2]]
        elif i==4:
            s = [[0,0], [0,1], [0,2]]
        elif i==5:
            s = [[1,0], [1,1], [1,2]]
        elif i==6:
            s = [[2,0],[2,1],[2,2]]
        elif i==7:
            s = [[0,0], [1,1], [2,2]]
        elif i==8:
            s = [[0,2], [1,1], [2,0]]
        elif i == 9 and j == 'O':
            j ='X'
            i =1;
            
        elif i == 9 and j == 'X':
            num = random.choice(sec)
            print(i)
        if (Tabla[s[0][0]][s[0][1]]==j and Tabla[s[1][0]][s[1][1]]==j and Tabla[s[2][0]][s[2][1]] == ' '):
            num = s[2];
        elif (Tabla[s[0][0]][s[0][1]]==j and Tabla[s[1][0]][s[1][1]]==' ' and Tabla[s[2][0]][s[2][1]] == j):
            num = s[1];
        elif (Tabla[s[0][0]][s[0][1]]==' ' and Tabla[s[1][0]][s[1][1]]==j and Tabla[s[2][0]][s[2][1]] == j):
            num = s[0];
        i = i + 1
        print(num)
    
    return num
 
# Configure text on button while playing with system
 
 
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        x = False
        box = messagebox.showinfo("Ganador", "El humano ganó el juego")
    elif winner(board, "O"):
        x = False
        box = messagebox.showinfo("Ganador", "Lo sentimos, un par de lines de codigo te ganaron.")
    elif(isfull()):
        x = False
        box = messagebox.showinfo("Empate", "Parece que no hay vida inteligente por aquí")
    if(x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)
 
# Create the GUI of game board for play along with system
 
 
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
 
# Initialize the game board to play with system
 
 
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Gato")
    l1 = Button(game_board, text="Jugador : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Coputadora : O",
                width=10, state=DISABLED)
 
    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)
 

 
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Gato")
    wpc = partial(withpc, menu)
 
    head = Button(menu, text="-----Juego del gato------",
                  activeforeground='red',
                  activebackground="yellow", bg="blue",
                  fg="yellow", width=500, font='summer', bd=5)
 
    B1 = Button(menu, text="Un jugador", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="blue",
                fg="yellow", width=500, font='summer', bd=5)
 
    head.pack(side='top')
    B1.pack(side='top')
    menu.mainloop()
 
 
# Call main function
if __name__ == '__main__':
    play()