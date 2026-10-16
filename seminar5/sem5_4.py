from tkinter import *
from tkinter import ttk

def color(*args):
    try:
        a = str(hexin.get()).strip()
        if a.startswith('#'):
            a = a[1:]
            
        if len(a) != 6:
            result_label['text'] = 'Ошибка: нужен формат #RRGGBB'
            result_label['bg'] = 'white'
            return  

        r = int(a[0:2], 16)
        g = int(a[2:4], 16)
        b = int(a[4:6], 16)

        comp_r = f"{255 - r:02x}"
        comp_g = f"{255 - g:02x}"
        comp_b = f"{255 - b:02x}"

        hexout = f"#{comp_r}{comp_g}{comp_b}"
        
        result.set(hexout)
        
        hexin_entry.config(fg=f"#{a}")
        
        result_label['bg'] = hexout 

    except ValueError:
        result_label['text'] = 'Ошибка: введены не HEX-символы'
        result_label['bg'] = 'white'

root = Tk()
root.title("Подбор цветов")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

hexin = StringVar()
hexin_entry = ttk.Entry(mainframe, width=7, textvariable=hexin)
hexin_entry.grid(column=2, row=1, sticky=(W, E))

result = StringVar()
result_label = ttk.Label(mainframe, textvariable=result, width=10, relief="solid") 
result_label.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Подобрать", command=color).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

hexin_entry.focus()
root.bind("<Return>", color)

root.mainloop()