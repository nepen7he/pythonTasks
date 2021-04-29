from tkinter import Tk, Frame, Label, Button, Text, Toplevel

class ClickCluckClowker:
    multiplier = 1
    clicks = 0
    flagforauto = False
    flagforfirst = True
    flagforsecond = True
    flagforthird = True
    flagforfourth = True
    mess = "Hello!"


    def get_plus(self):
        if self.clicks >= 100:
            self.clicks -= 100
            self.multiplier += 1
            self.mess = "Your multiplier have been updated"
            self.change_mes(self.mess)
        else:
            self.mess = "Sorry, not enough points"
            self.change_mes(self.mess)

    def autoclicker(self): #purchase
        if self.flagforauto == False:
            if self.clicks < 1500:
                self.mess = "Sorry, not enough points, autoclicker did not activated"
                self.change_mes(self.mess)
            else:
                self.clicks -= 1500
                flagforauto = True
                self.mess = "Autoclicker purchased! Click 'AUTO ON' to activate it."
                self.change_mes(self.mess)
        else:
            self.mess = "Autoclicker was already bought"
            self.change_mes(self.mess)


    def autoclick(self):
        if self.flagforauto:
            self.clicks += 1
            self.mainapp.click['text'] = self.clicks
            self.mainapp.after(1000, self.autoclick(self.mainapp, self.clicks, self.flagforauto))

    def __init__(self, mainapp):
        mainapp['bg'] = '#fafafa'
        mainapp.title('Simple Clicker')
        mainapp.geometry('500x400')
        mainapp.resizable(width=False, height=False)
        frame = Frame(mainapp, bg='pink4')
        frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
        self.click = Button(text='Click', width=7, height=3, font=20)
        self.click.place(relx=0.522, rely=0.3)
        self.click.config(command=self.change_cmd)
        self.autoclickpur = Button(text='Buy Autoclicker (for 1500 clicks)', width=25, height=2, font=20)
        self.autoclickpur.place(relx=0.15, rely=0.625)
        self.autoclickpur.config(command=self.autoclicker)

        self.auto = Button(text='AUTO ON', width=8, height=2, font=20)
        self.auto.place(relx=0.68, rely=0.15)
        self.auto.config(command=self.autoclick)

        self.achievement = Button(text='Get Achievements', width=25, height=2, font=20)
        self.achievement.place(relx=0.15, rely=0.505)
        self.achievement.config(command=self.get_achievement)

        self.mult = Button(text='Get +1 multiplier for each 100 clicks', width=30, height=2, font=20)
        self.mult.place(relx=0.15, rely=0.725)
        self.mult.config(command=self.get_plus)

        self.showclicks = Label(text='Clicks counter:', bg='light goldenrod', font=20, width=20, height=2)
        self.showclicks.place(relx=0.15, rely=0.33)

        self.ach_message = Label(width=50, font=20, bg='grey', text="You can get achievements for 100/400/1500/3000 points")
        self.ach_message.pack()

        self.message = Label(width=50, font=20, bg='grey', text="Hello!")
        self.message.pack()

    def change_mes(self, mess):
        self.message.config(text=mess)


    def change_cmd(self):
        self.clicks += (1 * self.multiplier)
        self.click['text'] = self.clicks

    def get_achievement(self):
        if self.clicks >= 100 and self.flagforfirst == True:
            self.mess = 'Achievement unlocked: Beginner. Bonus: +50 points'
            self.change_mes(self.mess)
            self.clicks += 50
            self.click['text'] = self.clicks
            self.flagforfirst = False

        elif self.clicks >= 400 and self.flagforsecond == True:
            self.mess = 'Achievement unlocked: Advanced. Bonus: +100 points'
            self.change_mes(self.mess)
            self.clicks += 100
            self.click['text'] = self.clicks
            self.flagforsecond = False

        elif self.clicks >= 1500 and self.flagforthird == True:
            self.mess = 'Achievement unlocked: Professional. Bonus: +200 points'
            self.change_mes(self.mess)
            self.clicks += 200
            self.click['text'] = self.clicks
            self.flagforthird = False


        elif self.clicks >= 3000 and self.flagforfourth == True:
            self.mess = 'Achievement unlocked: Idler. Bonus points: +1'
            self.change_mes(self.mess)
            self.clicks = + 1
            self.click['text'] = self.clicks
            self.flagforfourth = False

        else:
            self.mess = "You didn't collect enough points for any achievement"
            self.change_mes(self.mess)


if __name__ == '__main__':
    mainapp = Tk()
    ClickCluckClowker = ClickCluckClowker(mainapp)
    mainapp.mainloop()