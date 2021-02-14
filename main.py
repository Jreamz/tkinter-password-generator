from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip


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

    if len(uri) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill out all entries.")

    else:
        is_proceed = messagebox.askokcancel(title=uri, message=f"You have entered:\n Username: {username}\n Password: "
                                                               f"{password}\n Would you like to proceed?")

        if is_proceed:
            with open("data.txt", "a") as data:
                data.write(f"{uri} | {username} | {password}\n")
                uri_entry.delete(0, END)
                user_entry.delete(0, END)
                passw_entry.delete(0, END)

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
uri_entry = Entry(width=36)
uri_entry.grid(column=1, row=1, columnspan=2)
uri_entry.focus()

user_entry = Entry(width=36)
user_entry.grid(column=1, row=2, columnspan=2)

passw_entry = Entry(width=25, show="*")
passw_entry.grid(column=1, row=3)

# Button layout and config
passw_gen_button = Button(text="Generate", command=passw_gen)
passw_gen_button.grid(column=2, row=3)

add_passw_button = Button(text="Add", width=34, command=passw_save)
add_passw_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
