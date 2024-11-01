import tkinter

def button_clicked():
    input_text = input.get()
    if input_text:
        my_label["text"] = input_text
    else:
        my_label["text"] = "I got clicked"

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(pady=20, padx=20)

my_label = tkinter.Label(text="I am a label", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=0)
# my_label.pack(side="left")
# my_label.pack()

button = tkinter.Button(text="My new Button", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()

new_button = tkinter.Button(text="New button")
new_button.grid(column=2, row=0)

input = tkinter.Entry(width=10)
input.grid(column=3, row=3)
# input.pack()


window.mainloop()