import pickle
from tkinter import *
from tkinter import messagebox as mb
import funk, funk2



class Main(Frame):
    list_g_name=["Віра", "Іванна", "Катерина", "Софія", "Анна", "Лариса", "Аліна", "Юлія", "Галина", "Любов",
                 "Марина", "Марія", "Олена", "Дарина", "Надія"]
    list_g_name.sort()
    list_m_name = ["Сергій", "Іван", "Олег", "Матвій", "Ігор", "Василь", "Антон", "Віктор", "Євген",
                   "Роман","Артем", "Єгор", "Данило", "Остап", "Богдан"]
    list_m_name.sort()
    def __init__(self, root):
        super().__init__(root)
        self.win1(root)

    def win1(self, root):
        self.button1 = Button(root, text='Інформація про студента', command=self.student_option, font="Arial 12", width=20)
        self.button1.grid(row=1, column=1,  padx=10, pady=10)
        self.window2 = Button(root,font="Arial 12", width=20, text='Вікно №2', command=self.win2)
        self.window2.grid(row=2, column=0,padx=10, pady=10)

        self.window3 = Button(root,font="Arial 12", width=20, text='Вікно №3', command=self.win3)
        self.window3.grid(row=2, column=1, padx=10,pady=10)

        self.window4 = Button(root, text='Вікно №4',font="Arial 12", width=20, command=self.win4)
        self.window4.grid(row=2, column=2,padx=10, pady=10)


    def student_option(self):
        self.G = 1
        self.N = 26
        self.M = "ІО"
        self.n = 0
        if self.M == "ІО":
            self.n = ((self.N + 1 + self.G % 60) % 30 + 1)

        self.res = ('Cтудентка Ступак Альона Сергіївна\nМоя група: %s-0%s\nМій номер у групі:%s\nМій варіант:%s' % (
            self.M, self.G, self.N, self.n))
        self.msg = mb.showinfo("Інформація про студента", self.res)

    def win2(self):
        Window2()

    def win3(self):
        Window3()

    def win4(self):
        Window4()


