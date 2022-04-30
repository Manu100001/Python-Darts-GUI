#!/usr/bin/python3
# pylint: disable=C0302
"""
This script creates a special tournament tree
Winner - Loser - Game

:author: Manuel Milde manuelmilde@gmx.net
:copyright: 2022 Manuel Milde
"""
# import os
import random
from tkinter import Tk
from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox
# from datetime import datetime
# from openpyxl import Workbook
# from openpyxl.styles import PatternFill

all_player_names = []


def button_exit():
    """
    This function creates an exit - button for the gui
    :return:
    """
    if not any(isinstance(window, Toplevel) for window in gui.winfo_children()):
        exit_window = Toplevel(gui)
        exit_window.geometry('250x150')
        exit_window.resizable(width=False, height=False)
        exit_window.title("Stop?")

        label_exit = Label(exit_window, text="End game?", font=('Arial', 11))
        button_yes = Button(exit_window, text="Yes", command=exit_window.quit,
                            font=('Arial', 10, 'bold'), bg="white",
                            fg="green")
        button_no = Button(exit_window, text="No", command=exit_window.destroy,
                           font=('Arial', 10, 'bold'),
                           bg="white", fg="red")

        label_exit.place(x=80, y=0, width=100, height=50)
        button_yes.place(x=50, y=60, width=50, height=50)
        button_no.place(x=150, y=60, width=50, height=50)

    else:
        messagebox.showinfo("Info", "You already clicked on \"Stop\"!")


def start():
    """

    """
    start_button.pack()
    start_button.pack_forget()

    label_welcome.pack()
    label_welcome.pack_forget()

    input_name1.place(x=337.5, y=132.5, height=30, width=250)
    input_name2.place(x=337.5, y=182.5, height=30, width=250)
    input_name3.place(x=337.5, y=232.5, height=30, width=250)
    input_name4.place(x=337.5, y=282.5, height=30, width=250)

    input_name5.place(x=337.5, y=332.5, height=30, width=250)
    input_name6.place(x=337.5, y=382.5, height=30, width=250)
    input_name7.place(x=337.5, y=432.5, height=30, width=250)
    input_name8.place(x=337.5, y=482.5, height=30, width=250)

    input_name9.place(x=687.5, y=132.5, height=30, width=250)
    input_name10.place(x=687.5, y=182.5, height=30, width=250)
    input_name11.place(x=687.5, y=232.5, height=30, width=250)
    input_name12.place(x=687.5, y=282.5, height=30, width=250)
    input_name13.place(x=687.5, y=332.5, height=30, width=250)
    input_name14.place(x=687.5, y=382.5, height=30, width=250)
    input_name15.place(x=687.5, y=432.5, height=30, width=250)
    input_name16.place(x=687.5, y=482.5, height=30, width=250)

    label_name_order1.pack()
    label_name_order2.pack()
    button_switch_order.pack()
    label_name_order1.place(x=637.5, y=30, height=30, width=100)
    label_name_order2.place(x=537.5, y=30, height=30, width=100)
    button_switch_order.place(x=587.5, y=0, height=30, width=100)

    # enable label with entering all names
    label_info_names.pack()
    label_info_names.place(x=537.5, y=82.5, height=30, width=200)

    # enable button for next step and read the given names
    button_enter_names.pack()
    button_enter_names.place(x=1175, y=282.5, height=30, width=100)


def switch_order():
    """
    This function switches the mode between random or entered order
    for the player names in the tournament tree
    :return:
    """
    if label_name_order1['bg'] == "yellow":
        label_name_order1['bg'] = "white"
        label_name_order2['bg'] = "yellow"

    elif label_name_order2['bg'] == "yellow":
        label_name_order2['bg'] = "white"
        label_name_order1['bg'] = "yellow"


def disable_input_fields():
    """

    """
    input_name1.pack()
    input_name2.pack()
    input_name3.pack()
    input_name4.pack()
    input_name5.pack()
    input_name6.pack()
    input_name7.pack()
    input_name8.pack()
    input_name9.pack()
    input_name10.pack()
    input_name11.pack()
    input_name12.pack()
    input_name13.pack()
    input_name14.pack()
    input_name15.pack()
    input_name16.pack()

    input_name1.pack_forget()
    input_name2.pack_forget()
    input_name3.pack_forget()
    input_name4.pack_forget()
    input_name5.pack_forget()
    input_name6.pack_forget()
    input_name7.pack_forget()
    input_name8.pack_forget()
    input_name9.pack_forget()
    input_name10.pack_forget()
    input_name11.pack_forget()
    input_name12.pack_forget()
    input_name13.pack_forget()
    input_name14.pack_forget()
    input_name15.pack_forget()
    input_name16.pack_forget()


