import random
import tkinter as t
from json import JSONDecodeError
from tkinter import messagebox
import pandas
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, t.END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    try:
        json_data = pandas.read_json("data.json")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    else:
        website = web_site_input.get()
        if website:
            website = website.title()
        if website in json_data:
            email = json_data[website].email
            password = json_data[website].password
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassowrd: {password}")
        else:
            messagebox.showinfo(title=website, message=f"Password Not Found")


def add():
    website = web_site_input.get()
    password = password_input.get()
    email_username = email_username_input.get()

    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showerror(title="Opsss", message=f"Please, don't leave any the fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email_username}\n"
                                                              f"Password: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            if radio_var.get() == 'Csv':
                dict = {
                    "website": [website.title()],
                    "password": [password],
                    "email_username": [email_username],
                }
                data_df = pandas.DataFrame.from_dict(dict)
                data_df.to_csv("password.csv", mode="a", index=False, header=False, sep="|")
            else:
                new_dict = {
                    website.title(): {
                        "password": password,
                        "email": email_username
                    }
                }

                try:
                    with open("data.json", mode="r") as data_file:
                        dict_to_save = json.load(data_file)
                except FileNotFoundError as error_message:
                    with open("data.json", mode="w") as data_file:
                        json.dump(new_dict, data_file, indent=4)
                except JSONDecodeError as error_message:
                    print("File is empty.")
                else:
                    dict_to_save.update(new_dict)
                    with open("data.json", mode="w") as data_file:
                        json.dump(dict_to_save, data_file, indent=4)
                finally:
                    web_site_input.delete(0, t.END)
                    password_input.delete(0, t.END)


# ---------------------------- UI SETUP ------------------------------- #

window = t.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = t.Canvas(width=200, height=200)
logo_pgn = t.PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo_pgn)
canvas.grid(column=1, row=0)

web_site_label = t.Label(text="Website:")
web_site_label.grid(column=0, row=1)

email_username_label = t.Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = t.Label(text="Password:")
password_label.grid(column=0, row=3)

web_site_input = t.Entry(width=52)
web_site_input.grid(column=1, row=1, sticky="w", padx=10, pady=5)

email_username_input = t.Entry(width=52)
email_username_input.grid(column=1, row=2, columnspan=2, sticky="w", padx=10, pady=5)
email_username_input.insert(0, "leandro.lpalermo@gmail.com")

password_input = t.Entry(width=40)
password_input.grid(column=1, row=3, sticky="w", padx=10, pady=5)

search_button = t.Button(text="Search", command=search_password, width=15)
search_button.grid(column=2, row=1, sticky="w")

generate_password_button = t.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w")

radio_var = t.StringVar(value="Csv")
csv_radio_button = t.Radiobutton(window, text="Csv format", variable=radio_var, value="Csv")
json_radio_button = t.Radiobutton(window, text="Json format", variable=radio_var, value="Json")
csv_radio_button.grid(column=1, row=4, padx=10, pady=5, sticky="w")
json_radio_button.grid(column=2, row=4, pady=5, sticky="w")

add_button = t.Button(text="Add", width=44, command=add)
add_button.grid(column=1, row=5, columnspan=2, sticky="w", padx=10, pady=5)

window.mainloop()
