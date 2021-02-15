from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def passw_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbol + pass_numbers
    shuffle(password_list)

    final_password = "".join(password_list)
    passw_entry.insert(0, final_password)
    pyperclip.copy(final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def passw_save():

    uri = uri_entry.get()
    username = user_entry.get()
    password = passw_entry.get()
    new_data = {
        uri: {
            "username": username,
            "password": password,
        }
    }

    if len(uri) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill out all entries.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                read_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as new_file:
                json.dump(new_data, new_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # Updating old data with new data
                read_data.update(new_data)
                # Saving the updated data
                json.dump(read_data, data_file, indent=4)
        finally:
            uri_entry.delete(0, END)
            user_entry.delete(0, END)
            passw_entry.delete(0, END)

# ---------------------------- SEARCH URI -----------------------------#

def passw_search():

    uri = uri_entry.get()

    if len(uri) == 0:
        messagebox.showinfo(title="Error", message="URI form is empty.")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found.")
        else:
            if uri in data:
                messagebox.showinfo(title=f"{data[uri]}",
                                    message=f"\nUsername: {data[uri]['username']}"
                                            f"\nPassword: {data[uri]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No data for {uri} found.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

bg_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)

#Labels
uri_label = Label(text="URI:")
uri_label.grid(column=0, row=1)

user_label = Label(text="Username:")
user_label.grid(column=0, row=2)

passw_label = Label(text="Password:")
passw_label.grid(column=0, row=3)

#Entries
uri_entry = Entry(width=25)
uri_entry.grid(column=1, row=1)
uri_entry.focus()

user_entry = Entry(width=36)
user_entry.grid(column=1, row=2, columnspan=2)

passw_entry = Entry(width=25, show="*")
passw_entry.grid(column=1, row=3)

# Button layout and config
search_button = Button(text="  Search  ", command=passw_search)
search_button.grid(column=2, row=1)

passw_gen_button = Button(text="Generate", command=passw_gen)
passw_gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=passw_save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
