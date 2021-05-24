# Розфарбування графа прямимм алгоритмом

import random
from tkinter import *
from tkinter import messagebox as mb


import networkx as nx
import pylab  as plt


def student_option():
    G = 126
    M = "ІО"
    n = 0
    if M == "ІО":
        n = (G % 6 + 1)
    res = ('Cтудентка Ступак Альона Сергіївна\nНомер залікової книжки:%s\nМій варіант:%s' % (
        G, n))
    msg = mb.showinfo("Інформація про студента", res)


class Main(Frame):
    count_nodes = 10
    count_edges = 10
    list_edges = []
    G = nx.Graph(
        [(1, 3), (1, 7), (1, 6), (2, 7), (2, 8), (2, 3), (3, 9), (3, 4), (4, 5), (5, 9), (5, 10), (6, 7), (7, 8),
         (8, 9), (9, 10), (4, 9)])
    list_colors = []
    list_matr = []
    A = nx.adjacency_matrix(G, nodelist=[i for i in range(1, G.number_of_nodes() + 1)])
    colors = ['Yellow', 'Pink', 'Green', 'Red', 'Black', 'Navy', 'Orange', 'White', 'Gray', 'Purpul', 'Brown', 'Blue']

    def __init__(self, root):
        super().__init__(root)
        self.win1(root)

    def win1(self, root):
        self.button1 = Button(root, text='Інформація про студента', command=student_option, font="Arial 12", width=20,
                              bg='#20B2AA')
        self.button1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.frame1 = LabelFrame(root, text="Випадковий граф")
        self.frame1.grid(columnspan=3)
        self.frame2 = LabelFrame(root, text="Задати ребра графа")
        self.frame2.grid(columnspan=3)
        self.button1.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.button_node = Button(self.frame1, text='Кількість вершин', command=self.nodes, font="Arial 12", width=15,
                                  bg='#FFB6C1')
        self.button_node.grid(row=2, column=1, padx=10, pady=5)
        self.node_ = Entry(self.frame1, font="Arial 12", width=15)
        self.node_.grid(row=3, column=1, pady=10)
        self.node_func = Button(self.frame1, font="Arial 12", width=15, text="Задати\n граф", bg='#FFB6C1',
                                command=self.gr_accidentally)
        self.node_func.grid(row=2, rowspan=2, column=0, padx=10)
        self.button_edge = Button(self.frame1, text='Кількість ребер', command=self.edge, font="Arial 12", width=15,
                                  bg='#FFB6C1')
        self.button_edge.grid(row=2, column=2, padx=10, pady=5)
        self.edge_ = Entry(self.frame1, font="Arial 12", width=15)
        self.edge_.grid(row=3, column=2)
        self.button_edge_add = Button(self.frame2, text='Додати ребро', command=self.edges, font="Arial 12", width=15,
                                      bg='#FFB6C1')
        self.button_edge_add.grid(row=4, column=1, padx=10, pady=5)
        self.edge_add = Entry(self.frame2, font="Arial 12", width=15)
        self.edge_add.grid(row=5, column=1, pady=5)
        self.button_edge_del = Button(self.frame2, text='Видалити ребро', command=self.edges_del, font="Arial 12",
                                      width=15,
                                      bg='#FFB6C1')
        self.button_edge_del.grid(row=4, column=2, padx=10, pady=5)
        self.edge_del = Entry(self.frame2, font="Arial 12", width=15)
        self.edge_del.grid(row=5, column=2, pady=5)
        self.edge_func = Button(self.frame2, font="Arial 12", width=15, text="Задати\n граф", bg='#FFB6C1',
                                command=self.gr_edges)
        self.edge_func.grid(row=4, rowspan=2, column=0, padx=10)
        self.variant = Button(root, font="Arial 12", width=15, text="Граф для перевірки", bg='#40E0D0',
                              command=self.variant)
        self.variant.grid(row=6, column=0, pady=5)
        self.matr = Button(root, font="Arial 12", width=15, text="Матриця суміжності", bg='#40E0D0', command=self.matr)
        self.matr.grid(row=6, column=1, pady=5)
        self.col = Button(root, font="Arial 10", width=17, text="Розфарбування графа", bg='#40E0D0', command=self.col1)
        self.col.grid(row=6, column=2, pady=5)
        self.a = Text(root, width=50, wrap=WORD, font="Arial 12", bd=5, height=10)
        self.a.grid(row=7, columnspan=3)

    def edge(self):
        Main.count_edges = int(self.edge_.get())

    def nodes(self):
        Main.count_nodes = int(self.node_.get())

    def gr_edges(self):
        for i in range(1, Main.G.number_of_nodes() + 1):
            Main.G.remove_node(i)
        Main.G.add_edges_from(Main.list_edges)

    def gr_accidentally(self):
        for i in range(1, Main.G.number_of_nodes() + 1):
            Main.G.remove_node(i)
        for x in range(1, Main.count_nodes + 1):
            Main.G.add_node(x)
        while Main.G.number_of_edges() != Main.count_edges:
            x = random.randint(1, Main.count_nodes)
            y = random.randint(1, Main.count_nodes)
            if x != y:
                Main.G.add_edge(x, y)

    def edges(self):
        x = self.edge_add.get()
        try:
            tuple1 = (int(x[0]), int(x[2]))
            Main.list_edges.append(tuple1)
        except ValueError:
            res = ('Введіть правильні значення!\n Приклад:2 3')
            msg = mb.showinfo("Помилка!", res)
        print(Main.list_edges)

    def edges_del(self):
        x = self.edge_del.get()
        try:
            tuple2 = (int(x[0]), int(x[2]))
            Main.list_edges.remove(tuple2)
        except ValueError:
            res = ('Введіть правильні значення!\n Приклад:2 3')
            msg = mb.showinfo("Помилка!", res)
        print(Main.list_edges)

    def matr(self):
        Main.A = nx.adjacency_matrix(Main.G, nodelist=[i for i in range(1, Main.G.number_of_nodes() + 1)])
        self.a.delete(0.0, END)
        self.a.insert(1.1, Main.A.todense())

    def variant(self):
        Main.G = nx.Graph(
            [(1, 3), (1, 7), (1, 6), (2, 7), (2, 8), (2, 3), (3, 9), (3, 4), (4, 5), (5, 9), (5, 10), (6, 7), (7, 8),
             (8, 9), (9, 10), (4, 9)])

    def color(self, i):
        w = {0}
        for j in range(i):
            if Main.A.todense().tolist()[j][i] > 0:
                w.add(Main.list_colors[j])
        curlol = 0
        while True:
            curlol += 1
            if curlol not in w: break
        return curlol

    def col1(self):

        Main.list_colors = [0 for i in range(Main.G.number_of_nodes())]
        for i in range(Main.G.number_of_nodes()):
            Main.list_colors[i] = self.color(i)
        print(Main.list_colors)  # список номерів кольорів для відповідних вершин
        list_color_fin = []
        for i in Main.list_colors:
            list_color_fin.append(Main.colors[(i - 1)])
        nx.draw_networkx(self.G, arrows=True, node_size=200,
                         nodelist=[i for i in range(1, Main.G.number_of_nodes() + 1)], node_color=list_color_fin,
                         width=2)
        plt.show()


if __name__ == "__main__":
    root = Tk()
    adc = Main(root)
    root.title("Лабораторна робота №4")
    root.resizable(False, False)
    root.mainloop()
