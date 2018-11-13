import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("E-card Generator")
window.geometry('280x100')

labelTop = tk.Label(window, text="Choose Your Occasion")
labelTop.grid(row=0, column=0)

Occasions = ttk.Combobox(window, values=["Birthday", "Anniversary", "Christmas", "Valentines Day", "Congratulations"])
print(dict(Occasions))
Occasions.grid(row=1, column=0)
Occasions.current(0)
print(Occasions.current(), Occasions.get())

window.mainloop()
