import tkinter as t

def calculate():
    miles = miles_input.get()
    km = int(miles) * 1.609
    kilometers_converted_label.config(text=f"{km}")

window = t.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=200)
window.config(pady=20, padx=20)

is_equal_to_label = t.Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

miles_input = t.Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = t.Label(text="Miles")
miles_label.grid(column=2, row=0)

kilometers_converted_label = t.Label(text="0")
kilometers_converted_label.grid(column=1, row=1)

km_label = t.Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = t.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

t.mainloop()