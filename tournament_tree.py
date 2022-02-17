#!/usr/bin/python3
"""
This script creates a tournament tree
Overview over all participants

:author: Manuel Milde manuelmilde@gmx.net
:copyright: 2022 Manuel Milde
"""
import os
from tkinter import Tk
from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import PatternFill

# TODO add choice to add player names


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


def reset():
    """
    This function will be executed when the reset - button was pressed.
    The initial state will be restored
    :return:
    """
    label_result_player1['text'] = ""
    label_result_player2['text'] = ""
    label_result_player3['text'] = ""
    label_result_player4['text'] = ""
    label_result_player5['text'] = ""
    label_result_player6['text'] = ""
    label_result_player7['text'] = ""
    label_result_player8['text'] = ""

    label_result_quarter1['text'] = ""
    label_result_quarter2['text'] = ""
    label_result_quarter3['text'] = ""
    label_result_quarter4['text'] = ""

    label_result_semi1['text'] = ""
    label_result_semi2['text'] = ""

    label_winner_4players['text'] = ""
    label_winner_8players['text'] = ""

    label_quarter1['text'] = ""
    label_quarter2['text'] = ""
    label_quarter3['text'] = ""
    label_quarter4['text'] = ""

    label_semi1['text'] = ""
    label_semi2['text'] = ""

    label_winner_4players['bg'] = "white"
    label_winner_8players['bg'] = "white"

    # enable start und switch buttons
    label_mode_4players.pack()
    label_mode_8players.pack()
    switch_mode_button.pack()
    start_button.pack()

    label_mode_4players.place(x=610, y=0, height=30, width=60)
    label_mode_8players.place(x=670, y=0, height=30, width=60)
    switch_mode_button.place(x=490, y=0, height=30, width=100)
    start_button.place(x=750, y=0, height=30, width=100)

    # disable enter result button
    button_enter_results.pack()
    button_enter_results.pack_forget()

    # disable plus,minus, next and back button
    button_plus.pack()
    button_minus.pack()
    button_next.pack()
    button_back.pack()

    button_plus.pack_forget()
    button_minus.pack_forget()
    button_next.pack_forget()
    button_back.pack_forget()

    # disable all labels
    label_player1_name.pack()
    label_player2_name.pack()
    label_player3_name.pack()
    label_player4_name.pack()
    label_player5_name.pack()
    label_player6_name.pack()
    label_player7_name.pack()
    label_player8_name.pack()

    label_player1_name.pack_forget()
    label_player2_name.pack_forget()
    label_player3_name.pack_forget()
    label_player4_name.pack_forget()
    label_player5_name.pack_forget()
    label_player6_name.pack_forget()
    label_player7_name.pack_forget()
    label_player8_name.pack_forget()

    label_quarter1.pack()
    label_quarter2.pack()
    label_quarter3.pack()
    label_quarter4.pack()

    label_quarter1.pack_forget()
    label_quarter2.pack_forget()
    label_quarter3.pack_forget()
    label_quarter4.pack_forget()

    label_semi1.pack()
    label_semi2.pack()

    label_semi1.pack_forget()
    label_semi2.pack_forget()
    reset2()


def reset2():
    """
    This function is called by the reset()- function
    The function is split due to pylint - warnings
    :return:
    """
    label_winner_4players.pack()
    label_winner_8players.pack()

    label_winner_4players.pack_forget()
    label_winner_8players.pack_forget()

    label_result_player1.pack()
    label_result_player2.pack()
    label_result_player3.pack()
    label_result_player4.pack()
    label_result_player5.pack()
    label_result_player6.pack()
    label_result_player7.pack()
    label_result_player8.pack()

    label_result_player1.pack_forget()
    label_result_player2.pack_forget()
    label_result_player3.pack_forget()
    label_result_player4.pack_forget()
    label_result_player5.pack_forget()
    label_result_player6.pack_forget()
    label_result_player7.pack_forget()
    label_result_player8.pack_forget()

    label_result_quarter1.pack()
    label_result_quarter2.pack()
    label_result_quarter3.pack()
    label_result_quarter4.pack()

    label_result_quarter1.pack_forget()
    label_result_quarter2.pack_forget()
    label_result_quarter3.pack_forget()
    label_result_quarter4.pack_forget()

    label_result_semi1.pack()
    label_result_semi2.pack()
    label_result_semi1.pack_forget()
    label_result_semi2.pack_forget()


def switch_mode():
    """

    :return:
    """
    if label_mode_4players['bg'] == "yellow":
        label_mode_4players['bg'] = "white"
        label_mode_8players['bg'] = "yellow"

    else:
        label_mode_4players['bg'] = "yellow"
        label_mode_8players['bg'] = "white"


