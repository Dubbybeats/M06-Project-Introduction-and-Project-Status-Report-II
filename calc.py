from tkinter import *


def button_press(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, END)


def subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, END)


def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)


def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, END)


def equal():
    second_number = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, f_num + float(second_number))

    if math == "subtraction":
        entry.insert(0, f_num - float(second_number))

    if math == "multiplication":
        entry.insert(0, f_num * float(second_number))

    if math == "division":
        entry.insert(0, f_num / float(second_number))


def clear():
    entry.delete(0, END)


def info_window():
    window = Toplevel()
    window.title("Info")
    window.geometry("300x200")
    window.configure(bg="dark blue")

    ascii_flame = '''
       (
        )
       (
     /  \ 
    |(_)| 
    /_\_\\
    '''

    info_label = Label(window, text="Final Project - Angel Yi", font=("Arial", 16), bg="dark blue", fg="white")
    info_label.pack(pady=10)

    flame_text = Text(window, height=8, width=20, bg="dark blue", fg="white", font=("Courier", 12))
    flame_text.insert(INSERT, ascii_flame)
    flame_text.pack(pady=5)

    close_button = Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)


def main_calculator():
    global window
    global entry

    window = Tk()
    window.title("Calculator")
    window.geometry("400x400")
    window.configure(bg="dark blue")

    entry = Entry(window, width=30, borderwidth=5, font=("Arial", 20))
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('0', 4, 1),
    ]

    for (text, row, col) in buttons:
        Button(window, text=text, font=("Arial", 20), padx=40, pady=20, bg="purple", fg="white", command=lambda t=text: button_press(t)).grid(row=row, column=col)

        Button(window, text="+", font=("Arial", 20), padx=40, pady=20, bg="orange", fg="white", command=add).grid(row=1, column=3)
    Button(window, text="-", font=("Arial", 20), padx=40, pady=20, bg="orange", fg="white", command=subtract).grid(row=2, column=3)
    Button(window, text="*", font=("Arial", 20), padx=40, pady=20, bg="orange", fg="white", command=multiply).grid(row=3, column=3)
    Button(window, text="/", font=("Arial", 20), padx=40, pady=20, bg="orange", fg="white", command=divide).grid(row=4, column=3)
    Button(window, text="=", font=("Arial", 20), padx=40, pady=20, bg="green", fg="white", command=equal).grid(row=4, column=2)
    Button(window, text="C", font=("Arial", 20), padx=40, pady=20, bg="red", fg="white", command=clear).grid(row=4, column=0)
    Button(window, text="Info", font=("Arial", 20), padx=40, pady=20, bg="gray", fg="white", command=info_window).grid(row=5, column=0, columnspan=4)

    window.mainloop()


main_calculator()
