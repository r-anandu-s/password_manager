from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ------Password Generator------ #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(4, 5))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 3))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 3))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------Save Data------ #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nClick OK to save or Cancel to "
                                                              f"try again.")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ------UI SETUP------ #


window = Tk()
window.title("Password Manager")
window.config(padx=35, pady=35)

canvas = Canvas(height=200, width=200)
lock = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)
email_lbl = Label(text="Email/Username:")
email_lbl.grid(row=2, column=0)
password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
