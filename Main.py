import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        tk.Tk.iconbitmap(self, default = "favicon.ico")
        tk.Tk.wm_title(self, "IA - Search Methods")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, OptionsPage, MapPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Start Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = "Options",
                            command = lambda: controller.show_frame(OptionsPage))
        button1.pack()

        button2 = ttk.Button(self, text = "Map",
                            command = lambda: controller.show_frame(MapPage))
        button2.pack()


class OptionsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Options Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = "Back to start menu",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()


def testGraph():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=4)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('A', 'C', weight=3)
    G.add_edge('C', 'D', weight=4)
    print(nx.shortest_path(G, 'A', 'D', weight='weight'))
    nx.draw(G)
    plt.savefig("simple_path.png") # save as png
    plt.show() # display

class MapPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Map Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = "Back to start menu",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text = "test graph",
                            command = lambda: testGraph())
        button2.pack()



app = Main()
app.mainloop()