def check_names():
    """
    This function checks if all names have been entered
    :return:
    """
    name1 = input_name1.get()
    name2 = input_name2.get()
    name3 = input_name3.get()
    name4 = input_name4.get()
    name5 = input_name5.get()
    name6 = input_name6.get()
    name7 = input_name7.get()
    name8 = input_name8.get()
    name9 = input_name9.get()
    name10 = input_name10.get()
    name11 = input_name11.get()
    name12 = input_name12.get()
    name13 = input_name13.get()
    name14 = input_name14.get()
    name15 = input_name15.get()
    name16 = input_name16.get()

    if name1 == "" or name2 == "" or name3 == "" or name4 == "":
        messagebox.showinfo("Error", "Not all names were entered.")
        return

    if name5 == "" or name6 == "" or name7 == "" or name8 == "":
        messagebox.showinfo("Error", "Not all names were entered.")
        return

    if name9 == "" or name10 == "" or name11 == "" or name12 == "":
        messagebox.showinfo("Error", "Not all names were entered.")
        return

    if name13 == "" or name14 == "" or name15 == "" or name16 == "":
        messagebox.showinfo("Error", "Not all names were entered.")
        return

    all_player_names.append(name1)
    all_player_names.append(name2)
    all_player_names.append(name3)
    all_player_names.append(name4)
    all_player_names.append(name5)
    all_player_names.append(name6)
    all_player_names.append(name7)
    all_player_names.append(name8)
    all_player_names.append(name9)
    all_player_names.append(name10)
    all_player_names.append(name11)
    all_player_names.append(name12)
    all_player_names.append(name13)
    all_player_names.append(name14)
    all_player_names.append(name15)
    all_player_names.append(name16)

    button_enter_names.pack()
    button_enter_names.pack_forget()

    # disable input fields
    disable_input_fields()

    label_info_names.pack()
    label_info_names.pack_forget()

    label_name_order1.pack()
    label_name_order2.pack()
    button_switch_order.pack()

    label_name_order1.pack_forget()
    label_name_order2.pack_forget()
    button_switch_order.pack_forget()

    take_names()


def take_names():
    """
    This function writes the names into the tournament tree
    :return:
    """
    # check if random order
    if label_name_order1['bg'] == "yellow":
        numbers = []
        while len(numbers) < 16:

            random_number = round(random.uniform(0, 15))
            if random_number not in numbers:
                numbers.append(random_number)

        label_player1_name['text'] = all_player_names[numbers[0]]
        label_player2_name['text'] = all_player_names[numbers[1]]
        label_player3_name['text'] = all_player_names[numbers[2]]
        label_player4_name['text'] = all_player_names[numbers[3]]
        label_player5_name['text'] = all_player_names[numbers[4]]
        label_player6_name['text'] = all_player_names[numbers[5]]
        label_player7_name['text'] = all_player_names[numbers[6]]
        label_player8_name['text'] = all_player_names[numbers[7]]

        label_player9_name['text'] = all_player_names[numbers[8]]
        label_player10_name['text'] = all_player_names[numbers[9]]
        label_player11_name['text'] = all_player_names[numbers[10]]
        label_player12_name['text'] = all_player_names[numbers[11]]
        label_player13_name['text'] = all_player_names[numbers[12]]
        label_player14_name['text'] = all_player_names[numbers[13]]
        label_player15_name['text'] = all_player_names[numbers[14]]
        label_player16_name['text'] = all_player_names[numbers[15]]

        start_tree()

    else:
        take_names2()


def take_names2():
    """
    This function is called by take_names
    :return:
    """
    label_player1_name['text'] = all_player_names[0]
    label_player2_name['text'] = all_player_names[1]
    label_player3_name['text'] = all_player_names[2]
    label_player4_name['text'] = all_player_names[3]
    label_player5_name['text'] = all_player_names[4]
    label_player6_name['text'] = all_player_names[5]
    label_player7_name['text'] = all_player_names[6]
    label_player8_name['text'] = all_player_names[7]
    label_player9_name['text'] = all_player_names[8]
    label_player10_name['text'] = all_player_names[9]
    label_player11_name['text'] = all_player_names[10]
    label_player12_name['text'] = all_player_names[11]
    label_player13_name['text'] = all_player_names[12]
    label_player14_name['text'] = all_player_names[13]
    label_player15_name['text'] = all_player_names[14]
    label_player16_name['text'] = all_player_names[15]

    start_tree()


