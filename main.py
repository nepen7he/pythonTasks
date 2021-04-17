import keyboard
from tkinter import *


mainapp = Tk()
multiplier = 1
clicks = 0
flagforauto = False
flagforfirst = True
flagforsecond = True
flagforthird = True
flagforfourth = True


def change_mes():
    global mess
    global message
    message.config(text=mess)


def change_cmd():
    global clicks
    global multiplier
    clicks += (1 * multiplier)
    click['text'] = clicks

def getachievement():
    global clicks
    global mess
    global flagforfirst
    global flagforsecond
    global flagforthird
    global flagforfourth

    if clicks >= 100 and flagforfirst == True:
        mess = 'Achievement unlocked: Beginner. Bonus: +50 points'
        change_mes()
        clicks += 50
        click['text'] = clicks
        flagforfirst = False

    elif clicks >= 400 and flagforsecond == True:
        mess = 'Achievement unlocked: Advanced. Bonus: +100 points'
        change_mes()
        clicks += 100
        click['text'] = clicks
        flagforsecond = False

    elif clicks >= 1500 and flagforthird == True:
        mess = 'Achievement unlocked: Professional. Bonus: +200 points'
        change_mes()
        clicks += 200
        click['text'] = clicks
        flagforthird = False


    elif clicks >= 3000 and flagforfourth == True:
        mess = 'Achievement unlocked: Idler. Bonus points: +1'
        change_mes()
        clicks = + 1
        click['text'] = clicks
        flagforfourth = False

    else:
        mess = "You didn't collect enough points for any achievement"
        change_mes()


def getplus():
    global multiplier
    global mess
    global clicks
    if clicks >= 100:
        clicks -= 100
        multiplier += 1
        mess = "Your multiplier have been updated"
        change_mes()
    else:
        mess = "Sorry, not enough points"
        change_mes()


def autoclicker(): #purchase
    global clicks
    global mess
    global flagforauto
    if flagforauto == False:
        if clicks < 1500:
            mess = "Sorry, not enough points, autoclicker did not activated"
            change_mes()
        else:
            clicks -= 1500
            flagforauto = True
            mess = "Autoclicker purchased! Click 'AUTO ON' to activate it."
            change_mes()
    else:
        mess = "Autoclicker was already bought"
        change_mes()


def autoclick():
    global mainapp
    global clicks
    global flagforauto
    if flagforauto:
        clicks += 1
        click['text'] = clicks
        mainapp.after(1000, autoclick)


mainapp['bg'] = '#fafafa'
mainapp.title('Simple Clicker')
mainapp.geometry('500x400')
mainapp.resizable(width=False, height=False)

frame = Frame(mainapp, bg='pink4')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
title = Label(frame, text = 'Click "left mouse button" to get points', bg='light goldenrod', font=20)
title.pack(expand=1, anchor=NW)

click = Button(text='Click', width=7, height=3, font=20)
click.place(relx=0.522, rely=0.3)
click.config(command=change_cmd)

autoclickpur = Button(text='Buy Autoclicker (for 1500 clicks)', width=25, height=2, font=20)
autoclickpur.place(relx=0.15, rely=0.625)
autoclickpur.config(command=autoclicker)

auto = Button(text='AUTO ON', width=8, height=2, font=20)
auto.place(relx=0.68, rely=0.15)
auto.config(command=autoclick)

achievement = Button(text = 'Get Achievements', width=25, height=2, font=20)
achievement.place(relx=0.15, rely=0.505)
achievement.config(command=getachievement)

mult = Button(text = 'Get +1 multiplier for each 100 clicks', width=30, height=2, font=20)
mult.place(relx=0.15, rely=0.725)
mult.config(command=getplus)

showclicks = Label(text='Clicks counter:', bg='light goldenrod', font=20, width=20, height=2)
showclicks.place(relx=0.15, rely=0.33)

message = Label(width=50, font=20, bg='grey', text="Hello!")
mess = Label(width=50, font=20, bg='grey', text="Hello!")
message.pack()

ach_message = Label(width=50, font=20, bg='grey', text="You can get achievements for 100/400/1500/3000 points")
ach_message.pack()

mainapp.mainloop()