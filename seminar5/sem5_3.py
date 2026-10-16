import random
import tkinter as tk
import pandas as pd

class A:

    def __init__(self, w):
        self.w = w
        self.w.title("Films")
        self.s1 = {}

        d = pd.read_csv("imdb_top_250.csv")
        for i, r in d.iterrows():
            t = r["Title"]
            g_list = r["Genre"].split(" | ")

            for g in g_list:
                g = g.strip()
                if g not in self.s1:
                    self.s1[g] = []
                self.s1[g].append(t)

        self.e = tk.Entry(w)
        self.e.pack()

        self.b = tk.Button(w, text="Find", command=self.find)
        self.b.pack()

        self.l1 = tk.Label(w, text="")
        self.l1.pack()

        genres_string = ", ".join(sorted(self.s1.keys()))
        self.l2 = tk.Label(w, text=genres_string)
        self.l2.pack()

    def find(self):
        g = self.e.get().strip()
        films_list = self.s1[g]
        chosen_film = random.choice(films_list)

        self.l1.config(text=chosen_film + "\n(" + g + ")")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x250")
    app = A(root)
    root.mainloop()