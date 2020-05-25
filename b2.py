from tkinter import *
import time
import random


class bong:    
    def __init__(seft, canvas, color, thanh, thanh1):
        seft.canvas = canvas
        seft.thanh = thanh;
        seft.thanh1 = thanh1;
        seft.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        seft.canvas.move(seft.id , 150, 200)
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)

        seft.x = start[0];
        seft.y = -1; seft.y = 1;
        seft.canvas_height =500;
        seft.canvas_width = 400;
        seft.over = False


    def cham(seft, P):
        P_thanh = seft.canvas.coords(seft.thanh.id)
        if P[0] >= P_thanh[0] and P[0] <= P_thanh[2]:
            if P[1] >= P_thanh[1] and P [3] <= P_thanh[3]:
                return True
        return False
    
    def cham1(seft, P):
        P1_thanh1 = seft.canvas.coords(seft.thanh1.id)
        if P[0] >= P1_thanh1[0] and P[0] <= P1_thanh1[2]:
            if P[1] >= P1_thanh1[1] and P[3] <=P1_thanh1[3]:
                return True
        return False

    def draw(seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
        P = seft.canvas.coords(seft.id)
        print(P)
        if P[1] <= 0:
          seft.y = 3
        if (P[3] >= seft.canvas_height)or(P[1]<=0):
            seft.over = True
        if (seft.cham(P) == True):
            seft.y = -3;
        if(seft.cham1(P) == True):
            seft.y = 3;
        if P[0] <= 0:
            seft.x = 3;
        if P[2] >= seft.canvas_width:
            seft.x = -3;
  
class thanh:
    def __init__(seft, canvas, color):
        seft.canvas = canvas
        seft.id = canvas.create_rectangle(0, 0, 100, 20, fill=color)
        seft.canvas.move(seft.id, 160, 480)
        seft.canvas.bind_all(' <KeyPress-Left>', seft.trai)
        seft.canvas.bind_all(' <KeyPress-Right>', seft.phai)
        seft.x = 0;
        seft.y = 0;
    def draw (seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
    def trai(seft, event):
        seft.x = -2;
    def phai(seft, event):
        seft.x = 2;

class thanh1:
    def __init__(seft, canvas, color):
        seft.canvas = canvas
        seft.id = canvas.create_rectangle(0, 0, 100, 20, fill=color)
        seft.canvas.move(seft.id, 150, 0)
        seft.canvas.bind_all(' <KeyPress-1>', seft.trai)
        seft.canvas.bind_all(' <KeyPress-2>', seft.phai)
        seft.x = 1;
        seft.y = 0;
    def draw (seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
    def trai(seft, event):
        seft.x = -2;
    def phai(seft, event):
        seft.x = 2;
        
tk = Tk()
tk.title("PIN BALL")
tk.resizable(1, 1)
can= Canvas(tk, width=400, height = 500)
can.pack()
thanh = thanh(can, "red")
thanh1 = thanh1(can, "red")
bong = bong(can,"yellow", thanh, thanh1)


while 1:
    if bong.over != True:
        bong.draw()
        thanh.draw()
        thanh1.draw()
        tk.update_idletasks()
        tk.update ()
        time.sleep(0.01)
    else:
        break;
print ("Game Over")