def start_tree():
    """
    This function starts the tournament tree after the mode was chosen
    :return:
    """
    start_button.pack()
    start_button.pack_forget()

    # place all 16 player names
    label_player1_name.place(x=850, y=10, height=30, width=130)
    label_player2_name.place(x=850, y=45, height=30, width=130)
    label_player3_name.place(x=850, y=85, height=30, width=130)
    label_player4_name.place(x=850, y=120, height=30, width=130)
    label_player5_name.place(x=850, y=160, height=30, width=130)
    label_player6_name.place(x=850, y=195, height=30, width=130)
    label_player7_name.place(x=850, y=235, height=30, width=130)
    label_player8_name.place(x=850, y=270, height=30, width=130)
    label_player9_name.place(x=850, y=310, height=30, width=130)
    label_player10_name.place(x=850, y=345, height=30, width=130)
    label_player11_name.place(x=850, y=385, height=30, width=130)
    label_player12_name.place(x=850, y=420, height=30, width=130)
    label_player13_name.place(x=850, y=460, height=30, width=130)
    label_player14_name.place(x=850, y=495, height=30, width=130)
    label_player15_name.place(x=850, y=535, height=30, width=130)
    label_player16_name.place(x=850, y=570, height=30, width=130)

    # place all 8 first losers # middle of 2 players (height = 17.5)
    label_loser1_name.place(x=700, y=27.5, height=30, width=130)
    label_loser2_name.place(x=700, y=102.5, height=30, width=130)
    label_loser3_name.place(x=700, y=177.5, height=30, width=130)
    label_loser4_name.place(x=700, y=252.5, height=30, width=130)
    label_loser5_name.place(x=700, y=327.5, height=30, width=130)
    label_loser6_name.place(x=700, y=402.5, height=30, width=130)
    label_loser7_name.place(x=700, y=477.5, height=30, width=130)
    label_loser8_name.place(x=700, y=552.5, height=30, width=130)
    # button_enter_results.pack()
    # button_enter_results.place(x=5, y=10, height=30, width=130)


