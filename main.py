from tkinter import *
from PIL import Image, ImageTk
import pandas as pd


class Example:
    def __init__(self):
        self.tb1 = 0
        self.tb2 = 0
        self.tb3 = 0
        self.tb4 = 0
        self.tb5 = 0
        self.tb6 = 0
        self.tb7 = 0
        self.tb8 = 0
        self.tb9 = 0
        self.tb10 = 0
        self.tb11 = 0
        self.tb12 = 0
        self.tb13 = 0
        self.tb14 = 0
        self.tb15 = 0
        self.tb16 = 0
        self.tb17 = 0
        self.tb18 = 0
        self.tb19 = 0
        self.tb20 = 0
        self.tb21 = 0
        self.tb22 = 0
        self.tb23 = 0
        self.tb24 = 0
        self.tb25 = 0
        self.tb26 = 0
        self.tb27 = 0
        self.tb28 = 0
        self.tb29 = 0
        self.tb30 = 0
        self.tb31 = 0
        self.tb32 = 0
        self.tb33 = 0
        self.tb34 = 0
        self.tb35 = 0
        master = Tk()
        master.title('Museum Statistic')
        self.info1 = Tk()
        self.info1.geometry('425x100')
        self.info1.withdraw()

        self.info2 = Tk()
        self.info2.geometry('425x100')
        self.info2.withdraw()

        self.info3 = Tk()
        self.info3.geometry('425x100')
        self.info3.withdraw()

        self.info4 = Tk()
        self.info4.geometry('425x100')
        self.info4.withdraw()

        self.info5 = Tk()
        self.info5.geometry('425x100')
        self.info5.withdraw()

        self.info6 = Tk()
        self.info6.geometry('425x100')
        self.info6.withdraw()

        self.info7 = Tk()
        self.info7.geometry('425x100')
        self.info7.withdraw()
        self.frame = Frame(master, relief=SUNKEN, borderwidth=1)
        self.frame.grid(row=10, column=10, sticky=NW)
        button = Button(self.frame, text='Вывести таблицу', command=self.vivod, width=15, height=3)
        button.grid()
        im = Image.open(r"C:/Users/user/Downloads/IMG_20231026_171115_514.jpg").resize((150, 200))
        self.image = ImageTk.PhotoImage(im)
        im1 = Image.open(r"C:/Users/user/Downloads/IMG_20231026_171115_522.jpg").resize((150, 200))
        self.image1 = ImageTk.PhotoImage(im1)
        im2 = Image.open(r"C:/Users/user/Downloads/IMG_20231026_171142_554.jpg").resize((150, 200))
        self.image2 = ImageTk.PhotoImage(im2)
        im3 = Image.open(r"C:/Users/user/Downloads/IMG_20231026_171116_056.jpg").resize((150, 200))
        self.image3 = ImageTk.PhotoImage(im3)
        im4 = Image.open(r"C:/Users/user/Downloads/IMG_20231026_171142_521.jpg").resize((150, 200))
        self.image4 = ImageTk.PhotoImage(im4)
        im5 = Image.open(r"C:/Users/user/Downloads/IMG_20231026_171115_797.jpg").resize((150, 200))
        self.image5 = ImageTk.PhotoImage(im5)
        im6 = Image.open(r"C:/Users/user/Downloads/IMG_20231026_171143_474.jpg").resize((150, 200))
        self.image6 = ImageTk.PhotoImage(im6)
        button1 = Button(master, image=self.image, width=150, height=200, command=self.b1)
        button1.grid(row=0, column=2)
        button2 = Button(master, image=self.image1, width=150, height=200, command=self.b2)
        button2.grid(row=0, column=4)
        button3 = Button(master, image=self.image2, width=150, height=200, command=self.b3)
        button3.grid(row=5, column=0)
        button4 = Button(master, image=self.image3, width=150, height=200, command=self.b4)
        button4.grid(row=5, column=3)
        button5 = Button(master, image=self.image4, width=150, height=200, command=self.b5)
        button5.grid(row=5, column=5)
        button6 = Button(master, image=self.image5, width=150, height=200, command=self.b6)
        button6.grid(row=6, column=2)
        button7 = Button(master, image=self.image6, width=150, height=200, command=self.b7)
        button7.grid(row=6, column=4)
        self.label1 = Label(self.info1, text='Выберите оценку:')
        self.label2 = Label(self.info2, text='Выберите оценку:')
        self.label3 = Label(self.info3, text='Выберите оценку:')
        self.label4 = Label(self.info4, text='Выберите оценку:')
        self.label5 = Label(self.info5, text='Выберите оценку:')
        self.label6 = Label(self.info6, text='Выберите оценку:')
        self.label7 = Label(self.info7, text='Выберите оценку:')
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=0, column=0)
        self.label3.grid(row=0, column=0)
        self.label4.grid(row=0, column=0)
        self.label5.grid(row=0, column=0)
        self.label6.grid(row=0, column=0)
        self.label7.grid(row=0, column=0)
        self.but1 = Button(self.info1, text=1, command=self.summa1, width=10, height=5, bg='red')
        self.but2 = Button(self.info1, text=2, command=self.summa2, width=10, height=5, bg='orange')
        self.but3 = Button(self.info1, text=3, command=self.summa3, width=10, height=5, bg='yellow')
        self.but4 = Button(self.info1, text=4, command=self.summa4, width=10, height=5, bg='lime')
        self.but5 = Button(self.info1, text=5, command=self.summa5, width=10, height=5, bg='green')
        self.but6 = Button(self.info2, text=1, command=self.summa6, width=10, height=5, bg='red')
        self.but7 = Button(self.info2, text=2, command=self.summa7, width=10, height=5, bg='orange')
        self.but8 = Button(self.info2, text=3, command=self.summa8, width=10, height=5, bg='yellow')
        self.but9 = Button(self.info2, text=4, command=self.summa9, width=10, height=5, bg='lime')
        self.but10 = Button(self.info2, text=5, command=self.summa10, width=10, height=5, bg='green')
        self.but11 = Button(self.info3, text=1, command=self.summa11, width=10, height=5, bg='red')
        self.but12 = Button(self.info3, text=2, command=self.summa12, width=10, height=5, bg='orange')
        self.but13 = Button(self.info3, text=3, command=self.summa13, width=10, height=5, bg='yellow')
        self.but14 = Button(self.info3, text=4, command=self.summa14, width=10, height=5, bg='lime')
        self.but15 = Button(self.info3, text=5, command=self.summa15, width=10, height=5, bg='green')
        self.but16 = Button(self.info4, text=1, command=self.summa16, width=10, height=5, bg='red')
        self.but17 = Button(self.info4, text=2, command=self.summa17, width=10, height=5, bg='orange')
        self.but18 = Button(self.info4, text=3, command=self.summa18, width=10, height=5, bg='yellow')
        self.but19 = Button(self.info4, text=4, command=self.summa19, width=10, height=5, bg='lime')
        self.but20 = Button(self.info4, text=5, command=self.summa20, width=10, height=5, bg='green')
        self.but21 = Button(self.info5, text=1, command=self.summa21, width=10, height=5, bg='red')
        self.but22 = Button(self.info5, text=2, command=self.summa22, width=10, height=5, bg='orange')
        self.but23 = Button(self.info5, text=3, command=self.summa23, width=10, height=5, bg='yellow')
        self.but24 = Button(self.info5, text=4, command=self.summa24, width=10, height=5, bg='lime')
        self.but25 = Button(self.info5, text=5, command=self.summa25, width=10, height=5, bg='green')
        self.but26 = Button(self.info6, text=1, command=self.summa26, width=10, height=5, bg='red')
        self.but27 = Button(self.info6, text=2, command=self.summa27, width=10, height=5, bg='orange')
        self.but28 = Button(self.info6, text=3, command=self.summa28, width=10, height=5, bg='yellow')
        self.but29 = Button(self.info6, text=4, command=self.summa29, width=10, height=5, bg='lime')
        self.but30 = Button(self.info6, text=5, command=self.summa30, width=10, height=5, bg='green')
        self.but31 = Button(self.info7, text=1, command=self.summa31, width=10, height=5, bg='red')
        self.but32 = Button(self.info7, text=2, command=self.summa32, width=10, height=5, bg='orange')
        self.but33 = Button(self.info7, text=3, command=self.summa33, width=10, height=5, bg='yellow')
        self.but34 = Button(self.info7, text=4, command=self.summa34, width=10, height=5, bg='lime')
        self.but35 = Button(self.info7, text=5, command=self.summa35, width=10, height=5, bg='green')
        self.but1.grid(row=1, column=0)
        self.but2.grid(row=1, column=1)
        self.but3.grid(row=1, column=2)
        self.but4.grid(row=1, column=3)
        self.but5.grid(row=1, column=4)
        self.but6.grid(row=2, column=0)
        self.but7.grid(row=2, column=1)
        self.but8.grid(row=2, column=2)
        self.but9.grid(row=2, column=3)
        self.but10.grid(row=2, column=4)
        self.but11.grid(row=3, column=0)
        self.but12.grid(row=3, column=1)
        self.but13.grid(row=3, column=2)
        self.but14.grid(row=3, column=3)
        self.but15.grid(row=3, column=4)
        self.but16.grid(row=4, column=0)
        self.but17.grid(row=4, column=1)
        self.but18.grid(row=4, column=2)
        self.but19.grid(row=4, column=3)
        self.but20.grid(row=4, column=4)
        self.but21.grid(row=5, column=0)
        self.but22.grid(row=5, column=1)
        self.but23.grid(row=5, column=2)
        self.but24.grid(row=5, column=3)
        self.but25.grid(row=5, column=4)
        self.but26.grid(row=6, column=0)
        self.but27.grid(row=6, column=1)
        self.but28.grid(row=6, column=2)
        self.but29.grid(row=6, column=3)
        self.but30.grid(row=6, column=4)
        self.but31.grid(row=7, column=0)
        self.but32.grid(row=7, column=1)
        self.but33.grid(row=7, column=2)
        self.but34.grid(row=7, column=3)
        self.but35.grid(row=7, column=4)
        master.mainloop()

    def vivod(self):
        df = pd.DataFrame({'': ['_', ':', ':', ':', ':', ':', ':', ':'],
                           '1': ['_', self.tb1, self.tb6, self.tb11, self.tb16, self.tb21, self.tb26, self.tb31],
                           '2': ['_', self.tb2, self.tb7, self.tb12, self.tb17, self.tb22, self.tb27, self.tb32],
                          '3': ['_', self.tb3, self.tb8, self.tb13, self.tb18, self.tb23, self.tb28, self.tb33],
                           '4': ['_', self.tb4, self.tb9, self.tb14, self.tb19, self.tb24, self.tb29, self.tb34],
                           '5': ['_', self.tb5, self.tb10, self.tb15, self.tb20, self.tb25, self.tb30, self.tb35]},
                          index=['', '      Venus de Milo      ', '   Townley Discobolus    ',
                                 ' Perseus slaying Medusa  ', '         Tacita           ',
                                 '        Aphrodite          ',
                                 '          Adam              ', 'Dancing Girl with Cymbals'])
        ot = Tk()
        ot.geometry('300x150')
        ot.title('Таблица данных')
        lab = Label(ot, text=df)
        lab.grid()
        ot.mainloop()

    def b1(self):
        self.open_info(1)

    def b2(self):
        self.open_info(2)

    def b3(self):
        self.open_info(3)

    def b4(self):
        self.open_info(4)

    def b5(self):
        self.open_info(5)

    def b6(self):
        self.open_info(6)

    def b7(self):
        self.open_info(7)

    def open_info(self, num):
        if num == 1:
            self.info1.title('Venus de Milo')
            self.info1.deiconify()
        if num == 2:
            self.info2.title('Townley Discobolus')
            self.info2.deiconify()
        if num == 3:
            self.info3.title('Perseus slaying Medusa')
            self.info3.deiconify()
        if num == 4:
            self.info4.title('Tacita')
            self.info4.deiconify()
        if num == 5:
            self.info5.title('Aphrodite')
            self.info5.deiconify()
        if num == 6:
            self.info6.title('Adam')
            self.info6.deiconify()
        if num == 7:
            self.info7.title('Dancing Girl with Cymbals')
            self.info7.deiconify()

    def summa1(self):
        self.tb1 += 1

    def summa2(self):
        self.tb2 += 1

    def summa3(self):
        self.tb3 += 1

    def summa4(self):
        self.tb4 += 1

    def summa5(self):
        self.tb5 += 1

    def summa6(self):
        self.tb6 += 1

    def summa7(self):
        self.tb7 += 1

    def summa8(self):
        self.tb8 += 1

    def summa9(self):
        self.tb9 += 1

    def summa10(self):
        self.tb10 += 1

    def summa11(self):
        self.tb11 += 1

    def summa12(self):
        self.tb12 += 1

    def summa13(self):
        self.tb13 += 1

    def summa14(self):
        self.tb14 += 1

    def summa15(self):
        self.tb15 += 1

    def summa16(self):
        self.tb16 += 1

    def summa17(self):
        self.tb17 += 1

    def summa18(self):
        self.tb18 += 1

    def summa19(self):
        self.tb19 += 1

    def summa20(self):
        self.tb20 += 1

    def summa21(self):
        self.tb21 += 1

    def summa22(self):
        self.tb22 += 1

    def summa23(self):
        self.tb23 += 1

    def summa24(self):
        self.tb24 += 1

    def summa25(self):
        self.tb25 += 1

    def summa26(self):
        self.tb26 += 1

    def summa27(self):
        self.tb27 += 1

    def summa28(self):
        self.tb28 += 1

    def summa29(self):
        self.tb29 += 1

    def summa30(self):
        self.tb30 += 1

    def summa31(self):
        self.tb31 += 1

    def summa32(self):
        self.tb32 += 1

    def summa33(self):
        self.tb33 += 1

    def summa34(self):
        self.tb34 += 1

    def summa35(self):
        self.tb35 += 1


if __name__ == '__main__':
    Example()
