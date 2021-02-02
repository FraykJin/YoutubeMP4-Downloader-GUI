from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] \
                    + [random.choice(symbols) for char in range(nr_symbols)] \
                    + [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, f'{password}')
    pyperclip.copy(f'{password}')


# ---------------------------- SAVE PASSWORD ------------------------------- #


# Function for ADD BUTTON
def add():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Completez les champs vides.")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            input_email.delete(0, 'end')
            input_website.delete(0, 'end')
            input_password.delete(0, 'end')
        # else:
        #     messagebox.showwarning(title="Missing Infos", message="Complete the missing informations")

# --------------------------- SEARCH PASSWORD -------------------------#


def find_password():

    try:
        with open('data.json', 'r') as file:
            data_dict = json.load(file)
            website = input_website.get()
            content = data_dict[website]
    except KeyError:
        messagebox.showinfo(title='Show Info', message=f'No password registered for the website:\n{website}')
    except FileNotFoundError:
        messagebox.showinfo(title='Show Info', message='No Data File Found')

    else:
        email = content['email']
        password = content['password']
        messagebox.showinfo(title='Vos informations', message=f"Site: {website}\n"
                            f"Email: {email}\n"
                            f"Password: {password}")
        pyperclip.copy(f"{password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')


canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
photo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo_img)
canvas.grid(row=0, column=1)

# Website
label_website = Label(text='Website:')
label_website.grid(row=1, column=0)

input_website = Entry(width=22)
input_website.grid(row=1, column=1)
input_website.focus()
# Email/Username
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

input_email = Entry(width=42)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, '@gmail.com')
# Password
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

input_password = Entry(width=22)
input_password.grid(row=3, column=1)

button_password = Button(text='Generate Password', command=generate_password)
button_password.grid(row=3, column=2)

# Add Button
button_add = Button(text="Add", width=44, command=add)
button_add.grid(row=4, column=1, columnspan=2)

# SEARCH BUTTON
button_search = Button(text="Search", width=15, command=find_password)
button_search.grid(row=1, column=2)

window.mainloop()