def mode_4players():
    """
    This function creates all required labels for 4 players
    :return:
    """
    label_player1_name.pack()
    label_player2_name.pack()
    label_player3_name.pack()
    label_player4_name.pack()

    label_player1_name.place(x=5, y=110, height=30, width=130)
    label_player2_name.place(x=5, y=150, height=30, width=130)
    label_player3_name.place(x=5, y=220, height=30, width=130)
    label_player4_name.place(x=5, y=260, height=30, width=130)

    label_quarter1.pack()
    label_quarter2.pack()

    label_quarter1.place(x=180, y=165, height=30, width=130)
    label_quarter2.place(x=180, y=205, height=30, width=130)

    label_winner_4players.pack()
    label_winner_4players.place(x=355, y=185, height=30, width=130)

    label_result_player1.pack()
    label_result_player2.pack()
    label_result_player3.pack()
    label_result_player4.pack()

    label_result_player1.place(x=136, y=110, height=30, width=30)
    label_result_player2.place(x=136, y=150, height=30, width=30)
    label_result_player3.place(x=136, y=220, height=30, width=30)
    label_result_player4.place(x=136, y=260, height=30, width=30)

    label_result_quarter1.pack()
    label_result_quarter2.pack()

    label_result_quarter1.place(x=311, y=165, height=30, width=30)
    label_result_quarter2.place(x=311, y=205, height=30, width=30)


def mode_8players():
    """
    This function creates all required labels for 8 players
    :return:
    """
    label_player1_name.pack()
    label_player2_name.pack()
    label_player3_name.pack()
    label_player4_name.pack()
    label_player5_name.pack()
    label_player6_name.pack()
    label_player7_name.pack()
    label_player8_name.pack()

    label_player1_name.place(x=5, y=110, height=30, width=130)
    label_player2_name.place(x=5, y=150, height=30, width=130)
    label_player3_name.place(x=5, y=220, height=30, width=130)
    label_player4_name.place(x=5, y=260, height=30, width=130)
    label_player5_name.place(x=5, y=330, height=30, width=130)
    label_player6_name.place(x=5, y=370, height=30, width=130)
    label_player7_name.place(x=5, y=440, height=30, width=130)
    label_player8_name.place(x=5, y=480, height=30, width=130)

    label_quarter1.pack()
    label_quarter2.pack()
    label_quarter3.pack()
    label_quarter4.pack()

    label_quarter1.place(x=180, y=165, height=30, width=130)
    label_quarter2.place(x=180, y=205, height=30, width=130)
    label_quarter3.place(x=180, y=385, height=30, width=130)
    label_quarter4.place(x=180, y=425, height=30, width=130)

    label_semi1.pack()
    label_semi2.pack()

    label_semi1.place(x=355, y=270, height=30, width=130)
    label_semi2.place(x=355, y=310, height=30, width=130)

    label_winner_8players.pack()
    label_winner_8players.place(x=530, y=290, height=30, width=130)
    mode_8players2()


def mode_8players2():
    """
    This function is called by mode_8players
    Due to pylint warnings, the function was split
    :return:
    """
    label_result_player1.pack()
    label_result_player2.pack()
    label_result_player3.pack()
    label_result_player4.pack()
    label_result_player5.pack()
    label_result_player6.pack()
    label_result_player7.pack()
    label_result_player8.pack()

    label_result_player1.place(x=136, y=110, height=30, width=30)
    label_result_player2.place(x=136, y=150, height=30, width=30)
    label_result_player3.place(x=136, y=220, height=30, width=30)
    label_result_player4.place(x=136, y=260, height=30, width=30)
    label_result_player5.place(x=136, y=330, height=30, width=30)
    label_result_player6.place(x=136, y=370, height=30, width=30)
    label_result_player7.place(x=136, y=440, height=30, width=30)
    label_result_player8.place(x=136, y=480, height=30, width=30)

    label_result_quarter1.pack()
    label_result_quarter2.pack()
    label_result_quarter3.pack()
    label_result_quarter4.pack()

    label_result_quarter1.place(x=311, y=165, height=30, width=30)
    label_result_quarter2.place(x=311, y=205, height=30, width=30)
    label_result_quarter3.place(x=311, y=385, height=30, width=30)
    label_result_quarter4.place(x=311, y=425, height=30, width=30)

    label_result_semi1.pack()
    label_result_semi2.pack()

    label_result_semi1.place(x=486, y=270, height=30, width=30)
    label_result_semi2.place(x=486, y=310, height=30, width=30)


def start_tree():
    """
    This function starts the tournament tree after the mode was chosen
    :return:
    """
    label_mode_4players.pack()
    label_mode_8players.pack()
    switch_mode_button.pack()
    start_button.pack()

    label_mode_4players.pack_forget()
    label_mode_8players.pack_forget()
    switch_mode_button.pack_forget()
    start_button.pack_forget()

    if label_mode_4players['bg'] == "yellow":
        mode_4players()
    else:
        mode_8players()

    button_enter_results.pack()
    button_enter_results.place(x=5, y=10, height=30, width=130)