if __name__ == "__main__":
    # configure the window to generate
    gui = Tk()
    gui.geometry('1275x645')
    gui.resizable(width=False, height=False)
    gui.title("Darts - Tournament tree")
    gui.configure(background='grey')

    # define the exit - button
    exit_button = Button(gui, text="End game", command=button_exit, fg="black", bg="lightgreen",
                         font=('Arial', 10, 'bold'))
    exit_button.place(x=1175, y=0, height=80, width=100)

    # label for introducing and welcome
    label_welcome = Label(gui, text="Welcome to the darts winner - loser - game!\n"
                                    " Please press Continue to start.", bg="grey",
                          font=('Arial', 14))
    label_welcome.place(x=397.5, y=20, height=50, width=600)

    # define start-button after the mode was chosen the tournament tree can be created
    start_button = Button(gui, text="Continue", bg="lightgreen", font=('Arial', 10),
                          command=start)
    start_button.place(x=637.5, y=100, height=30, width=100)

    # define labels, text-fields and buttons for name input
    input_name1 = Entry(gui, bd=1, font=('Arial', 13))
    input_name2 = Entry(gui, bd=1, font=('Arial', 13))
    input_name3 = Entry(gui, bd=1, font=('Arial', 13))
    input_name4 = Entry(gui, bd=1, font=('Arial', 13))
    input_name5 = Entry(gui, bd=1, font=('Arial', 13))
    input_name6 = Entry(gui, bd=1, font=('Arial', 13))
    input_name7 = Entry(gui, bd=1, font=('Arial', 13))
    input_name8 = Entry(gui, bd=1, font=('Arial', 13))

    input_name9 = Entry(gui, bd=1, font=('Arial', 13))
    input_name10 = Entry(gui, bd=1, font=('Arial', 13))
    input_name11 = Entry(gui, bd=1, font=('Arial', 13))
    input_name12 = Entry(gui, bd=1, font=('Arial', 13))
    input_name13 = Entry(gui, bd=1, font=('Arial', 13))
    input_name14 = Entry(gui, bd=1, font=('Arial', 13))
    input_name15 = Entry(gui, bd=1, font=('Arial', 13))
    input_name16 = Entry(gui, bd=1, font=('Arial', 13))

    # define button and label for name - order
    label_name_order1 = Label(gui, text="Random order", bg="yellow", font=('Arial', 10))
    label_name_order2 = Label(gui, text="Entered order", bg="white", font=('Arial', 10))
    button_switch_order = Button(gui, text="Choose order", bg="lightgreen",
                                 font=('Arial', 10), command=switch_order)

    # define label for entering names
    label_info_names = Label(gui, text="Please enter all names", font=('Arial', 10))

    # define button for entering names

    button_enter_names = Button(gui, text="Continue", bg="lightgreen",
                                font=('Arial', 10), command=check_names)

    # define start-labels for 16 player names
    label_player1_name = Label(gui, text="", font=('Arial', 10))
    label_player2_name = Label(gui, text="", font=('Arial', 10))
    label_player3_name = Label(gui, text="", font=('Arial', 10))
    label_player4_name = Label(gui, text="", font=('Arial', 10))
    label_player5_name = Label(gui, text="", font=('Arial', 10))
    label_player6_name = Label(gui, text="", font=('Arial', 10))
    label_player7_name = Label(gui, text="", font=('Arial', 10))
    label_player8_name = Label(gui, text="", font=('Arial', 10))

    label_player9_name = Label(gui, text="", font=('Arial', 10))
    label_player10_name = Label(gui, text="", font=('Arial', 10))
    label_player11_name = Label(gui, text="", font=('Arial', 10))
    label_player12_name = Label(gui, text="", font=('Arial', 10))
    label_player13_name = Label(gui, text="", font=('Arial', 10))
    label_player14_name = Label(gui, text="", font=('Arial', 10))
    label_player15_name = Label(gui, text="", font=('Arial', 10))
    label_player16_name = Label(gui, text="", font=('Arial', 10))

    label_result_player1 = Label(gui, text="", font=('Arial', 10))
    label_result_player2 = Label(gui, text="", font=('Arial', 10))
    label_result_player3 = Label(gui, text="", font=('Arial', 10))
    label_result_player4 = Label(gui, text="", font=('Arial', 10))
    label_result_player5 = Label(gui, text="", font=('Arial', 10))
    label_result_player6 = Label(gui, text="", font=('Arial', 10))
    label_result_player7 = Label(gui, text="", font=('Arial', 10))
    label_result_player8 = Label(gui, text="", font=('Arial', 10))

    label_result_player9 = Label(gui, text="", font=('Arial', 10))
    label_result_player10 = Label(gui, text="", font=('Arial', 10))
    label_result_player11 = Label(gui, text="", font=('Arial', 10))
    label_result_player12 = Label(gui, text="", font=('Arial', 10))
    label_result_player13 = Label(gui, text="", font=('Arial', 10))
    label_result_player14 = Label(gui, text="", font=('Arial', 10))
    label_result_player15 = Label(gui, text="", font=('Arial', 10))
    label_result_player16 = Label(gui, text="", font=('Arial', 10))

    # define labels for first losers
    label_loser1_name = Label(gui, text="", font=('Arial', 10))
    label_loser2_name = Label(gui, text="", font=('Arial', 10))
    label_loser3_name = Label(gui, text="", font=('Arial', 10))
    label_loser4_name = Label(gui, text="", font=('Arial', 10))
    label_loser5_name = Label(gui, text="", font=('Arial', 10))
    label_loser6_name = Label(gui, text="", font=('Arial', 10))
    label_loser7_name = Label(gui, text="", font=('Arial', 10))
    label_loser8_name = Label(gui, text="", font=('Arial', 10))

    # define labels for first winners
    label_winner1_name = Label(gui, text="", font=('Arial', 10))
    label_winner2_name = Label(gui, text="", font=('Arial', 10))
    label_winner3_name = Label(gui, text="", font=('Arial', 10))
    label_winner4_name = Label(gui, text="", font=('Arial', 10))
    label_winner5_name = Label(gui, text="", font=('Arial', 10))
    label_winner6_name = Label(gui, text="", font=('Arial', 10))
    label_winner7_name = Label(gui, text="", font=('Arial', 10))
    label_winner8_name = Label(gui, text="", font=('Arial', 10))





    gui.mainloop()