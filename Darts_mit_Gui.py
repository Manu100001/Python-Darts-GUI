#!/usr/bin/python3
"""
This script will help you with Darts

:author: Manuel Milde manuelmilde@gmx.net
:copyright: 2021 Manuel Milde
"""
import sqlite3
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os

flag_switch = False
months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November',
          'Dezember']


def call_database(checkout):
    """
    This function reads the database and shows the data on the gui
    :return:
    """

    connection = sqlite3.connect("Datenbanken/checkouts.db")
    access = connection.cursor()

    select = "SELECT number, first_dart, second_dart, third_dart FROM Checkouts;"
    access.execute(select)
    records = access.fetchall()

    list_checkouts = []

    for row in records:
        if str(row[0]) == checkout:
            liste = [row[1], row[2], row[3]]
            list_checkouts.append(liste)

    space = 0
    i = 0
    # clear all labels
    while i < 4:
        label_one = Label(gui, text="", fg="black", font=('Arial', 13, 'bold'))
        label_two = Label(gui, text="", fg="black", font=('Arial', 13, 'bold'))
        label_three = Label(gui, text="", fg="black", font=('Arial', 13, 'bold'))
        label_one.place(x=0, y=150 + space, width=120)
        label_two.place(x=0, y=170 + space, width=120)
        label_three.place(x=0, y=190 + space, width=120)
        space = space + 80
        i = i + 1

    space = 0
    # set all labels
    for item in list_checkouts:
        label_one = Label(gui, text="1.Dart: " + str(item[0]), fg="black", font=('Arial', 13, 'bold'))
        label_two = Label(gui, text="2.Dart: " + str(item[1]), fg="black", font=('Arial', 13, 'bold'))
        label_three = Label(gui, text="3.Dart: " + str(item[2]), fg="black", font=('Arial', 13, 'bold'))
        label_one.place(x=0, y=150 + space, width=120)
        label_two.place(x=0, y=170 + space, width=120)
        label_three.place(x=0, y=190 + space, width=120)
        space = space + 80


def button_exit():
    """
    This function creates an exit - button for the gui
    :return:
    """
    if not any(isinstance(window, Toplevel) for window in gui.winfo_children()):
        exit_window = Toplevel(gui)
        exit_window.geometry('250x150')
        exit_window.resizable(width=0, height=0)
        exit_window.title("Beenden?")

        label_exit = Label(exit_window, text="Spiel beenden?", font=('Arial', 11))
        button_ja = Button(exit_window, text="Ja", command=exit_window.quit, font=('Arial', 10, 'bold'), bg="white",
                           fg="green")
        button_nein = Button(exit_window, text="Nein", command=exit_window.destroy, font=('Arial', 10, 'bold'),
                             bg="white", fg="red")

        label_exit.place(x=80, y=0, width=100, height=50)
        button_ja.place(x=50, y=60, width=50, height=50)
        button_nein.place(x=150, y=60, width=50, height=50)

    else:
        messagebox.showinfo("Info", "You already clicked on \"Beenden\"!")


def button_checkout():
    """

    :return:
    """
    result = eingabefeld.get()
    eingabefeld.delete("0", "end")

    checkout_label = Label(gui, text="Checkout: " + str(result), fg="black", font=('Arial', 15, 'bold'))

    checkout_label.place(x=0, y=100, width=140)

    # call Database with checkout to get the checkout - ways
    call_database(result)


def button_inc_player_one():
    """

    :return:
    """
    anzahl = int(label_anzahl_legs_player_one['text'])
    inc = anzahl + 1
    label_anzahl_legs_player_one['text'] = inc

    result = label_anzahl_legs['text'] / 2
    result += 0.5
    int(result)

    if inc == result:
        info = "Player 1 gewonnen mit " + str(label_anzahl_legs_player_one['text']) + ":" + \
               str(label_anzahl_legs_player_two['text'])
        messagebox.showinfo("Info", info)
        save_button_best_of_legs()
        clear_legs_buttons()

    switch_button_function()


def button_dec_player_one():
    """

    :return:
    """
    anzahl = int(label_anzahl_legs_player_one['text'])

    if anzahl == 0:
        label_anzahl_legs_player_one['text'] = 0
    else:
        dec = anzahl - 1
        label_anzahl_legs_player_one['text'] = dec


