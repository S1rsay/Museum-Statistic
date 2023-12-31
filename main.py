from tkinter import *
from PIL import Image, ImageTk
from prettytable import PrettyTable


class Example:
    def __init__(self):
        self.tb1, self.tb2, self.tb3, self.tb4, self.tb5, self.tb6, self.tb7 = 0, 0, 0, 0, 0, 0, 0
        self.tb7, self.tb8, self.tb9, self.tb10, self.tb11, self.tb12, self.tb13 = 0, 0, 0, 0, 0, 0, 0
        self.tb14, self.tb15, self.tb16, self.tb17, self.tb18, self.tb19, self.tb20 = 0, 0, 0, 0, 0, 0, 0
        self.tb21, self.tb22, self.tb23, self.tb24, self.tb25, self.tb26, self.tb27 = 0, 0, 0, 0, 0, 0, 0
        self.tb28, self.tb29, self.tb30, self.tb31, self.tb32, self.tb33, self.tb34, self.tb35 = 0, 0, 0, 0, 0, 0, 0, 0
        master = Tk()
        master.geometry('740x675')
        master.title('Museum Statistic')
        master.config(bg='grey')
        button = Button(master, text='Вывести таблицу', command=self.vivod, width=15, height=3)
        button.grid(row=3, column=7)
        im = Image.open(r"C:/Users/Danil/Downloads/IMG_20231026_171115_514.jpg").resize((150, 200))
        self.image = ImageTk.PhotoImage(im)
        im1 = Image.open(r"C:/Users/Danil/Downloads/IMG_20231026_171115_522.jpg").resize((150, 200))
        self.image1 = ImageTk.PhotoImage(im1)
        im2 = Image.open(r"C:/Users/Danil/Downloads/IMG_20231026_171142_554.jpg").resize((150, 200))
        self.image2 = ImageTk.PhotoImage(im2)
        im3 = Image.open(r"C:/Users/Danil/Downloads/IMG_20231026_171116_056.jpg").resize((150, 200))
        self.image3 = ImageTk.PhotoImage(im3)
        im4 = Image.open(r"C:/Users/Danil/Downloads/IMG_20231026_171142_521.jpg").resize((150, 200))
        self.image4 = ImageTk.PhotoImage(im4)
        im5 = Image.open(r"C:/Users/Danil/Downloads/IMG_20231026_171115_797.jpg").resize((150, 200))
        self.image5 = ImageTk.PhotoImage(im5)
        im6 = Image.open(r"C:/Users/Danil/Downloads/IMG_20231026_171143_474.jpg").resize((150, 200))
        self.image6 = ImageTk.PhotoImage(im6)
        button1 = Button(master, image=self.image, width=150, height=200, command=self.b1)
        button1.grid(row=0, column=4)
        button2 = Button(master, image=self.image1, width=150, height=200, command=self.b2)
        button2.grid(row=0, column=5)
        button3 = Button(master, image=self.image2, width=150, height=200, command=self.b3)
        button3.grid(row=1, column=0)
        button4 = Button(master, image=self.image3, width=150, height=200, command=self.b4)
        button4.grid(row=1, column=4, columnspan=2)
        button5 = Button(master, image=self.image4, width=150, height=200, command=self.b5)
        button5.grid(row=1, column=6)
        button6 = Button(master, image=self.image5, width=150, height=200, command=self.b6)
        button6.grid(row=2, column=0)
        button7 = Button(master, image=self.image6, width=150, height=200, command=self.b7)
        button7.grid(row=2, column=6)
        master.mainloop()

    def vivod(self):
        x = PrettyTable()
        x.field_names = ["", "1", "2", "3", "4", "5"]
        x.add_row(["Venus de Milo", self.tb1, self.tb2, self.tb3, self.tb4, self.tb5])
        x.add_row(["Townley Discobolus", self.tb6, self.tb7, self.tb8, self.tb9, self.tb10])
        x.add_row(["Perseus slaying Medusa", self.tb11, self.tb12, self.tb13, self.tb14, self.tb15])
        x.add_row(["Tacita", self.tb16, self.tb17, self.tb18, self.tb19, self.tb20])
        x.add_row(["Aphrodite", self.tb21, self.tb22, self.tb23, self.tb24, self.tb25])
        x.add_row(["Adam", self.tb26, self.tb27, self.tb28, self.tb29, self.tb30])
        x.add_row(["Dancing Girl with Cymbals", self.tb31, self.tb32, self.tb33, self.tb34, self.tb35])
        ot = Tk()
        ot.title('Таблица данных')
        lab = Label(ot, text=x)
        lab.grid()

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
        info = Tk()
        if num == 1:
            info.title('Venus de Milo')
            but1 = Button(info, text=1, command=self.summa1, width=10, height=5, bg='red')
            but2 = Button(info, text=2, command=self.summa2, width=10, height=5, bg='orange')
            but3 = Button(info, text=3, command=self.summa3, width=10, height=5, bg='yellow')
            but4 = Button(info, text=4, command=self.summa4, width=10, height=5, bg='lime')
            but5 = Button(info, text=5, command=self.summa5, width=10, height=5, bg='green')
        if num == 2:
            info.title('Townley Discobolus')
            but1 = Button(info, text=1, command=self.summa6, width=10, height=5, bg='red')
            but2 = Button(info, text=2, command=self.summa7, width=10, height=5, bg='orange')
            but3 = Button(info, text=3, command=self.summa8, width=10, height=5, bg='yellow')
            but4 = Button(info, text=4, command=self.summa9, width=10, height=5, bg='lime')
            but5 = Button(info, text=5, command=self.summa10, width=10, height=5, bg='green')
        if num == 3:
            info.title('Perseus slaying Medusa')
            but1 = Button(info, text=1, command=self.summa11, width=10, height=5, bg='red')
            but2 = Button(info, text=2, command=self.summa12, width=10, height=5, bg='orange')
            but3 = Button(info, text=3, command=self.summa13, width=10, height=5, bg='yellow')
            but4 = Button(info, text=4, command=self.summa14, width=10, height=5, bg='lime')
            but5 = Button(info, text=5, command=self.summa15, width=10, height=5, bg='green')
        if num == 4:
            info.title('Tacita')
            but1 = Button(info, text=1, command=self.summa16, width=10, height=5, bg='red')
            but2 = Button(info, text=2, command=self.summa17, width=10, height=5, bg='orange')
            but3 = Button(info, text=3, command=self.summa18, width=10, height=5, bg='yellow')
            but4 = Button(info, text=4, command=self.summa19, width=10, height=5, bg='lime')
            but5 = Button(info, text=5, command=self.summa20, width=10, height=5, bg='green')
        if num == 5:
            info.title('Aphrodite')
            but1 = Button(info, text=1, command=self.summa21, width=10, height=5, bg='red')
            but2 = Button(info, text=2, command=self.summa22, width=10, height=5, bg='orange')
            but3 = Button(info, text=3, command=self.summa23, width=10, height=5, bg='yellow')
            but4 = Button(info, text=4, command=self.summa24, width=10, height=5, bg='lime')
            but5 = Button(info, text=5, command=self.summa25, width=10, height=5, bg='green')
        if num == 6:
            info.title('Adam')
            but1 = Button(info, text=1, command=self.summa26, width=10, height=5, bg='red')
            but2 = Button(info, text=2, command=self.summa27, width=10, height=5, bg='orange')
            but3 = Button(info, text=3, command=self.summa28, width=10, height=5, bg='yellow')
            but4 = Button(info, text=4, command=self.summa29, width=10, height=5, bg='lime')
            but5 = Button(info, text=5, command=self.summa30, width=10, height=5, bg='green')
        if num == 7:
            info.title('Dancing Girl with Cymbals')
            but1 = Button(info, text=1, command=self.summa31, width=10, height=5, bg='red')
            but2 = Button(info, text=2, command=self.summa32, width=10, height=5, bg='orange')
            but3 = Button(info, text=3, command=self.summa33, width=10, height=5, bg='yellow')
            but4 = Button(info, text=4, command=self.summa34, width=10, height=5, bg='lime')
            but5 = Button(info, text=5, command=self.summa35, width=10, height=5, bg='green')
        info.geometry('425x100')
        but1.grid(row=3, column=0, columnspan=1)
        but2.grid(row=3, column=1)
        but3.grid(row=3, column=2)
        but4.grid(row=3, column=3)
        but5.grid(row=3, column=4)
        label = Label(info, text='Выберите оценку:')
        label.grid(row=0, column=0)

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
