#дебажил дипсиком, терпения не хватило
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def MNK(x, y):
    a, b = np.polyfit(x, y, 1)
    return a, b


def read_csv(path):
    df = pd.read_csv(path, sep=None, engine="python", decimal=",")
    data = df.to_numpy(dtype=float)
    return data[:, 0], data[:, 1]


def file_select():
    path = filedialog.askopenfilename(
        filetypes=[("CSV", "*.csv"), ("All", "*.*")])
    if path:
        file_path_var.set(path)
        status_var.set("Файл выбран.")


def calculate():
    file_path = file_path_var.get()
    if not file_path:
        status_var.set("Ошибка: выберите CSV-файл.")
        return
    try:
        x, y = read_csv(file_path)
        a, b = MNK(x, y)

        x_line = np.linspace(np.min(x), np.max(x), 200)
        fig = plt.figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        ax.scatter(x, y, color="tab:blue", label="Экспериментальные точки")
        ax.plot(x_line, a * x_line + b, color="red", linewidth=2,
                label=f"МНК: y = {a:.4f}x + {b:.4f}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Аппроксимация МНК")
        ax.grid(True, alpha=0.3)
        ax.legend()

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("PDF", "*.pdf")])
        if save_path:
            fig.savefig(save_path, dpi=200, bbox_inches="tight")
            status_var.set(f"График сохранён: {save_path}")
        else:
            status_var.set("График построен (не сохранён).")

        coef_var.set(f"a = {a:.6f}   b = {b:.6f}")

        plt.show(block=True)
        plt.close(fig)

    except Exception as e:
        status_var.set(f"Ошибка: {e}")


root = Tk()
root.title("Лабный Автомат")
root.geometry("580x260")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file_path_var = StringVar()
file_path_var.set("файл не выбран")
coef_var = StringVar()
status_var = StringVar()
status_var.set("Готово.")

ttk.Button(mainframe, text="Выбрать файл CSV",
           command=file_select).grid(column=1, row=1,
                                     columnspan=2, sticky=(W, E))

file_label = ttk.Label(mainframe, textvariable=file_path_var,
                       wraplength=500)
file_label.grid(column=1, row=2, columnspan=2, sticky=(W, E))

ttk.Button(mainframe, text="Рассчитать и создать график",
           command=calculate).grid(column=1, row=3,
                                   columnspan=2, sticky=(W, E))

coef_var.set("Коэффициенты МНК: —")
ttk.Label(mainframe, textvariable=coef_var).grid(column=1, row=4,
                                                  columnspan=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=status_var,
          wraplength=500, foreground="gray").grid(column=1, row=5,
                                                   columnspan=2, sticky=(W, E))

for c in mainframe.winfo_children():
    c.grid_configure(padx=7, pady=7)

root.mainloop()