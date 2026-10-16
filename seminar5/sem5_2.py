from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value1 = int(mas.get())
        value2 = float(rost.get())
        value3 = value1/(value2**2/10000)
        r = ''
        if value3 <= 16:
            r = "Выраженный дефицит массы тела"
        elif 16 < value3 <= 18.5:
            r = "Недостаточная (дефицит) масса тела"
        elif 18.5 < value3 <= 25:
            r = "Норма"
        elif 25 < value3 <= 30:
            r = "Избыточная масса тела (предожирение)"
        elif 30 < value3 <= 35:
            r = "Ожирение 1 степени"
        elif 35 < value3 <= 40:
            r = "Ожирение 2 степени"
        else:
            r = "Ожирение 3 степени"

        result.set(f'{value1/(value2**2/10000):.1f} {r}')

    except ValueError:
        pass

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
for i in range(10):
    mainframe.columnconfigure(i, weight=1)
    mainframe.rowconfigure(i, weight=1)

mas = StringVar()
mas_entry = ttk.Entry(mainframe, width=7, textvariable= mas)
mas_entry.grid(column=2, row=1, sticky=(W, E))
rost = StringVar()
rost_entry = ttk.Entry(mainframe, width=7, textvariable=rost)
rost_entry.grid(column=2, row=2, sticky=(W, E))

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="кг").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="см").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="результат").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

mas_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()