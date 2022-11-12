import json
from tkinter import *
from tkinter import messagebox
import random



letters = ['a' ,"b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",'u','v','w','x','y','z','A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@',"#",'$','%','^','&','*','(',')']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    yoyo = 0
    word = ""

    while yoyo < 12:
        XXX = random.randint(0,2)
        yoyo +=1
        if XXX == 0:
            letter = letters[random.randint(0,len(letters)-1)]
            word += letter
        elif XXX == 1:
            letter = symbols[random.randint(0, len(symbols)-1)]
            word += letter
        elif XXX == 2:
            letter = str(random.randint(0, 9))
            word += letter
    entry3.delete(0,len(entry3.get()))
    entry3.insert(0,word)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = entry1.get()
    username = entry2.get()
    password = entry3.get()
    new_data = {
        website:    {
        "username": username,
        "password": password,
        }
    }



    if len(website) > 0 and len(username)> 0 and len(password) > 0:

        is_ok = messagebox.askokcancel(title=website, message=f"Data entered:\nUsername:{username}\nPassword:{password}\n\n Save data?")

        if is_ok:
            try:
                with open("password_list_json.json", mode="r") as file:

                    # Reading old data
                    rzecz = json.load(file)
                    # Updating old data with new data
                    rzecz.update(new_data)

                with open("password_list_json.json", mode="w") as file:

                    # saving updated data
                    json.dump(rzecz, file, indent=4)

            except FileNotFoundError:
                YOYO = {
        website:    {
        "username": 'username',
        "password": 'password',
        }
}
                with open("password_list_json.json", mode="w") as file:
                    json.dump(YOYO, file)

                with open("password_list_json.json", mode="r") as file:

                    # Reading old data
                    rzecz = json.load(file)
                    # Updating old data with new data
                    rzecz.update(new_data)

                with open("password_list_json.json", mode="w") as file:

                    # saving updated data
                    json.dump(rzecz, file, indent=4)

                #file.write(f"\n{website}  |  {username}  |  {password}")

            entry1.delete(0, END)
            entry3.delete(0, END)

    else:
        messagebox.showwarning(title="Element missing", message="Please fill all the information boxes before adding.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_button():
    website = entry1.get()
    try:
        with open("password_list_json.json", mode="r") as file:
            rzecz = json.load(file)
            name_found = 0
            for name in rzecz:
                if name == website:
                    messagebox.showwarning(title=(f"{website}"), message=f'Website: {website}\nUsername: {(rzecz[website]["username"])} \nPassword: {(rzecz[website]["password"])}')
                    name_found +=1
            if name_found == 0:
                messagebox.showwarning(title="Password not found", message="No password for this website saved.")
    except FileNotFoundError:
        messagebox.showwarning(title="Database empty", message="Database empty. Please, before searching, save website password.")

    #czytaj plik z hasłami
    #dla każdego z haseł spradź czy jest takie samo, jeśli tak to wyśpietl passy, jeśli nei wyświetl info, że nie ma





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20, bg="white")

### Canva

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=1)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

### LABELS
label0 = Label(text="")
label0.grid(column=0, row=0)

label1 = Label(text="Website:", anchor="w")
label1.grid(column=0, row=1)

label2 = Label(text="Email/Username:", anchor="w")
label2.grid(column=0, row=2)

label3 = Label(text="Password:", anchor="w")
label3.grid(column=0, row=3)

### ENTRY

entry1 = Entry(width=52, justify="left")
entry1.grid(column=1, row=1, columnspan=2, sticky="W")
entry1.focus()

entry2 = Entry(width=52, justify="left")
entry2.grid(column=1, row=2, columnspan=2, sticky="W")
entry2.insert(0,"tomasz@gmail.com")

entry3 = Entry(width=32, justify="left")
entry3.grid(column=1, row=3, sticky="W")

### BUTTON

button1 = Button(text="Generate Password", command=password_generator)
button1.grid(column=2, row=3, sticky="W")

button2 = Button(text="Add", width=44, command=save_password)
button2.grid(column=1, row=4, columnspan=2, sticky="W")

button3 = Button(text="Search", width=15, command=search_button)
button3.grid(column=2, row=1, sticky="W")


window.mainloop()
