from tkinter import *


def converter():
    pounds = input_entry.get()
    output = (int(pounds) / 2.205).__round__(2)
    output_label.config(text=output)



window = Tk()
window.minsize(width=100, height=100)
window.title("Pounds / KG Converter")
window.config(padx=20, pady=20)

# title_label = Label(text="Pounds/KG")
# title_label.config(padx=5, pady=5)
# title_label.grid(column=0, row=0)


input_entry = Entry(width=7)
input_entry.insert(END, string="0")
input_entry.grid(column=1, row=0)

pounds_label = Label(text="Pounds")
pounds_label.config(padx=5, pady=5)
pounds_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to:")
is_equal_to_label.grid(column=0, row=1)

output_label = Label(text="0.0")
output_label.grid(column=1, row=1)

kg_label = Label(text="Kg")
kg_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=converter)
calc_button.grid(column=1, row=2)
window.mainloop()