def enter_results():
    """
    This function allows to enter all results to the tournament tree
    :return:
    """
    button_enter_results.pack()
    button_enter_results.pack_forget()

    if label_quarter1['text'] == "":
        label_result_player1['bg'] = "yellow"

    elif label_mode_8players['bg'] == "yellow" and label_semi1['text'] != "":
        label_result_semi1['bg'] = "yellow"

    else:
        label_result_quarter1['bg'] = "yellow"

    button_next.pack()
    button_back.pack()
    button_back.place(x=5, y=10, height=30, width=100)
    button_next.place(x=215, y=10, height=30, width=100)

    button_plus.pack()
    button_minus.pack()
    button_minus.place(x=135, y=10, height=30, width=30)
    button_plus.place(x=165, y=10, height=30, width=30)


def back_button1():
    """
     This function switches the labels of the player names (4 or 8) backwards
    :return:
    """
    if label_semi1['text'] != "":
        back_third_round()

    elif label_quarter1['text'] != "":
        back_second_round()

    else:
        if label_result_player8['bg'] == "yellow":
            label_result_player8['bg'] = "white"
            label_result_player7['bg'] = "yellow"

        elif label_result_player7['bg'] == "yellow":
            label_result_player7['bg'] = "white"
            label_result_player6['bg'] = "yellow"

        elif label_result_player6['bg'] == "yellow":
            label_result_player6['bg'] = "white"
            label_result_player5['bg'] = "yellow"

        elif label_result_player5['bg'] == "yellow":
            label_result_player5['bg'] = "white"
            label_result_player4['bg'] = "yellow"

        elif label_result_player4['bg'] == "yellow":
            label_result_player4['bg'] = "white"
            label_result_player3['bg'] = "yellow"

        elif label_result_player3['bg'] == "yellow":
            label_result_player3['bg'] = "white"
            label_result_player2['bg'] = "yellow"

        elif label_result_player2['bg'] == "yellow":
            label_result_player2['bg'] = "white"
            label_result_player1['bg'] = "yellow"


def back_second_round():
    """

    :return:
    """
    if label_result_quarter4['bg'] == "yellow":
        label_result_quarter4['bg'] = "white"
        label_result_quarter3['bg'] = "yellow"

    elif label_result_quarter3['bg'] == "yellow":
        label_result_quarter3['bg'] = "white"
        label_result_quarter2['bg'] = "yellow"

    elif label_result_quarter2['bg'] == "yellow":
        label_result_quarter2['bg'] = "white"
        label_result_quarter1['bg'] = "yellow"


def back_third_round():
    """

    :return:
    """
    if label_result_semi2['bg'] == "yellow":
        label_result_semi2['bg'] = "white"
        label_result_semi1['bg'] = "yellow"


def next_button1():
    """
    This function switches the labels of the player names (4 or 8) forwards
    :return:
    """
    if label_semi1['text'] != "":
        next_third_round()

    elif label_quarter1['text'] != "":
        next_second_round()

    else:
        if label_result_player1['bg'] == "yellow":
            label_result_player1['bg'] = "white"
            label_result_player2['bg'] = "yellow"

        elif label_result_player2['bg'] == "yellow":
            label_result_player2['bg'] = "white"
            label_result_player3['bg'] = "yellow"

        elif label_result_player3['bg'] == "yellow":
            label_result_player3['bg'] = "white"
            label_result_player4['bg'] = "yellow"

        elif label_result_player4['bg'] == "yellow":
            if label_mode_4players['bg'] == "yellow":
                if check_if_all_labels_filled():
                    label_result_player4['bg'] = "white"
                    calculate1()
            else:
                label_result_player4['bg'] = "white"
                label_result_player5['bg'] = "yellow"

        elif label_result_player5['bg'] == "yellow":
            label_result_player5['bg'] = "white"
            label_result_player6['bg'] = "yellow"

        elif label_result_player6['bg'] == "yellow":
            label_result_player6['bg'] = "white"
            label_result_player7['bg'] = "yellow"

        elif label_result_player7['bg'] == "yellow":
            label_result_player7['bg'] = "white"
            label_result_player8['bg'] = "yellow"

        elif label_result_player8['bg'] == "yellow":
            if check_if_all_labels_filled():
                label_result_player8['bg'] = "white"
                calculate1()


