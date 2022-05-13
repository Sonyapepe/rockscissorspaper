from tkinter import *
import random as rdm


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, text="Камень", font=("Times New Roman", 15),
                    command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, text="Ножницы", font=("Times New Roman", 15),
                    command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text="Бумага", font=("Times New Roman", 15),
                    command=lambda x=3: self.btn_click(x))
        btn4 = Button(root, text="Заново", font=("Times New Roman", 10),
                    command=lambda x=4: self.btn_click(x))

        btn.place (x=10, y=100, width=120, height=50)
        btn2.place (x=155, y=100, width=120, height=50)
        btn3.place (x=300, y=100, width=120, height=50)
        btn4.place (x=360,y=15, width=60, height=50)
        self.lbl = Label(root, text="Начало игры!", bg="#FFF", font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=150, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13),
                        text=f"Побед: {self.win}\nПроигрышей:"
                            f" {self.lose}\nНичей: {self.drow}", bg="#FFF")
        self.lbl2.place(x=5, y=5)
        self.choise= Label(root, bg="#FFF",font=("Times New Roman", 12))
        self.choise.place(x=150, y=60)

    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)
        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Ничья")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Победа")
        elif choise == 2 and comp_choise == 1 \
                or choise == 3 and comp_choise == 2 \
                or choise == 1 and comp_choise == 3:
            self.lose += 1
            self.lbl.configure(text="Проигрыш")
        elif choise==4:
            self.win = self.drow = self.lose = 0 
            comp_choise = 0
            self.lbl.configure(text="Начало игры!")
        self.lbl2.configure(text=f"Побед: {self.win}\nПроигрышей:"
                                f" {self.lose}\nНичей: {self.drow}")
        if comp_choise==0:
            self.choise.configure(text=f" ")
        elif comp_choise==2:
            self.choise.configure(text=f"Соперник выбрал Ножницы")
        elif comp_choise==1:
            self.choise.configure(text=f"Соперник выбрал Камень")
        elif comp_choise==3:
            self.choise.configure(text=f"Соперник выбрал Бумагу")
        
        del comp_choise


if __name__ == '__main__':
    root = Tk()
    root.geometry("430x160+200+200")
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()