from tkinter import *
from PIL import ImageTk, Image
import time

tk = Tk()
tk.title('Game')
tk.resizable(1, 1)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=600, height=500, highlightthickness=0)
canvas.pack()
my_image = PhotoImage(file='wow.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
tk.update()


width = 600
height = 500

class Game:
    def __init__(self):
        self.player = Player()

class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        pilImage = Image.open("andrew.png")
        image = ImageTk.PhotoImage(pilImage)
        self.id = canvas.create_image(50, 50, image=image)
        self.y = 100
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.started = False

    def turn_right(self,  event):
        self.x = 2

    def turn_left(self, event):
        self.x = -2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)



player = Player(canvas)
while 1:
    player.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)