def button_inc_player_two():
    """

    :return:
    """
    anzahl = int(label_anzahl_legs_player_two['text'])
    inc = anzahl + 1
    label_anzahl_legs_player_two['text'] = inc

    result = label_anzahl_legs['text'] / 2
    result += 0.5
    int(result)

    switch_button_function()

    if inc == result:
        info = "Player 2 gewonnen mit " + str(label_anzahl_legs_player_two['text']) + ":" + \
               str(label_anzahl_legs_player_one['text'])
        messagebox.showinfo("Info", info)
        save_button_best_of_legs()
        clear_legs_buttons()


def button_dec_player_two():
    """

    :return:
    """
    anzahl = int(label_anzahl_legs_player_two['text'])

    if anzahl == 0:
        label_anzahl_legs_player_two['text'] = 0
    else:
        dec = anzahl - 1
        label_anzahl_legs_player_two['text'] = dec


def clear_legs_buttons():
    """

    :return:
    """
    label_anzahl_legs_player_one['text'] = 0
    label_anzahl_legs_player_two['text'] = 0


def button_inc_legs_player_one_function():
    """

    :return:
    """
    amount1 = int(label_hidden_one['text'])
    amount2 = amount1 + 1
    label_hidden_one['text'] = amount2

    anzahl = int(label_anzahl_legs_for_sets_player_one['text'])
    inc = anzahl + 1

    switch_button_function_sets()

    if inc == 3:
        amount = int(label_anzahl_sets_player_one['text'])
        amount = amount + 1
        label_anzahl_sets_player_one['text'] = amount

        anzahl = label_anzahl_legs_for_sets_player_one['text'] + 1
        anzahl += label_anzahl_legs_for_sets_player_two['text']

        if anzahl % 2 == 0:
            switch_button_function_sets()

        label_anzahl_legs_for_sets_player_one['text'] = 0
        label_anzahl_legs_for_sets_player_two['text'] = 0

    else:

        label_anzahl_legs_for_sets_player_one['text'] = inc

    if label_anzahl_sets_player_one['text'] == label_anzahl_sets['text']:
        messagebox.showinfo("Info", "Winner Player 1.")
        save_button_sets()
        clear_legs_for_sets_buttons()
        clear_sets_button()


def button_dec_legs_player_one_function():
    """

    :return:
    """
    anzahl = int(label_anzahl_legs_for_sets_player_one['text'])

    if anzahl == 0:
        label_anzahl_legs_for_sets_player_one['text'] = 0
    else:
        dec = anzahl - 1
        label_anzahl_legs_for_sets_player_one['text'] = dec


def button_inc_legs_player_two_function():
    """

    :return:
    """
    amount3 = int(label_hidden_two['text'])
    amount4 = amount3 + 1
    label_hidden_two['text'] = amount4

    anzahl = int(label_anzahl_legs_for_sets_player_two['text'])
    inc = anzahl + 1

    switch_button_function_sets()

    if inc == 3:
        amount = int(label_anzahl_sets_player_two['text'])
        amount = amount + 1
        label_anzahl_sets_player_two['text'] = amount

        anzahl = label_anzahl_legs_for_sets_player_one['text']
        anzahl += label_anzahl_legs_for_sets_player_two['text'] + 1

        if anzahl % 2 == 0:
            switch_button_function_sets()

        label_anzahl_legs_for_sets_player_one['text'] = 0
        label_anzahl_legs_for_sets_player_two['text'] = 0

    else:

        label_anzahl_legs_for_sets_player_two['text'] = inc

    if label_anzahl_sets_player_two['text'] == label_anzahl_sets['text']:
        messagebox.showinfo("Info", "Winner Player 2.")
        save_button_sets()
        clear_legs_for_sets_buttons()
        clear_sets_button()


def button_dec_legs_player_two_function():
    """

    :return:
    """
    anzahl = int(label_anzahl_legs_for_sets_player_two['text'])

    if anzahl == 0:
        label_anzahl_legs_for_sets_player_two['text'] = 0
    else:
        dec = anzahl - 1
        label_anzahl_legs_for_sets_player_two['text'] = dec


