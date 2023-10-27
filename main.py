from tkinter import *
from PIL import Image, ImageTk


class Example:
    def __init__(self):
        master = Tk()
        master.title('Museum Statistic(Demo)')
        self.info1 = Tk()
        self.info1.geometry('200x250')
        self.info1.withdraw()

        self.info2 = Tk()
        self.info2.geometry('200x250')
        self.info2.withdraw()

        self.info3 = Tk()
        self.info3.geometry('200x250')
        self.info3.withdraw()

        self.info4 = Tk()
        self.info4.geometry('200x250')
        self.info4.withdraw()

        self.info5 = Tk()
        self.info5.geometry('200x250')
        self.info5.withdraw()

        self.info6 = Tk()
        self.info6.geometry('200x250')
        self.info6.withdraw()

        self.info7 = Tk()
        self.info7.geometry('200x250')
        self.info7.withdraw()
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
        self.label1 = Label(self.info1)
        self.label2 = Label(self.info2)
        self.label3 = Label(self.info3)
        self.label4 = Label(self.info4)
        self.label5 = Label(self.info5)
        self.label6 = Label(self.info6)
        self.label7 = Label(self.info7)
        master.mainloop()
        self.info1.mainloop()
        self.info2.mainloop()
        self.info3.mainloop()
        self.info4.mainloop()
        self.info5.mainloop()
        self.info6.mainloop()
        self.info7.mainloop()

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
            self.info1.deiconify()
        if num == 2:
            self.info2.deiconify()
        if num == 3:
            self.info3.deiconify()
        if num == 4:
            self.info4.deiconify()
        if num == 5:
            self.info5.deiconify()
        if num == 6:
            self.info6.deiconify()
        if num == 7:
            self.info7.deiconify()


if __name__ == '__main__':
    Example()