def next_second_round():
    """
    This function shall enable the plus, minus, back and next - button
    :return:
    """
    button_next.pack()
    button_back.pack()
    button_minus.pack()
    button_plus.pack()

    button_minus.place(x=135, y=10, height=30, width=30)
    button_plus.place(x=165, y=10, height=30, width=30)
    button_back.place(x=5, y=10, height=30, width=100)
    button_next.place(x=215, y=10, height=30, width=100)

    if label_result_quarter1['bg'] == "yellow":
        label_result_quarter1['bg'] = "white"
        label_result_quarter2['bg'] = "yellow"

    elif label_result_quarter2['bg'] == "yellow":
        if label_mode_4players['bg'] == "yellow":
            if check_if_all_labels_filled2():
                label_result_quarter2['bg'] = "white"
                calculate2()
        else:
            label_result_quarter2['bg'] = "white"
            label_result_quarter3['bg'] = "yellow"

    elif label_result_quarter3['bg'] == "yellow":
        label_result_quarter3['bg'] = "white"
        label_result_quarter4['bg'] = "yellow"

    elif label_result_quarter4['bg'] == "yellow":
        if check_if_all_labels_filled2():
            label_result_quarter4['bg'] = "white"
            calculate2()

    if label_mode_4players['bg'] == "yellow":
        button_enter_results.pack()
        button_enter_results.pack_forget()


def next_third_round():
    """

    :return:
    """
    button_next.pack()
    button_back.pack()
    button_minus.pack()
    button_plus.pack()

    button_minus.place(x=135, y=10, height=30, width=30)
    button_plus.place(x=165, y=10, height=30, width=30)
    button_back.place(x=5, y=10, height=30, width=100)
    button_next.place(x=215, y=10, height=30, width=100)

    if label_result_semi1['bg'] == "yellow":
        label_result_semi1['bg'] = "white"
        label_result_semi2['bg'] = "yellow"

    elif label_result_semi2['bg'] == "yellow":
        if check_if_all_labels_filled3():
            label_result_semi2['bg'] = "white"
            calculate3()