class Window2(Toplevel):
    setA=set()
    setB = set()
    def __init__(self):
        super().__init__(root)
        self.win_2()

    def win_2(self):
        self.title("Вікно №2")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.listbox = Listbox(self, selectmode=EXTENDED)
        self.listbox.grid(row=1, column=0,  padx=10, pady=10)
        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=1, column=1, sticky = "nsew")
        for i in Main.list_g_name:
            self.listbox.insert(END, i)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox2 = Listbox(self, selectmode=EXTENDED)
        self.listbox2.grid(row=1, column=2,  padx=10, pady=10)
        for i in Main.list_m_name:
            self.listbox2.insert(END, i)
        self.scrollbar2 = Scrollbar(self)
        self.scrollbar2.grid(row=1, column=3, sticky="nsew")
        self.listbox2.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.listbox2.yview)
        self.v = BooleanVar()
        self.v.set(0)
        self.radio = Radiobutton(self, text="Дії з множиною А", variable=self.v, value=1)
        self.radio.grid(row=2, column=0, columnspan=2)
        self.radio2 = Radiobutton(self, text="Дії з множиною B", variable=self.v, value=0)
        self.radio2.grid(row=3, column=0, columnspan=2)
        self.add = Button(self, text="Додати", width=10, command = self.add_)
        self.add.grid(row=2, column =2)
        self.del_= Button(self, text="Очистити", width=10, command = self.del_s)
        self.del_.grid(row=3, column=2)
        self.listbox3 = Listbox(self, selectmode=EXTENDED)
        self.listbox3.grid(row=4, column=0,  padx=10, pady=10)
        self.scrollbar3 = Scrollbar(self)
        self.scrollbar3.grid(row=4, column=1, sticky="nsew")
        self.listbox3.config(yscrollcommand=self.scrollbar3.set)
        self.scrollbar3.config(command=self.listbox3.yview)
        self.listbox4 = Listbox(self, selectmode=EXTENDED)
        self.listbox4.grid(row=4, column=2,  padx=10, pady=10)
        self.scrollbar4 = Scrollbar(self)
        self.scrollbar4.grid(row=4, column=3, sticky="nsew")
        self.listbox4.config(yscrollcommand=self.scrollbar4.set)
        self.scrollbar4.config(command=self.listbox4.yview)
        self.keep = Button(self, text="Зберегти у файл", command =self.wr)
        self.keep.grid(row=5, column=0, pady=10)
        self.read = Button(self, text="Зчитати з файлу", command =self.rd)
        self.read.grid(row=5, column=2, pady=10)
    def add_(self):
        if self.v.get():
            self.listbox3.delete(0, END)
            Window2.setA.update(self.listbox.get(ind) for ind in self.listbox.curselection())
            Window2.setA.update(self.listbox2.get(ind) for ind in self.listbox2.curselection())
            for i in Window2.setA:
                self.listbox3.insert(END, i)
        else :
            self.listbox4.delete(0, END)
            Window2.setB.update(self.listbox.get(ind) for ind in self.listbox.curselection())
            Window2.setB.update(self.listbox2.get(ind) for ind in self.listbox2.curselection())
            for i in Window2.setB:
                self.listbox4.insert(END, i)
    def del_s(self):
        if self.v.get():
            self.listbox3.delete(0, END)
            Window2.setA.clear()
        else:
            self.listbox4.delete(0, END)
            Window2.setB.clear()
    def wr(self):
        if self.v.get():
            with  open("lab2_setA.txt", "wb") as n:
                pickle.dump(Window2.setA, n)
        else:
            with  open("lab2_setB.txt", "wb") as n:
                pickle.dump(Window2.setB, n)
    def rd(self):
        if self.v.get():
            self.listbox3.delete(0, END)
            with open("lab2_setA.txt", "rb") as f:
                for i in pickle.load(f):
                    self.listbox3.insert(END, i)
        else:
            self.listbox4.delete(0, END)
            with open("lab2_setB.txt", "rb") as f:
                for i in pickle.load(f):
                    self.listbox4.insert(END, i)

