# from tkinter import *

# def calc(*args):
#     try:
#         result.set(str(eval(command.get())))
#     except:
#         pass


# root = Tk()
# root.title('Калькулятор')

# mainframe = Frame(root)
# mainframe.grid(column = 0, row= 0, sticky= (N, S, W, E))
# root.columnconfigure(0, weight= 1)
# root.rowconfigure(0, weight= 1)

# command = StringVar()
# result = StringVar()


# entry = Entry(mainframe, textvariable= command)
# entry.grid(column = 1, row= 0)

# Label(mainframe, textvariable= result).grid(column= 1, row= 2)

# Button(mainframe, text= 'Calculate!', command = calc).grid(column= 1, row=3)

# root.bind('<Return>', calc)
# entry.focus()

# root.mainloop()

from tkinter import *

def calc(*args):
    try:
        result.set(str(eval(command.get())))
    except Exception:
        result.set("Ошибка")

root = Tk()
root.title('Калькулятор')

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, S, W, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

command = StringVar()
result = StringVar()

entry = Entry(mainframe, textvariable=command)
entry.grid(column=1, row=0)
entry.focus_set()

Label(mainframe, textvariable=result).grid(column=1, row=2)

Button(mainframe, text='Calculate!', command=calc).grid(column=1, row=3)

root.bind('<Return>', calc)

root.mainloop()