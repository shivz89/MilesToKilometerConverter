from tkinter import *

def convert_miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to KM Coverter")
window.config(padx=20,pady=20)

#creating widgets
#miles input widget
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#label 1
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#label 2
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

#label 3 
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

#label 4
kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

#Button
calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()