class Window3(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.win_3()


    def win_3(self):
        self.title("Вікно №3")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.lab_a = Label(self, text="Множина А")
        self.lab_a.grid(row=1, column=0)
        self.lab_b= Label(self, text="Множина В")
        self.lab_b.grid(row=1, column=2)
        self.listbox3 = Listbox(self, selectmode=EXTENDED, font='Arial 10', width=30)
        self.listbox3.grid(row=2, column=0, padx=10, pady=10)
        self.scrollbar3 = Scrollbar(self)
        self.scrollbar3.grid(row=2, column=1, sticky="nsew")
        self.listbox3.config(yscrollcommand=self.scrollbar3.set)
        self.scrollbar3.config(command=self.listbox3.yview)
        self.listbox4 = Listbox(self, selectmode=EXTENDED, width=30)
        self.listbox4.grid(row=2, column=2, padx=10, pady=10)
        self.scrollbar4 = Scrollbar(self)
        self.scrollbar4.grid(row=2, column=3, sticky="nsew")
        self.listbox4.config(yscrollcommand=self.scrollbar4.set)
        self.scrollbar4.config(command=self.listbox4.yview)
        self.r()
        self.S=funk.a_husband_b(Window2.setA, Window2.setB, Main.list_m_name, Main.list_g_name)
        self.R =funk.a_test_b(Window2.setA, Window2.setB, Main.list_m_name)
        self.f = open(r"fileS.txt", "wb")
        pickle.dump(self.S, self.f)
        self.f.close()
        self.f2 = open(r"fileR.txt", "wb")
        pickle.dump(self.R, self.f2)
        self.f2.close()
        self.lab_S= Label(self, text="Відношення S")
        self.lab_S.grid(row=3, column=0)
        self.lab_R = Label(self, text="Відношення R")
        self.lab_R.grid(row=5, column=0)
        self.aSb = Canvas(self,  bg='white', width=600, height=200)
        self.dict_SA = {}
        self.dict_SB = {}
        for i in range(len(Window2.setA)):
            self.aSb.create_text(30 + i * 50, 50, text=list(Window2.setA)[i], font='Arial 10')
            self.aSb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
            self.dict_SA.update({list(Window2.setA)[i]: [30 + i * 50, 80]})
        for j in range(len(Window2.setB)):
            self.aSb.create_text(30 + j * 50, 190, text=list(Window2.setB)[j], font='Arial 10')
            self.aSb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="pink")
            self.dict_SB.update({list(Window2.setB)[j]: [30 + j * 50, 160]})
        for k in self.S:
            self.aSb.create_line(self.dict_SA[k[0]], self.dict_SB[k[1]], arrow=LAST)
        self.aSb.grid(row=4, column=0, columnspan=5)
        self.dict_RA = {}
        self.dict_RB = {}
        self.aRb = Canvas(self, bg='white', width=600, height=200, )
        for i in range(len(Window2.setA)):
            self.aRb.create_text(30 + i * 50, 50, text=list(Window2.setA)[i], font='Arial 10')
            self.aRb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            self.dict_RA.update({list(Window2.setA)[i]: [30 + i * 50, 80]})
        for j in range(len(Window2.setB)):
            self.aRb.create_text(30 + j * 50, 190, text=list(Window2.setB)[j], font='Arial 10')
            self.aRb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="orange")
            self.dict_RB.update({list(Window2.setB)[j]: [30 + j * 50, 160]})
        for k in self.R:
            self.aRb.create_line(self.dict_RA[k[0]], self.dict_RB[k[1]], arrow=LAST)
        self.aRb.grid(row=6, column=0, columnspan=5)

    def r(self):
        with open("lab2_setA.txt", "rb") as f:
            for i in pickle.load(f):
                self.listbox3.insert(END, i)
        with open("lab2_setB.txt", "rb") as p:
            for i in pickle.load(p):
                self.listbox4.insert(END, i)




