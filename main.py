from tkinter import *


def button_cliked():
    print("Igot clicked")
    user_input = int(entry.get())
    changed = round(user_input*1.609, 2)
    Converted_label.config(text= changed)



# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx= 25, pady=25)

#Label
Miles_label = Label(text="Miles", font=("Arial", 14, "normal"))
Miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 14, "normal"))
equal_label.grid(column=0, row=1)

Km_label = Label(text="Km", font=("Arial", 14, "normal"))
Km_label.grid(column=2, row=1)

Converted_label = Label(text="0", font=("Arial", 14, "normal"))
Converted_label.grid(column=1, row=1)

#Button


button1 = Button(text="Calculate", command=button_cliked)
button1.grid(column=1, row=2)


entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)












window.mainloop()