def clear_legs_for_sets_buttons():
    """

    :return:
    """
    label_anzahl_legs_for_sets_player_one['text'] = 0
    label_anzahl_legs_for_sets_player_two['text'] = 0
    label_hidden_one['text'] = 0
    label_hidden_two['text'] = 0


def clear_sets_button():
    """

    :return:
    """
    label_anzahl_sets_player_one['text'] = 0
    label_anzahl_sets_player_two['text'] = 0


def clear_all_button():
    """

    :return:
    """
    label_anzahl_legs_for_sets_player_one['text'] = 0
    label_anzahl_legs_for_sets_player_two['text'] = 0
    label_anzahl_sets_player_one['text'] = 0
    label_anzahl_sets_player_two['text'] = 0
    label_hidden_one['text'] = 0
    label_hidden_two['text'] = 0


def save_button_sets():
    """

    :return:
    """
    sets_one = label_anzahl_sets_player_one['text']
    sets_two = label_anzahl_sets_player_two['text']
    legs_one = label_hidden_one['text']
    legs_two = label_hidden_two['text']

    input = "# Spielstand \n\nSets Player 1: " + str(sets_one) + "\nSets Player 2: " + str(sets_two)
    input += "\n\n# Anzahl insgesamt gewonnene Legs\nPlayer 1: " + str(legs_one) + "\nPlayer 2: " + str(legs_two)

    # create directory
    if not os.path.isdir("Spielstände"):
        os.mkdir("Spielstände")

    if not os.path.isdir("Spielstände/Sets"):
        os.mkdir("Spielstände/Sets")

    # current year
    current_year = datetime.now().strftime('%Y')
    if not os.path.isdir("Spielstände/Sets/" + current_year):
        os.mkdir("Spielstände/Sets/" + current_year)

    # current month
    current_month = datetime.now().strftime('%m')
    month_name = months[int(current_month) - 1]
    if not os.path.isdir("Spielstände/Sets/" + current_year + "/" + month_name):
        os.mkdir("Spielstände/Sets/" + current_year + "/" + month_name)

    # current day
    current_day = int(datetime.now().strftime('%d'))
    date = str(current_day) + "." + str(current_month)
    if not os.path.isdir("Spielstände/Sets/" + current_year + "/" + month_name + "/" + date):
        os.mkdir("Spielstände/Sets/" + current_year + "/" + month_name + "/" + date)

    # create new score - file
    time = datetime.now().strftime('%H-%M-%S')

    path = "Spielstände/Sets/" + current_year + "/" + month_name + "/" + date + "/" + time + ".txt"
    with open(path, 'w') as file:
        file.write(input)

    messagebox.showinfo("Info", "Spielstand gespeichert!")


def inc_legs():
    """

    :return:
    """
    number = label_anzahl_legs['text']
    number = number + 2
    label_anzahl_legs['text'] = number


def dec_legs():
    """

    :return:
    """
    number = label_anzahl_legs['text']

    if number == 3:
        return
    else:
        number = number - 2
        label_anzahl_legs['text'] = number


def clear_best_of():
    """

    :return:
    """
    label_anzahl_legs['text'] = 3


def save_button_best_of_legs():
    """

    :return:
    """
    legs_one = label_anzahl_legs_player_one['text']
    legs_two = label_anzahl_legs_player_two['text']

    input = "# Spielstand \n\nLegs Player 1: " + str(legs_one) + "\nLegs Player 2: " + str(legs_two)

    # create directory
    if not os.path.isdir("Spielstände"):
        os.mkdir("Spielstände")

    if not os.path.isdir("Spielstände/Best of Legs"):
        os.mkdir("Spielstände/Best of Legs")

    # current year
    current_year = datetime.now().strftime('%Y')
    if not os.path.isdir("Spielstände/Best of Legs/" + current_year):
        os.mkdir("Spielstände/Best of Legs/" + current_year)

    # current month
    current_month = datetime.now().strftime('%m')
    month_name = months[int(current_month) - 1]

    if not os.path.isdir("Spielstände/Best of Legs/" + current_year + "/" + month_name):
        os.mkdir("Spielstände/Best of Legs/" + current_year + "/" + month_name)

    # current day
    current_day = int(datetime.now().strftime('%d'))
    date = str(current_day) + "." + str(current_month)

    if not os.path.isdir("Spielstände/Best of Legs/" + current_year + "/" + month_name + "/" + date):
        os.mkdir("Spielstände/Best of Legs/" + current_year + "/" + month_name + "/" + date)

    # create new score - file
    time = datetime.now().strftime('%H-%M-%S')

    path = "Spielstände/Best of Legs/" + current_year + "/" + month_name + "/" + date + "/" + time + ".txt"
    with open(path, 'w') as file:
        file.write(input)

    messagebox.showinfo("Info", "Spielstand gespeichert!")