class Window4(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.win_4()

    def win_4(self):
        self.title("Вікно №4")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.f = open(r"fileS.txt", "rb")
        self.S= pickle.load(self.f)
        self.f.close()
        self.f2 = open(r"fileR.txt", "rb")
        self.R = pickle.load(self.f2)
        self.f2.close()
        self.res_1 = Canvas(self, bg='white', width=600, height=200)
        self.res1= funk2.product1(self.S, self.R)
        self.d1={}
        self.d2 = {}
        self.l1=Label(self, text="Об'єднання S і R")
        self.l1.grid(row=1, column=0)
        for i in range(len(Window2.setA)):
            self.res_1.create_text(30 + i * 50, 50, text=list(Window2.setA)[i], font='Arial 10')
            self.res_1.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="blue")
            self.d1.update({list(Window2.setA)[i]: [30 + i * 50, 80]})
        for j in range(len(Window2.setB)):
            self.res_1.create_text(30 + j * 50, 190, text=list(Window2.setB)[j], font='Arial 10')
            self.res_1.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="pink")
            self.d2.update({list(Window2.setB)[j]: [30 + j * 50, 160]})
        for k in self.res1:
            self.res_1.create_line(self.d1[k[0]], self.d2[k[1]], arrow=LAST)
        self.res_1.grid(row=2, column=0)
        self.res_2 = Canvas(self, bg='white', width=600, height=200)
        self.res2 = funk2.product2(self.S, self.R)
        self.d1_2 = {}
        self.d2_2 = {}
        self.l2 = Label(self, text="Перетин S і R")
        self.l2.grid(row=3, column=0)
        for i in range(len(Window2.setA)):
            self.res_2.create_text(30 + i * 50, 50, text=list(Window2.setA)[i], font='Arial 10')
            self.res_2.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            self.d1_2.update({list(Window2.setA)[i]: [30 + i * 50, 80]})
        for j in range(len(Window2.setB)):
            self.res_2.create_text(30 + j * 50, 190, text=list(Window2.setB)[j], font='Arial 10')
            self.res_2.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="orange")
            self.d2_2.update({list(Window2.setB)[j]: [30 + j * 50, 160]})
        for k in self.res2:
            self.res_2.create_line(self.d1[k[0]], self.d2[k[1]], arrow=LAST)
        self.res_2.grid(row=4, column=0)
        self.res_3 = Canvas(self, bg='white', width=600, height=200)
        self.res3 = funk2.product3(self.S, self.R)
        self.d1_3 = {}
        self.d2_3 = {}
        self.l3 = Label(self, text="Різниця S і R")
        self.l3.grid(row=5, column=0)
        for i in range(len(Window2.setA)):
            self.res_3.create_text(30 + i * 50, 50, text=list(Window2.setA)[i], font='Arial 10')
            self.res_3.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="purple")
            self.d1_3.update({list(Window2.setA)[i]: [30 + i * 50, 80]})
        for j in range(len(Window2.setB)):
            self.res_3.create_text(30 + j * 50, 190, text=list(Window2.setB)[j], font='Arial 10')
            self.res_3.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="yellow")
            self.d2_3.update({list(Window2.setB)[j]: [30 + j * 50, 160]})
        for k in self.res3:
            self.res_3.create_line(self.d1[k[0]], self.d2[k[1]], arrow=LAST)
        self.res_3.grid(row=6, column=0)
        self.res_4 = Canvas(self, bg='white', width=600, height=200)
        self.res4 = funk2.product4(Window2.setA, Window2.setB, self.R)
        self.d1_4 = {}
        self.d2_4 = {}
        self.l4 = Label(self, text="Різниця U і R")
        self.l4.grid(row=1, column=2)
        for i in range(len(Window2.setA)):
            self.res_4.create_text(30 + i * 50, 50, text=list(Window2.setA)[i], font='Arial 10')
            self.res_4.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="red")
            self.d1_4.update({list(Window2.setA)[i]: [30 + i * 50, 80]})
        for j in range(len(Window2.setB)):
            self.res_4.create_text(30 + j * 50, 190, text=list(Window2.setB)[j], font='Arial 10')
            self.res_4.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="white")
            self.d2_4.update({list(Window2.setB)[j]: [30 + j * 50, 160]})
        for k in self.res4:
            self.res_4.create_line(self.d1_4[k[0]], self.d2_4[k[1]], arrow=LAST)
        self.res_4.grid(row=2, column=2)
        self.l5 = Label(self, text="S^-1")
        self.l5.grid(row=3, column=2)
        self.aSb = Canvas(self,  bg='white', width=600, height=200)
        self.dict_SA = {}
        self.dict_SB = {}
        for i in range(len(Window2.setA)):
            self.aSb.create_text(30 + i * 50, 50, text=list(Window2.setA)[i], font='Arial 10')
            self.aSb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="coral")
            self.dict_SA.update({list(Window2.setA)[i]: [30 + i * 50, 80]})
        for j in range(len(Window2.setB)):
            self.aSb.create_text(30 + j * 50, 190, text=list(Window2.setB)[j], font='Arial 10')
            self.aSb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="aquamarine")
            self.dict_SB.update({list(Window2.setB)[j]: [30 + j * 50, 160]})
        for k in self.S:
            self.aSb.create_line(self.dict_SB[k[1]], self.dict_SA[k[0]],  arrow=LAST)
        self.aSb.grid(row=4, column=2)

if __name__ == "__main__":
    root = Tk()
    adc = Main(root)
    root.title("Лабораторна робота №1")
    root.resizable(False, False)
    root.mainloop()

