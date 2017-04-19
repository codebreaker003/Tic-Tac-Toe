#! /usr/bin/env python3.5
from tkinter import *
from random import choice
from time import sleep

root = Tk()
root.title("TIC-TAC-TOE")
root.resizable(width=False,height=False)
root.geometry("800x800")
root.configure(background='white')
b10=Button(root,text="EXIT",command=lambda:root.destroy(),bg='#FF2400',fg="white",padx=35,pady=15)
b10.place(x=350,y=730)
play = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = []
eco = []
masterl=Label(text="TIC-TAC-TOE",font="Helvetica 42 bold",fg="royal blue",bg="white")
masterl.place(x=220,y=20)
def check():
    if 9 in player and 5 in player and 1 in player:
        return "player"
    if 9 in player and 3 in player and 6 in player:
        return "player"
    if 9 in player and 8 in player and 7 in player:
        return "player"
    if 6 in player and 5 in player and 4 in player:
        return "player"
    if 2 in player and 5 in player and 8 in player:
        return "player"
    if 3 in player and 5 in player and 7 in player:
        return "player"
    if 3 in player and 2 in player and 1 in player:
        return "player"
    if 7 in player and 4 in player and 1 in player:
        return "player"
    if 9 in eco and 5 in eco and 1 in eco:
        return "eco"
    if 9 in eco and 3 in eco and 6 in eco:
        return "eco"
    if 2 in eco and 5 in eco and 8 in eco:
        return "eco"
    if 9 in eco and 8 in eco and 7 in eco:
        return "eco"
    if 6 in eco and 5 in eco and 4 in eco:
        return "eco"
    if 3 in eco and 5 in eco and 7 in eco:
        return "eco"
    if 3 in eco and 2 in eco and 1 in eco:
        return "eco"
    if 7 in eco and 4 in eco and 1 in eco:
        return "eco"


def write(num):
    pos = {1: [490, 490], 2: [290, 490], 3: [90, 490], 4: [490, 290], 5: [290, 290], 6: [90, 290], 7: [490, 90],
           8: [290, 90], 9: [90, 90]}
    if num == 9:
        player.append(9)
        play.remove(9)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=160, y=140)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")

            
        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")
                
            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")
    
                
    if num == 8:
        player.append(8)
        play.remove(8)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=360, y=140)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")


        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            
    if num == 7:
        player.append(7)
        play.remove(7)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=560, y=140)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")


        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            
    if num == 6:
        player.append(6)
        play.remove(6)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=160, y=340)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")


        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            
    if num == 5:
        player.append(5)
        play.remove(5)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=360, y=340)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")


        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            
    if num == 4:
        player.append(4)
        play.remove(4)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=560, y=340)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")


        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            
    if num == 3:
        player.append(3)
        play.remove(3)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=160, y=540)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")


        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")
            
    if num == 2:
        player.append(2)
        play.remove(2)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=360, y=540)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")

        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

            
    if num == 1:
        player.append(1)
        play.remove(1)
        v = Label(root, text="X", fg="green", bg="black", font="Helvetica 72 bold")
        v.place(x=560, y=540)
        c = check()
        if c == "player":
            v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")
        elif c == "eco":
            v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                       font="Helvetica 22 bold");
            v3.place(x=150, y=400)
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            b5.config(state="disabled")
            b6.config(state="disabled")
            b7.config(state="disabled")
            b8.config(state="disabled")
            b9.config(state="disabled")

        else:
            if play:
                comp = choice(play)
                play.remove(comp)
                x = pos[comp][0]
                y = pos[comp][1]
                v1 = Label(root, text="O", fg="white", bg="black", font="Helvetica 72 bold");
                v1.place(x=x + 70, y=y + 50)
                eco.append(comp)
            c = check()
            if c == "player":
                v3 = Label(root, text="PLAYER X WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")
            if c == "eco":
                v3 = Label(root, text="PLAYER O WINS!!! click close to exit", fg="yellow", bg="red",
                           font="Helvetica 22 bold");
                v3.place(x=150, y=400)
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                b5.config(state="disabled")
                b6.config(state="disabled")
                b7.config(state="disabled")
                b8.config(state="disabled")
                b9.config(state="disabled")

b1 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(1),highlightbackground="green",borderwidth=5)
b1.place(x=490, y=490)
b2 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(2),highlightbackground="green",borderwidth=5)
b2.place(x=290, y=490)
b3 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(3),highlightbackground="green",borderwidth=5)
b3.place(x=90, y=490)
b4 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(4),highlightbackground="green",borderwidth=5)
b4.place(x=490, y=290)
b5 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(5),highlightbackground="green",borderwidth=5)
b5.place(x=290, y=290)
b6 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(6),highlightbackground="green",borderwidth=5)
b6.place(x=90, y=290)
b7 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(7),highlightbackground="green",borderwidth=5)
b7.place(x=490, y=90)
b8 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(8),highlightbackground="green",borderwidth=5)
b8.place(x=290, y=90)
b9 = Button(root, padx=100, pady=100, bg="black", command=lambda: write(9),highlightbackground="green",borderwidth=5)
b9.place(x=90, y=90)
root.mainloop()