def check_if_all_labels_filled():
    """
    After entering the results we need a check if all labels are filled
    :return:
    """
    if label_result_player1['text'] == "" or label_result_player2['text'] == "" \
            or label_result_player3['text'] == "" or label_result_player4['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if int(label_result_player1['text']) == int(label_result_player2['text']) \
            or int(label_result_player3['text']) == int(label_result_player4['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if label_mode_8players['bg'] == "yellow":
        if label_result_player5['text'] == "" or label_result_player6['text'] == "" \
                or label_result_player7['text'] == "" or label_result_player8['text'] == "":
            messagebox.showinfo("Error", "Check if everything has been entered correctly.")
            return False

        if int(label_result_player5['text']) == int(label_result_player6['text']) \
                or int(label_result_player7['text'] == int(label_result_player8['text'])):
            messagebox.showinfo("Error", "Check if everything has been entered correctly.")
            return False

    return True


def check_if_all_labels_filled2():
    """
    After entering the results of the second round we need a check if all labels are filled
    :return:
    """
    if label_result_quarter1['text'] == "" or label_result_quarter2['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if int(label_result_quarter1['text']) == int(label_result_quarter2['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if label_mode_8players['bg'] == "yellow":
        if label_result_quarter3['text'] == "" or label_result_quarter4['text'] == "":
            messagebox.showinfo("Error", "Check if everything has been entered correctly.")
            return False

        if int(label_result_quarter3['text']) == int(label_result_quarter4['text']):
            messagebox.showinfo("Error", "Check if everything has been entered correctly.")
            return False

    return True


def check_if_all_labels_filled3():
    """

    :return
    """
    if label_result_semi1['text'] == "" or label_result_semi2['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if int(label_result_semi1['text']) == int(label_result_semi2['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    return True


def calculate1():
    """

    :return:
    """
    button_next.pack()
    button_next.pack_forget()

    button_back.pack()
    button_back.pack_forget()

    button_minus.pack()
    button_plus.pack()
    button_plus.pack_forget()
    button_minus.pack_forget()

    # check which player has won the first round und set him to the quarter-finals
    if int(label_result_player1['text']) > int(label_result_player2['text']):
        label_quarter1['text'] = label_player1_name['text']
    else:
        label_quarter1['text'] = label_player2_name['text']

    if int(label_result_player3['text']) > int(label_result_player4['text']):
        label_quarter2['text'] = label_player3_name['text']
    else:
        label_quarter2['text'] = label_player4_name['text']

    # if 8 players check the other 4 players too
    if label_mode_8players['bg'] == "yellow":
        if int(label_result_player5['text']) > int(label_result_player6['text']):
            label_quarter3['text'] = label_player5_name['text']
        else:
            label_quarter3['text'] = label_player6_name['text']

        if int(label_result_player7['text']) > int(label_result_player8['text']):
            label_quarter4['text'] = label_player7_name['text']
        else:
            label_quarter4['text'] = label_player8_name['text']

    button_enter_results.pack()
    button_enter_results.place(x=5, y=10, height=30, width=130)


def calculate2():
    """

    :return:
    """
    button_next.pack()
    button_next.pack_forget()

    button_back.pack()
    button_back.pack_forget()

    button_minus.pack()
    button_plus.pack()
    button_plus.pack_forget()
    button_minus.pack_forget()

    # check which player has won the second round und set him to the semi-finals or winner (4 players)
    if label_mode_4players['bg'] == "yellow":
        if int(label_result_quarter1['text']) > int(label_result_quarter2['text']):
            label_winner_4players['text'] = label_quarter1['text']
        else:
            label_winner_4players['text'] = label_quarter1['text']

        label_winner_4players['bg'] = "yellow"
        messagebox.showinfo("Info", label_winner_4players['text'] + " is the winner of the tournament!")

        end_game()

    else:
        if int(label_result_quarter1['text']) > int(label_result_quarter2['text']):
            label_semi1['text'] = label_quarter1['text']
        else:
            label_semi1['text'] = label_quarter2['text']

        if int(label_result_quarter3['text']) > int(label_result_quarter4['text']):
            label_semi2['text'] = label_quarter3['text']
        else:
            label_semi2['text'] = label_quarter4['text']

    button_enter_results.pack()
    button_enter_results.place(x=5, y=10, height=30, width=130)


def calculate3():
    """

    :return:
    """
    # check which player has won the final
    button_next.pack()
    button_next.pack_forget()

    button_back.pack()
    button_back.pack_forget()

    button_minus.pack()
    button_plus.pack()
    button_plus.pack_forget()
    button_minus.pack_forget()

    if int(label_result_semi1['text']) > int(label_result_semi2['text']):
        label_winner_8players['text'] = label_semi1['text']
    else:
        label_winner_8players['text'] = label_semi2['text']

    label_winner_8players['bg'] = "yellow"
    messagebox.showinfo("Info", label_winner_8players['text'] + " is the winner of the tournament!")
    end_game()


def plus_first_round():
    """
    This function increments
    :return:
    """
    if label_semi1['text'] != "":
        plus_third_round()

    elif label_quarter1['text'] != "":
        plus_second_round()

    else:
        if label_result_player1['bg'] == "yellow":
            if label_result_player1['text'] == "":
                label_result_player1['text'] = "1"
            else:
                label_result_player1['text'] = int(label_result_player1['text']) + 1

        elif label_result_player2['bg'] == "yellow":
            if label_result_player2['text'] == "":
                label_result_player2['text'] = "1"
            else:
                label_result_player2['text'] = int(label_result_player2['text']) + 1

        elif label_result_player3['bg'] == "yellow":
            if label_result_player3['text'] == "":
                label_result_player3['text'] = "1"
            else:
                label_result_player3['text'] = int(label_result_player3['text']) + 1

        elif label_result_player4['bg'] == "yellow":
            if label_result_player4['text'] == "":
                label_result_player4['text'] = "1"
            else:
                label_result_player4['text'] = int(label_result_player4['text']) + 1

        elif label_result_player5['bg'] == "yellow":
            if label_result_player5['text'] == "":
                label_result_player5['text'] = "1"
            else:
                label_result_player5['text'] = int(label_result_player5['text']) + 1

        elif label_result_player6['bg'] == "yellow":
            if label_result_player6['text'] == "":
                label_result_player6['text'] = "1"
            else:
                label_result_player6['text'] = int(label_result_player6['text']) + 1

        elif label_result_player7['bg'] == "yellow":
            if label_result_player7['text'] == "":
                label_result_player7['text'] = "1"
            else:
                label_result_player7['text'] = int(label_result_player7['text']) + 1

        elif label_result_player8['bg'] == "yellow":
            if label_result_player8['text'] == "":
                label_result_player8['text'] = "1"
            else:
                label_result_player8['text'] = int(label_result_player8['text']) + 1


def minus_first_round():
    """
    This function decrements
    :return:
    """
    if label_semi1['text'] != "":
        minus_third_round()

    elif label_quarter1['text'] != "":
        minus_second_round()

    else:
        if label_result_player1['bg'] == "yellow":
            if label_result_player1['text'] == "":
                label_result_player1['text'] = "0"
            elif int(label_result_player1['text']) > 0:
                label_result_player1['text'] = int(label_result_player1['text']) - 1

        elif label_result_player2['bg'] == "yellow":
            if label_result_player2['text'] == "":
                label_result_player2['text'] = "0"
            elif int(label_result_player2['text']) > 0:
                label_result_player2['text'] = int(label_result_player2['text']) - 1

        elif label_result_player3['bg'] == "yellow":
            if label_result_player3['text'] == "":
                label_result_player3['text'] = "0"
            elif int(label_result_player3['text']) > 0:
                label_result_player3['text'] = int(label_result_player3['text']) - 1

        elif label_result_player4['bg'] == "yellow":
            if label_result_player4['text'] == "":
                label_result_player4['text'] = "0"
            elif int(label_result_player4['text']) > 0:
                label_result_player4['text'] = int(label_result_player4['text']) - 1

        elif label_result_player5['bg'] == "yellow":
            if label_result_player5['text'] == "":
                label_result_player5['text'] = "0"
            elif int(label_result_player5['text']) > 0:
                label_result_player5['text'] = int(label_result_player5['text']) - 1

        elif label_result_player6['bg'] == "yellow":
            if label_result_player6['text'] == "":
                label_result_player6['text'] = "0"
            elif int(label_result_player6['text']) > 0:
                label_result_player6['text'] = int(label_result_player6['text']) - 1

        elif label_result_player7['bg'] == "yellow":
            if label_result_player7['text'] == "":
                label_result_player7['text'] = "0"
            elif int(label_result_player7['text']) > 0:
                label_result_player7['text'] = int(label_result_player7['text']) - 1

        elif label_result_player8['bg'] == "yellow":
            if label_result_player8['text'] == "":
                label_result_player8['text'] = "0"
            elif int(label_result_player8['text']) > 0:
                label_result_player8['text'] = int(label_result_player8['text']) - 1


def plus_second_round():
    """
    This function increments for the second round
    :return:
    """
    if label_result_quarter1['bg'] == "yellow":
        if label_result_quarter1['text'] == "":
            label_result_quarter1['text'] = "1"
        else:
            label_result_quarter1['text'] = int(label_result_quarter1['text']) + 1

    elif label_result_quarter2['bg'] == "yellow":
        if label_result_quarter2['text'] == "":
            label_result_quarter2['text'] = "1"
        else:
            label_result_quarter2['text'] = int(label_result_quarter2['text']) + 1

    elif label_result_quarter3['bg'] == "yellow":
        if label_result_quarter3['text'] == "":
            label_result_quarter3['text'] = "1"
        else:
            label_result_quarter3['text'] = int(label_result_quarter3['text']) + 1

    elif label_result_quarter4['bg'] == "yellow":
        if label_result_quarter4['text'] == "":
            label_result_quarter4['text'] = "1"
        else:
            label_result_quarter4['text'] = int(label_result_quarter4['text']) + 1


def minus_second_round():
    """
    This function decrements for the second round
    :return:
    """
    if label_result_quarter1['bg'] == "yellow":
        if label_result_quarter1['text'] == "":
            label_result_quarter1['text'] = "0"
        elif int(label_result_quarter1['text']) > 0:
            label_result_quarter1['text'] = int(label_result_quarter1['text']) - 1

    elif label_result_quarter2['bg'] == "yellow":
        if label_result_quarter2['text'] == "":
            label_result_quarter2['text'] = "0"
        elif int(label_result_quarter2['text']) > 0:
            label_result_quarter2['text'] = int(label_result_quarter2['text']) - 1

    elif label_result_quarter3['bg'] == "yellow":
        if label_result_quarter3['text'] == "":
            label_result_quarter3['text'] = "0"
        elif int(label_result_quarter3['text']) > 0:
            label_result_quarter3['text'] = int(label_result_quarter3['text']) - 1

    elif label_result_quarter4['bg'] == "yellow":
        if label_result_quarter4['text'] == "":
            label_result_quarter4['text'] = "0"
        elif int(label_result_quarter4['text']) > 0:
            label_result_quarter4['text'] = int(label_result_quarter4['text']) - 1


def plus_third_round():
    """
    This function increments for the third round
    :return:
    """
    if label_result_semi1['bg'] == "yellow":
        if label_result_semi1['text'] == "":
            label_result_semi1['text'] = "1"
        else:
            label_result_semi1['text'] = int(label_result_semi1['text']) + 1

    elif label_result_semi2['bg'] == "yellow":
        if label_result_semi2['text'] == "":
            label_result_semi2['text'] = "1"
        else:
            label_result_semi2['text'] = int(label_result_semi2['text']) + 1


def minus_third_round():
    """
    This function decrements for the third round
    """
    if label_result_semi1['bg'] == "yellow":
        if label_result_semi1['text'] == "":
            label_result_semi1['text'] = "0"
        elif int(label_result_semi1['text']) > 0:
            label_result_semi1['text'] = int(label_result_semi1['text']) - 1

    elif label_result_semi2['bg'] == "yellow":
        if label_result_semi2['text'] == "":
            label_result_semi2['text'] = "0"
        elif int(label_result_semi2['text']) > 0:
            label_result_semi2['text'] = int(label_result_semi2['text']) - 1


def end_game():
    """

    :return:
    """
    button_enter_results.pack()
    button_enter_results.pack_forget()
    # TODO enable button for creating excel with all information


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

    # define button for switching mode (4 or 8 players)
    switch_mode_button = Button(gui, text="Switch mode", bd=1, fg="black", bg="white",
                                font=('Arial', 10), command=switch_mode)

    switch_mode_button.place(x=490, y=0, height=30, width=100)

    # define labels for switching mode (4 or 8 players)
    label_mode_4players = Label(gui, text="4 Players", bg="white", font=('Arial', 10))
    label_mode_8players = Label(gui, text="8 Players", bg="yellow", font=('Arial', 10))

    label_mode_4players.place(x=610, y=0, height=30, width=60)
    label_mode_8players.place(x=670, y=0, height=30, width=60)

    # define start-button after the mode was chosen the tournament tree can be created
    start_button = Button(gui, text="Start", bg="lightgreen", font=('Arial', 10),
                          command=start_tree)
    start_button.place(x=750, y=0, height=30, width=100)

    # define reset - button
    reset_button = Button(gui, text="Reset", bg="red", font=('Arial', 10, 'bold'), command=reset)
    reset_button.place(x=1175, y=80, height=30, width=100)

    # define button for entering results
    button_enter_results = Button(gui, text="Enter results", bd=1, fg="black", bg="lightgreen",
                                  font=('Arial', 10), command=enter_results)

    button_enter_results.place(x=5, y=10, height=30, width=130)

    button_enter_results.pack()
    button_enter_results.pack_forget()

    # define next-button for entering results
    button_next = Button(gui, text="Next", bd=1, fg="black", bg="lightgreen",
                         font=('Arial', 10), command=next_button1)
    button_next.place(x=215, y=10, height=30, width=100)
    button_next.pack()
    button_next.pack_forget()

    # define back-button for entering results
    button_back = Button(gui, text="Back", bd=1, fg="black", bg="lightgreen",
                         font=('Arial', 10), command=back_button1)
    button_back.place(x=5, y=10, height=30, width=100)
    button_back.pack()
    button_back.pack_forget()

    # define plus and minus buttons
    button_minus = Button(gui, text="-", bd=1, fg="black", bg="red",
                          font=('Arial', 10), command=minus_first_round)

    button_plus = Button(gui, text="+", bd=1, fg="black", bg="lightgreen",
                         font=('Arial', 10), command=plus_first_round)

    button_minus.place(x=135, y=10, height=30, width=30)
    button_plus.place(x=165, y=10, height=30, width=30)
    button_minus.pack()
    button_plus.pack()
    button_minus.pack_forget()
    button_plus.pack_forget()

    # ---------------------------------------------------------------------------------------------#
    # define labels for 8 player names
    label_player1_name = Label(gui, text="Michael van Gerwen", font=('Arial', 10))
    label_player2_name = Label(gui, text="Devon Peterson", font=('Arial', 10))
    label_player3_name = Label(gui, text="Michael Smith", font=('Arial', 10))
    label_player4_name = Label(gui, text="Peter Wright", font=('Arial', 10))
    label_player5_name = Label(gui, text="Gary Anderson", font=('Arial', 10))
    label_player6_name = Label(gui, text="Gabriel Clemens", font=('Arial', 10))
    label_player7_name = Label(gui, text="Jonny Clayton", font=('Arial', 10))
    label_player8_name = Label(gui, text="Darius Labanauskas", font=('Arial', 10))

    label_player1_name.place(x=5, y=110, height=30, width=130)
    label_player2_name.place(x=5, y=150, height=30, width=130)
    label_player3_name.place(x=5, y=220, height=30, width=130)
    label_player4_name.place(x=5, y=260, height=30, width=130)
    label_player5_name.place(x=5, y=330, height=30, width=130)
    label_player6_name.place(x=5, y=370, height=30, width=130)
    label_player7_name.place(x=5, y=440, height=30, width=130)
    label_player8_name.place(x=5, y=480, height=30, width=130)

    # define labels for 4 quarter finals
    label_quarter1 = Label(gui, text="", font=('Arial', 10))
    label_quarter2 = Label(gui, text="", font=('Arial', 10))
    label_quarter3 = Label(gui, text="", font=('Arial', 10))
    label_quarter4 = Label(gui, text="", font=('Arial', 10))
    label_quarter1.place(x=180, y=165, height=30, width=130)
    label_quarter2.place(x=180, y=205, height=30, width=130)
    label_quarter3.place(x=180, y=385, height=30, width=130)
    label_quarter4.place(x=180, y=425, height=30, width=130)

    # define labels for 2 semi finals
    label_semi1 = Label(gui, text="", font=('Arial', 10))
    label_semi2 = Label(gui, text="", font=('Arial', 10))
    label_semi1.place(x=355, y=270, height=30, width=130)
    label_semi2.place(x=355, y=310, height=30, width=130)

    # define label for winner for 4 players
    label_winner_4players = Label(gui, text="", font=('Arial', 10))
    label_winner_4players.place(x=355, y=185, height=30, width=130)

    # define label for winner for 8 players
    label_winner_8players = Label(gui, text="", font=('Arial', 10))
    label_winner_8players.place(x=530, y=290, height=30, width=130)

    # define result - labels for players 1-8
    label_result_player1 = Label(gui, text="", font=('Arial', 10))
    label_result_player2 = Label(gui, text="", font=('Arial', 10))
    label_result_player3 = Label(gui, text="", font=('Arial', 10))
    label_result_player4 = Label(gui, text="", font=('Arial', 10))
    label_result_player5 = Label(gui, text="", font=('Arial', 10))
    label_result_player6 = Label(gui, text="", font=('Arial', 10))
    label_result_player7 = Label(gui, text="", font=('Arial', 10))
    label_result_player8 = Label(gui, text="", font=('Arial', 10))

    label_result_player1.place(x=136, y=110, height=30, width=30)
    label_result_player2.place(x=136, y=150, height=30, width=30)
    label_result_player3.place(x=136, y=220, height=30, width=30)
    label_result_player4.place(x=136, y=260, height=30, width=30)
    label_result_player5.place(x=136, y=330, height=30, width=30)
    label_result_player6.place(x=136, y=370, height=30, width=30)
    label_result_player7.place(x=136, y=440, height=30, width=30)
    label_result_player8.place(x=136, y=480, height=30, width=30)

    # define result - labels for 4 quarter
    label_result_quarter1 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter2 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter3 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter4 = Label(gui, text="", font=('Arial', 10))

    label_result_quarter1.place(x=311, y=165, height=30, width=30)
    label_result_quarter2.place(x=311, y=205, height=30, width=30)
    label_result_quarter3.place(x=311, y=385, height=30, width=30)
    label_result_quarter4.place(x=311, y=425, height=30, width=30)

    # define result - labels for 2 semi
    label_result_semi1 = Label(gui, text="", font=('Arial', 10))
    label_result_semi2 = Label(gui, text="", font=('Arial', 10))

    label_result_semi1.place(x=486, y=270, height=30, width=30)
    label_result_semi2.place(x=486, y=310, height=30, width=30)

    # ---------------------------------------------------------------------------------------------#
    # disable all labels
    label_player1_name.pack()
    label_player2_name.pack()
    label_player3_name.pack()
    label_player4_name.pack()
    label_player5_name.pack()
    label_player6_name.pack()
    label_player7_name.pack()
    label_player8_name.pack()

    label_player1_name.pack_forget()
    label_player2_name.pack_forget()
    label_player3_name.pack_forget()
    label_player4_name.pack_forget()
    label_player5_name.pack_forget()
    label_player6_name.pack_forget()
    label_player7_name.pack_forget()
    label_player8_name.pack_forget()

    label_quarter1.pack()
    label_quarter2.pack()
    label_quarter3.pack()
    label_quarter4.pack()

    label_quarter1.pack_forget()
    label_quarter2.pack_forget()
    label_quarter3.pack_forget()
    label_quarter4.pack_forget()

    label_semi1.pack()
    label_semi2.pack()

    label_semi1.pack_forget()
    label_semi2.pack_forget()

    label_winner_4players.pack()
    label_winner_8players.pack()

    label_winner_4players.pack_forget()
    label_winner_8players.pack_forget()

    label_result_player1.pack()
    label_result_player2.pack()
    label_result_player3.pack()
    label_result_player4.pack()
    label_result_player5.pack()
    label_result_player6.pack()
    label_result_player7.pack()
    label_result_player8.pack()

    label_result_player1.pack_forget()
    label_result_player2.pack_forget()
    label_result_player3.pack_forget()
    label_result_player4.pack_forget()
    label_result_player5.pack_forget()
    label_result_player6.pack_forget()
    label_result_player7.pack_forget()
    label_result_player8.pack_forget()

    label_result_quarter1.pack()
    label_result_quarter2.pack()
    label_result_quarter3.pack()
    label_result_quarter4.pack()

    label_result_quarter1.pack_forget()
    label_result_quarter2.pack_forget()
    label_result_quarter3.pack_forget()
    label_result_quarter4.pack_forget()

    label_result_semi1.pack()
    label_result_semi2.pack()
    label_result_semi1.pack_forget()
    label_result_semi2.pack_forget()

    gui.mainloop()
