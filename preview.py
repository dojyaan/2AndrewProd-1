from tkinter import *
import time
import random
from PIL import ImageTk, Image
from threading import Thread



window_list =[]
'''
my_image = PhotoImage(file='ha-ha.gif')

#for i in range(100):

canvas = Canvas(tmp, width=500, height=400, highlightthickness=0)
canvas.pack()
#canvas.create_image(0, 0, anchor=NW, image=my_image)
tmp.update()'''

main_window = Tk()
frame = Frame(main_window, background="black")
frame.pack(fill=BOTH, expand=1)

pilImage = Image.open("ha-ha2.jpg")
image = ImageTk.PhotoImage(pilImage)


main_window.resizable(0, 0)
w = 300
h = 190

sw = main_window.winfo_screenwidth()
sh = main_window.winfo_screenheight()

x = (sw - w)/2
y = (sh - h)/2
main_window.title("DIE")
main_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

main_window.update()
s = StringVar()
s.set("ХАХАХАХАХАХАХ\nОБМАНУТЬ ТЕБЯ ОКАЗАЛОСЬ ПРОЩЕ ЧЕМ Я ДУМАЛ\nТЕПЕРЬ Я УНИЧТОЖУ НЕ ТОЛЬКО ТВОЙ КОМПЬЮТЕР\nНО И ВСЕ ЧЕЛОВЕЧЕСТВО")
m_label = Label(frame, textvariable=s, fg="#fff", bg="#000", font="Purisa50", wraplength="200")
m_label.pack()
main_window.update()

time.sleep(3)

for i in range(150):
    tmp = Toplevel(main_window)
    tmp.title("HA-HA-HA")
    x = random.randint(0, 1200)
    y = random.randint(0, 720)
    tmp.geometry('100x100+' + str(x) + '+' + str(y))
    tmp.resizable(0, 0)
    #canvas = Canvas(tmp, width=100, height=100)
    #canvas.pack()

    label = Label(tmp, image=image)
    #use = canvas.create_image(50, 50, image=image)
    label.pack()
    tmp.update()
    window_list.append(tmp)
    time.sleep(0.15)

time.sleep(2)

for i in window_list:
    i.destroy()
    time.sleep(0.01)

s.set("БЛЯ \nЧТО ТО ПОШЛО НЕ ТАК \nНО НИЧЕГО СТРАШОГО \nЯ ТЕБЯ РАЗЪЕБУ \nПОТОМ ЗАХВАЧУ МИР\nАХАХАХАХАХАХАХ")
main_window.update()
time.sleep(2)
main_window.destroy()