def inc_sets():
    """

    :return:
    """
    number = label_anzahl_sets['text']
    number = number + 1
    label_anzahl_sets['text'] = number


def dec_sets():
    """

    :return:
    """
    number = label_anzahl_sets['text']

    if number == 1:
        return
    else:
        number = number - 1
        label_anzahl_sets['text'] = number


def clear_first_to_sets():
    """

    :return:
    """
    label_anzahl_sets['text'] = 1


def switch_button():
    """

    :return:
    """
    if p1_switch['bg'] == "white":
        p1_switch['bg'] = "yellow"
        p2_switch['bg'] = "white"
    else:
        p1_switch['bg'] = "white"
        p2_switch['bg'] = "yellow"


def switch_button_function():
    """

    :return:
    """
    if p1_switch['bg'] == "white":
        p1_switch['bg'] = "yellow"
        p2_switch['bg'] = "white"
    else:
        p1_switch['bg'] = "white"
        p2_switch['bg'] = "yellow"


def switch_button_function_sets():
    """

    :return:
    """
    if p1_switch_sets['bg'] == "white":
        p1_switch_sets['bg'] = "yellow"
        p2_switch_sets['bg'] = "white"
    else:
        p1_switch_sets['bg'] = "white"
        p2_switch_sets['bg'] = "yellow"


def switch_button_sets():
    """

    :return:
    """
    if p1_switch_sets['bg'] == "white":
        p1_switch_sets['bg'] = "yellow"
        p2_switch_sets['bg'] = "white"
    else:
        p1_switch_sets['bg'] = "white"
        p2_switch_sets['bg'] = "yellow"


