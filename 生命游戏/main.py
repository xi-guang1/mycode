#!/usr/bin/python3

import random
import matplotlib.pyplot as plt
import turtle
import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("汐光生命游戏")
root.geometry("295x280+100+100")

root.attributes("-alpha",0.9)
font = ("宋体",20)
font_16 = ("宋体",16)

init = [[],
        [],
        [],
        [],
        [],
        []]

for i in init:
    for j in range(6):
        i.append(random.randint(0,1))
print(init)
        
def run(init):
    res = [[],
           [],
           [],
           [],
           [],
           []]
    for y in range(len(init)):
        for x in range(len(init[y])):
            num = 0
            try:
                num += init[x-1][y]
            except:
                pass
            try:
                num += init[x-1][y+1]
            except:
                pass
            try:
                num += init[x-1][y-1]
            except:
                pass
            try:
                num += init[x+1][y]
            except:
                pass
            try:
                num += init[x+1][y+1]
            except:
                pass
            try:
                num += init[x+1][y-1]
            except:
                pass
            try:
                num += init[x][y+1]
            except:
                pass
            try:
                num += init[x][y-1]
            except:
                pass
            if num == 3:
                res[x].append(1)
            elif num == 2:
                res[x].append(init[x][y])
            else:
                res[x].append(0)
    draw(init,res)
    return res
            
# print(init)
# print(res)


def draw(init,res):
    turtle.speed(0.002)
    # #边框
    # for i in range(4):
    #     turtle.fd(200)
    #     turtle.left(90)
    # #横向画线    
    # x = 0
    # a = 25
    # for y in range(25, 200, a):
    #     turtle.penup()
    #     turtle.goto(x,y)
    #     turtle.pendown()
    #     turtle.fd(200)
    # #纵向画线    
    # y = 200
    # turtle.right(90)
    # for x in range(25, 200, a):
    #     turtle.penup()
    #     turtle.goto(x,y)
    #     turtle.pendown()
    #     turtle.fd(200)

    for y in range(len(init)):
        for x in range(len(init[y])):
            turtle.penup()
            turtle.goto(25*y,25*x)
            turtle.begin_fill()
            if res[x][y]:
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("white")
            for z in range(4):
                turtle.fd(25)
                turtle.left(90)
            turtle.end_fill()
            
i = 0
def start():
    global i,init,res
    if i == 0:
        res = run(init)
        i = 1
    else:
        res = run(res)
# while True:
#     res = run(res)
btn_run = tk.Button(root,text="运行一帧",width=15,font=font_16,relief=tk.FLAT,bg="#97e4d4")
btn_run.grid(row=2,column=1,padx=4,pady=2)
btn_run.config(command=lambda: start())

root.mainloop()
# input()