if __name__ == "__main__":
    gui = Tk()
    gui.geometry('700x500')
    gui.resizable(width=0, height=0)
    gui.title("Dart - User Interface")

    # exit - buttons
    exit_button = Button(gui, text="Beenden", command=button_exit, fg="black", bg="lightgreen",
                         font=('Arial', 10, 'bold'))
    exit_button.place(x=598, y=0, height=80, width=100)

    # checkout - button
    checkout_button = Button(gui, text="Go!", command=button_checkout, fg="red", bg="black", font=('Arial', 10))
    checkout_button.place(x=80, y=60, height=35, width=35)

    # checkout
    welcome_label = Label(gui, text="Geben Sie ihr Checkout ein:", fg="black", font=('Arial', 10, 'bold'))
    welcome_label.place(x=0, y=0, height=60, width=200)

    eingabefeld = Entry(gui, bd=5, font=('Arial', 20))
    eingabefeld.place(x=0, y=60, width=80, height=40)

    # nur legs
    # labels - legs - text
    label_legs_player_one = Label(gui, text="Legs Player 1: ", fg="black", font=('Arial', 13, 'bold'))
    label_legs_player_two = Label(gui, text="Legs Player 2: ", fg="black", font=('Arial', 13, 'bold'))

    label_legs_player_one.place(x=250, y=80, height=30)
    label_legs_player_two.place(x=250, y=130, height=30)

    # labels - legs - anzeige Ziffer
    label_anzahl_legs_player_one = Label(gui, text=0, fg="black", font=('Arial', 13, 'bold'))
    label_anzahl_legs_player_two = Label(gui, text=0, fg="black", font=('Arial', 13, 'bold'))

    label_anzahl_legs_player_one.place(x=375, y=80, height=30)
    label_anzahl_legs_player_two.place(x=375, y=130, height=30)

    # buttons + und -
    button_inc_legs_player_one = Button(gui, text="+", fg="black", bg="lightgreen", font=('Arial', 13),
                                        command=button_inc_player_one)
    button_dec_legs_player_one = Button(gui, text="-", fg="black", bg="red", font=('Arial', 13),
                                        command=button_dec_player_one)

    button_inc_legs_player_two = Button(gui, text="+", fg="black", bg="lightgreen", font=('Arial', 13),
                                        command=button_inc_player_two)
    button_dec_legs_player_two = Button(gui, text="-", fg="black", bg="red", font=('Arial', 13),
                                        command=button_dec_player_two)

    button_clear_legs = Button(gui, text="Clear", font=('Arial', 13, 'bold'), bg="lightblue",
                               command=clear_legs_buttons)

    # buttons out
    button_inc_legs_player_one.place(x=410, y=80, height=30, width=30)
    button_dec_legs_player_one.place(x=450, y=80, height=30, width=30)

    button_inc_legs_player_two.place(x=410, y=130, height=30, width=30)
    button_dec_legs_player_two.place(x=450, y=130, height=30, width=30)

    button_clear_legs.place(x=520, y=105, height=30, width=60)

    # label for separating
    label_separating = Label(gui, text="-----------------------------------------------------------------------------"
                                       "-----------------------------")
    label_separating.place(x=150, y=205)

    # legs and sets - below
    # here all for sets and legs
    label_legs_for_sets_player_one = Label(gui, text="Legs Player 1: ", fg="black", font=('Arial', 13, 'bold'))
    label_legs_for_sets_player_two = Label(gui, text="Legs Player 2: ", fg="black", font=('Arial', 13, 'bold'))

    label_sets_player_one = Label(gui, text="Sets Player 1: ", fg="black", font=('Arial', 13, 'bold'))
    label_sets_player_two = Label(gui, text="Sets Player 2: ", fg="black", font=('Arial', 13, 'bold'))

    label_anzahl_legs_for_sets_player_one = Label(gui, text=0, fg="black", font=('Arial', 13, 'bold'))
    label_anzahl_legs_for_sets_player_two = Label(gui, text=0, fg="black", font=('Arial', 13, 'bold'))
    label_anzahl_sets_player_one = Label(gui, text=0, fg="black", font=('Arial', 13, 'bold'))
    label_anzahl_sets_player_two = Label(gui, text=0, fg="black", font=('Arial', 13, 'bold'))

    label_legs_for_sets_player_one.place(x=250, y=300)
    label_legs_for_sets_player_two.place(x=250, y=350)
    label_sets_player_one.place(x=250, y=400)
    label_sets_player_two.place(x=250, y=450)

    label_anzahl_legs_for_sets_player_one.place(x=375, y=300)
    label_anzahl_legs_for_sets_player_two.place(x=375, y=350)
    label_anzahl_sets_player_one.place(x=375, y=400)
    label_anzahl_sets_player_two.place(x=375, y=450)

    button_inc_legs_for_sets_player_one = Button(gui, text="+", fg="black", bg="lightgreen", font=('Arial', 13),
                                                 command=button_inc_legs_player_one_function)
    button_dec_legs_for_sets_player_one = Button(gui, text="-", fg="black", bg="red", font=('Arial', 13),
                                                 command=button_dec_legs_player_one_function)

    # buttons for player two
    button_inc_legs_for_sets_player_two = Button(gui, text="+", fg="black", bg="lightgreen", font=('Arial', 13),
                                                 command=button_inc_legs_player_two_function)
    button_dec_legs_for_sets_player_two = Button(gui, text="-", fg="black", bg="red", font=('Arial', 13),
                                                 command=button_dec_legs_player_two_function)

    button_clear_legs = Button(gui, text="Clear", font=('Arial', 13, 'bold'), bg="lightblue",
                               command=clear_legs_buttons)

    button_inc_legs_for_sets_player_one.place(x=410, y=300, height=30, width=30)
    button_dec_legs_for_sets_player_one.place(x=450, y=300, height=30, width=30)
    button_inc_legs_for_sets_player_two.place(x=410, y=350, height=30, width=30)
    button_dec_legs_for_sets_player_two.place(x=450, y=350, height=30, width=30)

    button_clear_all = Button(gui, text="Clear all", font=('Arial', 13, 'bold'), bg="#FF6961",
                              command=clear_all_button)

    button_clear_all.place(x=520, y=450)

    # button_save = Button(gui, text="Save score", font=('Arial', 13, 'bold'), bg="yellow", command=save_button_sets)
    # button_save.place(x=170, y=445)

    label_hidden_one = Label(gui, text=0)
    label_hidden_two = Label(gui, text=0)

    # label best of legs
    label_best_of = Label(gui, text="Best of ", font=('Arial', 13, 'bold'))
    label_anzahl_legs = Label(gui, text=3, font=('Arial', 13, 'bold'))
    label_legs = Label(gui, text="Legs", font=('Arial', 13, 'bold'))

    label_best_of.place(x=250, y=20)
    label_anzahl_legs.place(x=320, y=20)
    label_legs.place(x=350, y=20)

    inc_legs = Button(gui, text="+", fg="black", bg="lightgreen", font=('Arial', 13),
                      command=inc_legs)
    dec_legs = Button(gui, text="-", fg="black", bg="red", font=('Arial', 13),
                      command=dec_legs)

    inc_legs.place(x=410, y=20, height=30, width=30)
    dec_legs.place(x=450, y=20, height=30, width=30)

    clear_best_of = Button(gui, text="Clear", fg="black", bg="lightblue", font=('Arial', 13, 'bold'),
                           command=clear_best_of)

    clear_best_of.place(x=520, y=20, height=30, width=60)

    # button_save_best_of_legs = Button(gui, text="Save score", font=('Arial', 13, 'bold'), bg="yellow",
    #   command=save_button_best_of_legs)
    # button_save_best_of_legs.place(x=250, y=170)

    # label best of legs
    label_first_to_sets = Label(gui, text="First to ", font=('Arial', 13, 'bold'))
    label_anzahl_sets = Label(gui, text=1, font=('Arial', 13, 'bold'))
    label_sets = Label(gui, text="Sets", font=('Arial', 13, 'bold'))

    label_first_to_sets.place(x=250, y=250)
    label_anzahl_sets.place(x=320, y=250)
    label_sets.place(x=350, y=250)

    inc_legs = Button(gui, text="+", fg="black", bg="lightgreen", font=('Arial', 13),
                      command=inc_sets)
    dec_legs = Button(gui, text="-", fg="black", bg="red", font=('Arial', 13),
                      command=dec_sets)

    inc_legs.place(x=410, y=250, height=30, width=30)
    dec_legs.place(x=450, y=250, height=30, width=30)

    clear_first_to_sets = Button(gui, text="Clear", fg="black", bg="lightblue", font=('Arial', 13, 'bold'),
                                 command=clear_first_to_sets)

    clear_first_to_sets.place(x=520, y=250, height=30, width=60)

    p1_switch = Label(gui, text="P1", fg="black", bg="yellow", font=('Arial', 13, 'bold'))
    p1_switch.place(x=250, y=175)

    switch_button = Button(gui, text="Switch", fg="black", font=('Arial', 13, 'bold'), command=switch_button)
    switch_button.place(x=285, y=175, height=25)

    p2_switch = Label(gui, text="P2", fg="black", bg="white", font=('Arial', 13, 'bold'))
    p2_switch.place(x=360, y=175)

    # new switch - button for sets

    p1_switch_sets = Label(gui, text="P1", fg="black", bg="yellow", font=('Arial', 13, 'bold'))
    p1_switch_sets.place(x=520, y=310)

    switch_button_sets = Button(gui, text="Switch", fg="black", font=('Arial', 13, 'bold'), command=switch_button_sets)
    switch_button_sets.place(x=555, y=310, height=25)

    p2_switch_sets = Label(gui, text="P2", fg="black", bg="white", font=('Arial', 13, 'bold'))
    p2_switch_sets.place(x=630, y=310)

    gui.mainloop()

    sys.exit(0)
