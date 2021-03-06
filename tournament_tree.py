#!/usr/bin/python3
# pylint: disable=C0302
"""
This script creates a tournament tree
Overview over all participants

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


def reset():
    """
    This function will be executed when the reset - button was pressed.
    The initial state will be restored
    :return:
    """
    label_player1_name['text'] = ""
    label_player2_name['text'] = ""
    label_player3_name['text'] = ""
    label_player4_name['text'] = ""
    label_player5_name['text'] = ""
    label_player6_name['text'] = ""
    label_player7_name['text'] = ""
    label_player8_name['text'] = ""
    label_player9_name['text'] = ""
    label_player10_name['text'] = ""
    label_player11_name['text'] = ""
    label_player12_name['text'] = ""
    label_player13_name['text'] = ""
    label_player14_name['text'] = ""
    label_player15_name['text'] = ""
    label_player16_name['text'] = ""

    label_result_player1['text'] = ""
    label_result_player2['text'] = ""
    label_result_player3['text'] = ""
    label_result_player4['text'] = ""
    label_result_player5['text'] = ""
    label_result_player6['text'] = ""
    label_result_player7['text'] = ""
    label_result_player8['text'] = ""
    label_result_player9['text'] = ""
    label_result_player10['text'] = ""
    label_result_player11['text'] = ""
    label_result_player12['text'] = ""
    label_result_player13['text'] = ""
    label_result_player14['text'] = ""
    label_result_player15['text'] = ""
    label_result_player16['text'] = ""

    label_result_quarter1['text'] = ""
    label_result_quarter2['text'] = ""
    label_result_quarter3['text'] = ""
    label_result_quarter4['text'] = ""
    label_result_quarter5['text'] = ""
    label_result_quarter6['text'] = ""
    label_result_quarter7['text'] = ""
    label_result_quarter8['text'] = ""

    label_result_semi1['text'] = ""
    label_result_semi2['text'] = ""
    label_result_semi3['text'] = ""
    label_result_semi4['text'] = ""

    label_result_final1['text'] = ""
    label_result_final2['text'] = ""
    reset2()


def reset2():
    """
    This function is called by the reset
    :return:
    """
    # disable all labels
    label_player1_name.pack()
    label_player2_name.pack()
    label_player3_name.pack()
    label_player4_name.pack()
    label_player5_name.pack()
    label_player6_name.pack()
    label_player7_name.pack()
    label_player8_name.pack()
    label_player9_name.pack()
    label_player10_name.pack()
    label_player11_name.pack()
    label_player12_name.pack()
    label_player13_name.pack()
    label_player14_name.pack()
    label_player15_name.pack()
    label_player16_name.pack()

    label_player1_name.pack_forget()
    label_player2_name.pack_forget()
    label_player3_name.pack_forget()
    label_player4_name.pack_forget()
    label_player5_name.pack_forget()
    label_player6_name.pack_forget()
    label_player7_name.pack_forget()
    label_player8_name.pack_forget()
    label_player9_name.pack_forget()
    label_player10_name.pack_forget()
    label_player11_name.pack_forget()
    label_player12_name.pack_forget()
    label_player13_name.pack_forget()
    label_player14_name.pack_forget()
    label_player15_name.pack_forget()
    label_player16_name.pack_forget()

    label_result_player1.pack()
    label_result_player2.pack()
    label_result_player3.pack()
    label_result_player4.pack()
    label_result_player5.pack()
    label_result_player6.pack()
    label_result_player7.pack()
    label_result_player8.pack()
    label_result_player9.pack()
    label_result_player10.pack()
    label_result_player11.pack()
    label_result_player12.pack()
    label_result_player13.pack()
    label_result_player14.pack()
    label_result_player15.pack()
    label_result_player16.pack()

    reset3()


def reset3():
    """
    This function is called by the reset2
    :return:
    """
    label_winner_4players['text'] = ""
    label_winner_8players['text'] = ""
    label_winner_16players['text'] = ""

    label_quarter1['text'] = ""
    label_quarter2['text'] = ""
    label_quarter3['text'] = ""
    label_quarter4['text'] = ""
    label_quarter5['text'] = ""
    label_quarter6['text'] = ""
    label_quarter7['text'] = ""
    label_quarter8['text'] = ""

    label_semi1['text'] = ""
    label_semi2['text'] = ""
    label_semi3['text'] = ""
    label_semi4['text'] = ""

    label_final1['text'] = ""
    label_final2['text'] = ""

    label_winner_4players['bg'] = "white"
    label_winner_8players['bg'] = "white"
    label_winner_16players['bg'] = "white"

    label_result_player1.pack_forget()
    label_result_player2.pack_forget()
    label_result_player3.pack_forget()
    label_result_player4.pack_forget()
    label_result_player5.pack_forget()
    label_result_player6.pack_forget()
    label_result_player7.pack_forget()
    label_result_player8.pack_forget()
    label_result_player9.pack_forget()
    label_result_player10.pack_forget()
    label_result_player11.pack_forget()
    label_result_player12.pack_forget()
    label_result_player13.pack_forget()
    label_result_player14.pack_forget()
    label_result_player15.pack_forget()
    label_result_player16.pack_forget()

    reset4()


def reset4():
    """
    This function is called by the reset3
    :return:
    """
    label_result_quarter1.pack()
    label_result_quarter2.pack()
    label_result_quarter3.pack()
    label_result_quarter4.pack()
    label_result_quarter5.pack()
    label_result_quarter6.pack()
    label_result_quarter7.pack()
    label_result_quarter8.pack()

    label_result_quarter1.pack_forget()
    label_result_quarter2.pack_forget()
    label_result_quarter3.pack_forget()
    label_result_quarter4.pack_forget()
    label_result_quarter5.pack_forget()
    label_result_quarter6.pack_forget()
    label_result_quarter7.pack_forget()
    label_result_quarter8.pack_forget()

    label_quarter1.pack()
    label_quarter2.pack()
    label_quarter3.pack()
    label_quarter4.pack()
    label_quarter5.pack()
    label_quarter6.pack()
    label_quarter7.pack()
    label_quarter8.pack()

    label_quarter1.pack_forget()
    label_quarter2.pack_forget()
    label_quarter3.pack_forget()
    label_quarter4.pack_forget()
    label_quarter5.pack_forget()
    label_quarter6.pack_forget()
    label_quarter7.pack_forget()
    label_quarter8.pack_forget()

    label_result_semi1.pack()
    label_result_semi2.pack()
    label_result_semi3.pack()
    label_result_semi4.pack()

    label_result_semi1.pack_forget()
    label_result_semi2.pack_forget()
    label_result_semi3.pack_forget()
    label_result_semi4.pack_forget()

    label_result_final1.pack()
    label_result_final2.pack()

    label_result_final1.pack_forget()
    label_result_final2.pack_forget()

    reset5()


def reset5():
    """
    This function is called by the reset4
    :return:
    """
    disable_first_four_input_fields()
    disable_input_fields_5_to_16()

    label_semi1.pack()
    label_semi2.pack()
    label_semi3.pack()
    label_semi4.pack()

    label_semi1.pack_forget()
    label_semi2.pack_forget()
    label_semi3.pack_forget()
    label_semi4.pack_forget()

    label_final1.pack()
    label_final2.pack()

    label_final1.pack_forget()
    label_final2.pack_forget()

    label_winner_4players.pack()
    label_winner_8players.pack()
    label_winner_16players.pack()

    label_winner_4players.pack_forget()
    label_winner_8players.pack_forget()
    label_winner_16players.pack_forget()

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

    # enable start und switch buttons
    label_mode_4players.pack()
    label_mode_8players.pack()
    switch_mode_button.pack()
    start_button.pack()

    label_mode_4players.place(x=532.5, y=0, height=30, width=70)
    label_mode_8players.place(x=602.5, y=0, height=30, width=70)
    label_mode_16players.place(x=672.5, y=0, height=30, width=70)
    switch_mode_button.place(x=412.4, y=0, height=30, width=100)
    start_button.place(x=762.5, y=0, height=30, width=100)

    button_enter_names.pack()
    button_enter_names.pack_forget()

    reset6()


def reset6():
    """
    This function is called by the reset5
    :return:
    """
    while len(all_player_names) > 0:
        for item in all_player_names:
            all_player_names.remove(item)

    label_name_order1.pack()
    label_name_order2.pack()

    label_info_names.pack()
    button_switch_order.pack()

    label_name_order1.pack_forget()
    label_name_order2.pack_forget()
    label_info_names.pack_forget()
    button_switch_order.pack_forget()

    label_result_player1['bg'] = "white"
    label_result_player2['bg'] = "white"
    label_result_player3['bg'] = "white"
    label_result_player4['bg'] = "white"
    label_result_player5['bg'] = "white"
    label_result_player6['bg'] = "white"
    label_result_player7['bg'] = "white"
    label_result_player8['bg'] = "white"
    label_result_player9['bg'] = "white"
    label_result_player10['bg'] = "white"
    label_result_player11['bg'] = "white"
    label_result_player12['bg'] = "white"
    label_result_player13['bg'] = "white"
    label_result_player14['bg'] = "white"
    label_result_player15['bg'] = "white"
    label_result_player16['bg'] = "white"

    label_result_quarter1['bg'] = "white"
    label_result_quarter2['bg'] = "white"
    label_result_quarter3['bg'] = "white"
    label_result_quarter4['bg'] = "white"
    label_result_quarter5['bg'] = "white"
    label_result_quarter6['bg'] = "white"
    label_result_quarter7['bg'] = "white"
    label_result_quarter8['bg'] = "white"

    label_result_semi1['bg'] = "white"
    label_result_semi2['bg'] = "white"
    label_result_semi3['bg'] = "white"
    label_result_semi4['bg'] = "white"

    label_result_final1['bg'] = "white"
    label_result_final2['bg'] = "white"


def disable_first_four_input_fields():
    """
    This function disables the first four input names
    :return:
    """
    input_name1.pack()
    input_name2.pack()
    input_name3.pack()
    input_name4.pack()

    input_name1.pack_forget()
    input_name2.pack_forget()
    input_name3.pack_forget()
    input_name4.pack_forget()


def disable_input_fields_5_to_16():
    """
    This function disables the input fields 5 to 16
    :return:
    """
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


def switch_mode():
    """
    This function switches the mode between 4, 8 and 16 players
    :return:
    """
    if label_mode_4players['bg'] == "yellow":
        label_mode_4players['bg'] = "white"
        label_mode_8players['bg'] = "yellow"

    elif label_mode_8players['bg'] == "yellow":
        label_mode_8players['bg'] = "white"
        label_mode_16players['bg'] = "yellow"

    else:
        label_mode_16players['bg'] = "white"
        label_mode_4players['bg'] = "yellow"


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


def mode_4players():
    """
    This function creates all required labels for 4 players
    :return:
    """
    label_player1_name.place(x=5, y=140, height=30, width=130)
    label_player2_name.place(x=5, y=180, height=30, width=130)
    label_player3_name.place(x=5, y=250, height=30, width=130)
    label_player4_name.place(x=5, y=290, height=30, width=130)

    label_quarter1.place(x=180, y=195, height=30, width=130)
    label_quarter2.place(x=180, y=235, height=30, width=130)

    label_winner_4players.place(x=355, y=215, height=30, width=130)

    label_result_player1.place(x=136, y=140, height=30, width=30)
    label_result_player2.place(x=136, y=180, height=30, width=30)
    label_result_player3.place(x=136, y=250, height=30, width=30)
    label_result_player4.place(x=136, y=290, height=30, width=30)

    label_result_quarter1.place(x=311, y=195, height=30, width=30)
    label_result_quarter2.place(x=311, y=235, height=30, width=30)


def mode_8players():
    """
    This function creates all required labels for 8 players
    :return:
    """
    label_player1_name.place(x=5, y=140, height=30, width=130)
    label_player2_name.place(x=5, y=180, height=30, width=130)
    label_player3_name.place(x=5, y=250, height=30, width=130)
    label_player4_name.place(x=5, y=290, height=30, width=130)
    label_player5_name.place(x=5, y=360, height=30, width=130)
    label_player6_name.place(x=5, y=400, height=30, width=130)
    label_player7_name.place(x=5, y=470, height=30, width=130)
    label_player8_name.place(x=5, y=510, height=30, width=130)

    label_quarter1.place(x=180, y=195, height=30, width=130)
    label_quarter2.place(x=180, y=235, height=30, width=130)
    label_quarter3.place(x=180, y=415, height=30, width=130)
    label_quarter4.place(x=180, y=455, height=30, width=130)

    label_semi1.place(x=355, y=300, height=30, width=130)
    label_semi2.place(x=355, y=340, height=30, width=130)

    label_winner_8players.place(x=530, y=320, height=30, width=130)

    mode_8players2()


def mode_8players2():
    """
    This function is called by mode_8players
    :return:
    """
    label_result_player1.place(x=136, y=140, height=30, width=30)
    label_result_player2.place(x=136, y=180, height=30, width=30)
    label_result_player3.place(x=136, y=250, height=30, width=30)
    label_result_player4.place(x=136, y=290, height=30, width=30)
    label_result_player5.place(x=136, y=360, height=30, width=30)
    label_result_player6.place(x=136, y=400, height=30, width=30)
    label_result_player7.place(x=136, y=470, height=30, width=30)
    label_result_player8.place(x=136, y=510, height=30, width=30)

    label_result_quarter1.place(x=311, y=195, height=30, width=30)
    label_result_quarter2.place(x=311, y=235, height=30, width=30)
    label_result_quarter3.place(x=311, y=415, height=30, width=30)
    label_result_quarter4.place(x=311, y=455, height=30, width=30)

    label_result_semi1.place(x=486, y=300, height=30, width=30)
    label_result_semi2.place(x=486, y=340, height=30, width=30)


def mode_16players():
    """
    This function creates all required labels for 16 players
    :return:
    """
    mode_8players2()

    label_player1_name.place(x=5, y=140, height=30, width=130)
    label_player2_name.place(x=5, y=180, height=30, width=130)
    label_player3_name.place(x=5, y=250, height=30, width=130)
    label_player4_name.place(x=5, y=290, height=30, width=130)
    label_player5_name.place(x=5, y=360, height=30, width=130)
    label_player6_name.place(x=5, y=400, height=30, width=130)
    label_player7_name.place(x=5, y=470, height=30, width=130)
    label_player8_name.place(x=5, y=510, height=30, width=130)

    label_quarter1.place(x=180, y=195, height=30, width=130)
    label_quarter2.place(x=180, y=235, height=30, width=130)
    label_quarter3.place(x=180, y=415, height=30, width=130)
    label_quarter4.place(x=180, y=455, height=30, width=130)

    label_quarter5.place(x=965, y=195, height=30, width=130)
    label_quarter6.place(x=965, y=235, height=30, width=130)
    label_quarter7.place(x=965, y=415, height=30, width=130)
    label_quarter8.place(x=965, y=455, height=30, width=130)

    label_semi1.place(x=355, y=300, height=30, width=130)
    label_semi2.place(x=355, y=340, height=30, width=130)
    label_semi3.place(x=790, y=300, height=30, width=130)
    label_semi4.place(x=790, y=340, height=30, width=130)

    label_final1.place(x=461.5, y=400, height=30, width=130)
    label_final2.place(x=683.5, y=400, height=30, width=130)

    label_result_final1.place(x=592.5, y=400, height=30, width=30)
    label_result_final2.place(x=652.5, y=400, height=30, width=30)

    label_winner_16players.place(x=572.5, y=460, height=30, width=130)

    # define labels for the other 8 players
    label_player9_name.place(x=1140, y=140, height=30, width=130)
    label_player10_name.place(x=1140, y=180, height=30, width=130)
    label_player11_name.place(x=1140, y=250, height=30, width=130)
    label_player12_name.place(x=1140, y=290, height=30, width=130)
    label_player13_name.place(x=1140, y=360, height=30, width=130)
    label_player14_name.place(x=1140, y=400, height=30, width=130)
    label_player15_name.place(x=1140, y=470, height=30, width=130)
    label_player16_name.place(x=1140, y=510, height=30, width=130)

    label_result_player9.place(x=1109, y=140, height=30, width=30)
    label_result_player10.place(x=1109, y=180, height=30, width=30)
    label_result_player11.place(x=1109, y=250, height=30, width=30)
    label_result_player12.place(x=1109, y=290, height=30, width=30)
    label_result_player13.place(x=1109, y=360, height=30, width=30)
    label_result_player14.place(x=1109, y=400, height=30, width=30)
    label_result_player15.place(x=1109, y=470, height=30, width=30)
    label_result_player16.place(x=1109, y=510, height=30, width=30)

    label_result_quarter5.place(x=934, y=195, height=30, width=30)
    label_result_quarter6.place(x=934, y=235, height=30, width=30)
    label_result_quarter7.place(x=934, y=415, height=30, width=30)
    label_result_quarter8.place(x=934, y=455, height=30, width=30)

    label_result_semi3.place(x=759, y=300, height=30, width=30)
    label_result_semi4.place(x=759, y=340, height=30, width=30)


def check_names():
    """
    This function checks if all names have been entered
    :return:
    """
    name1 = input_name1.get()
    name2 = input_name2.get()
    name3 = input_name3.get()
    name4 = input_name4.get()

    if name1 == "" or name2 == "" or name3 == "" or name4 == "":
        messagebox.showinfo("Error", "Not all names were entered.")
        return

    all_player_names.append(name1)
    all_player_names.append(name2)
    all_player_names.append(name3)
    all_player_names.append(name4)

    # check if 8 or players
    if label_mode_8players['bg'] == "yellow" or label_mode_16players['bg'] == "yellow":
        name5 = input_name5.get()
        name6 = input_name6.get()
        name7 = input_name7.get()
        name8 = input_name8.get()

        if name5 == "" or name6 == "" or name7 == "" or name8 == "":
            messagebox.showinfo("Error", "Not all names were entered.")
            return

        all_player_names.append(name5)
        all_player_names.append(name6)
        all_player_names.append(name7)
        all_player_names.append(name8)

    check_names2()


def check_names2():
    """
    This function is called by check_names
    :return:
    """

    if label_mode_16players['bg'] == "yellow":
        name9 = input_name9.get()
        name10 = input_name10.get()
        name11 = input_name11.get()
        name12 = input_name12.get()
        name13 = input_name13.get()
        name14 = input_name14.get()
        name15 = input_name15.get()
        name16 = input_name16.get()

        if name9 == "" or name10 == "" or name11 == "" or name12 == "":
            messagebox.showinfo("Error", "Not all names were entered.")
            return

        if name13 == "" or name14 == "" or name15 == "" or name16 == "":
            messagebox.showinfo("Error", "Not all names were entered.")
            return

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
    disable_first_four_input_fields()

    check_names3()


def check_names3():
    """
    This function is called by check_names2
    :return:
    """

    if label_mode_8players['bg'] == "yellow" or label_mode_16players['bg'] == "yellow":
        disable_input_fields_5_to_16()

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
        if label_mode_4players['bg'] == "yellow":
            numbers = []
            while len(numbers) < 4:

                random_number = round(random.uniform(0, 3))
                if random_number not in numbers:
                    numbers.append(random_number)

            label_player1_name['text'] = all_player_names[numbers[0]]
            label_player2_name['text'] = all_player_names[numbers[1]]
            label_player3_name['text'] = all_player_names[numbers[2]]
            label_player4_name['text'] = all_player_names[numbers[3]]

        elif label_mode_8players['bg'] == "yellow":
            numbers = []
            while len(numbers) < 8:

                random_number = round(random.uniform(0, 7))
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

        else:
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

    if label_mode_8players['bg'] == "yellow" or label_mode_16players['bg'] == "yellow":
        label_player5_name['text'] = all_player_names[4]
        label_player6_name['text'] = all_player_names[5]
        label_player7_name['text'] = all_player_names[6]
        label_player8_name['text'] = all_player_names[7]

        if label_mode_16players['bg'] == "yellow":
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
    label_mode_4players.pack()
    label_mode_8players.pack()
    label_mode_16players.pack()
    switch_mode_button.pack()
    start_button.pack()

    label_mode_4players.pack_forget()
    label_mode_8players.pack_forget()
    label_mode_16players.pack_forget()
    switch_mode_button.pack_forget()
    start_button.pack_forget()

    if label_mode_4players['bg'] == "yellow":
        mode_4players()
    elif label_mode_8players['bg'] == "yellow":
        mode_8players()
    else:
        mode_16players()

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

    elif label_mode_16players['bg'] == "yellow" and label_final1['text'] != "":
        label_result_final1['bg'] = "yellow"

    elif not label_mode_4players['bg'] == "yellow" and label_semi1['text'] != "":
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


def back_button_first_round():
    """
    This function switches the labels of the player names backwards
    :return:
    """
    if label_final1['text'] != "":
        back_fourth_round()

    elif label_semi1['text'] != "":
        back_third_round()

    elif label_quarter1['text'] != "":
        back_second_round()

    else:
        back_button_first_round2()


def back_button_first_round2():
    """
    This function is called by back_button_first_round
    :return:
    """
    if label_result_player16['bg'] == "yellow":
        label_result_player16['bg'] = "white"
        label_result_player15['bg'] = "yellow"

    elif label_result_player15['bg'] == "yellow":
        label_result_player15['bg'] = "white"
        label_result_player14['bg'] = "yellow"

    elif label_result_player14['bg'] == "yellow":
        label_result_player14['bg'] = "white"
        label_result_player13['bg'] = "yellow"

    elif label_result_player13['bg'] == "yellow":
        label_result_player13['bg'] = "white"
        label_result_player12['bg'] = "yellow"

    elif label_result_player12['bg'] == "yellow":
        label_result_player12['bg'] = "white"
        label_result_player11['bg'] = "yellow"

    elif label_result_player11['bg'] == "yellow":
        label_result_player11['bg'] = "white"
        label_result_player10['bg'] = "yellow"

    elif label_result_player10['bg'] == "yellow":
        label_result_player10['bg'] = "white"
        label_result_player9['bg'] = "yellow"

    else:
        back_button_first_round3()


def back_button_first_round3():
    """
    This function is called by back_button_first_round2
    :return:
    """
    if label_result_player9['bg'] == "yellow":
        label_result_player9['bg'] = "white"
        label_result_player8['bg'] = "yellow"

    elif label_result_player8['bg'] == "yellow":
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
    This function switches the labels of the player names in the second round backwards
    :return:
    """
    if label_result_quarter8['bg'] == "yellow":
        label_result_quarter8['bg'] = "white"
        label_result_quarter7['bg'] = "yellow"

    if label_result_quarter7['bg'] == "yellow":
        label_result_quarter7['bg'] = "white"
        label_result_quarter6['bg'] = "yellow"

    if label_result_quarter6['bg'] == "yellow":
        label_result_quarter6['bg'] = "white"
        label_result_quarter5['bg'] = "yellow"

    if label_result_quarter5['bg'] == "yellow":
        label_result_quarter5['bg'] = "white"
        label_result_quarter4['bg'] = "yellow"

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
    This function switches the labels of the player names in the third round backwards
    :return:
    """
    if label_result_semi4['bg'] == "yellow":
        label_result_semi4['bg'] = "white"
        label_result_semi3['bg'] = "yellow"

    elif label_result_semi3['bg'] == "yellow":
        label_result_semi3['bg'] = "white"
        label_result_semi2['bg'] = "yellow"

    elif label_result_semi2['bg'] == "yellow":
        label_result_semi2['bg'] = "white"
        label_result_semi1['bg'] = "yellow"


def back_fourth_round():
    """
    This function switches the labels of the player names in the fourth round backwards
    :return:
    """
    if label_result_final2['bg'] == "yellow":
        label_result_final2['bg'] = "white"
        label_result_final1['bg'] = "yellow"


def next_button_first_round():
    """
    This function switches the labels of the player names forwards
    :return:
    """
    if label_final1['text'] != "":
        next_fourth_round()

    elif label_semi1['text'] != "":
        next_third_round()

    elif label_quarter1['text'] != "":
        next_second_round()

    else:
        next_button_first_round2()


def next_button_first_round2():
    """
    This function is called by next_button_first_round
    :return:
    """
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

    else:
        next_button_first_round3()


def next_button_first_round3():
    """
    This function is called by next_button_first_round2
    :return:
    """
    if label_result_player8['bg'] == "yellow":
        if label_mode_8players['bg'] == "yellow":
            if check_if_all_labels_filled():
                label_result_player8['bg'] = "white"
                calculate1()
        else:
            label_result_player8['bg'] = "white"
            label_result_player9['bg'] = "yellow"

    else:
        next_button_first_round4()


def next_button_first_round4():
    """
    This function is called by next_button_first_round3
    :return:
    """
    if label_result_player9['bg'] == "yellow":
        label_result_player9['bg'] = "white"
        label_result_player10['bg'] = "yellow"

    elif label_result_player10['bg'] == "yellow":
        label_result_player10['bg'] = "white"
        label_result_player11['bg'] = "yellow"

    elif label_result_player11['bg'] == "yellow":
        label_result_player11['bg'] = "white"
        label_result_player12['bg'] = "yellow"

    elif label_result_player12['bg'] == "yellow":
        label_result_player12['bg'] = "white"
        label_result_player13['bg'] = "yellow"

    elif label_result_player13['bg'] == "yellow":
        label_result_player13['bg'] = "white"
        label_result_player14['bg'] = "yellow"

    elif label_result_player14['bg'] == "yellow":
        label_result_player14['bg'] = "white"
        label_result_player15['bg'] = "yellow"

    elif label_result_player15['bg'] == "yellow":
        label_result_player15['bg'] = "white"
        label_result_player16['bg'] = "yellow"

    elif label_result_player16['bg'] == "yellow":
        if check_if_all_labels_filled():
            label_result_player16['bg'] = "white"
            calculate1()


def next_second_round():
    """
    This function switches the labels of the player names in the second round forwards
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
        if label_mode_8players['bg'] == "yellow":
            if check_if_all_labels_filled2():
                label_result_quarter4['bg'] = "white"
                calculate2()
        else:
            label_result_quarter4['bg'] = "white"
            label_result_quarter5['bg'] = "yellow"

    else:
        next_second_round2()


def next_second_round2():
    """
    This function is called by next_second_round
    :return:
    """
    if label_result_quarter5['bg'] == "yellow":
        label_result_quarter5['bg'] = "white"
        label_result_quarter6['bg'] = "yellow"

    elif label_result_quarter6['bg'] == "yellow":
        label_result_quarter6['bg'] = "white"
        label_result_quarter7['bg'] = "yellow"

    elif label_result_quarter7['bg'] == "yellow":
        label_result_quarter7['bg'] = "white"
        label_result_quarter8['bg'] = "yellow"

    elif label_result_quarter8['bg'] == "yellow":
        if check_if_all_labels_filled2():
            label_result_quarter8['bg'] = "white"
            calculate2()

    if label_mode_4players['bg'] == "yellow":
        button_enter_results.pack()
        button_enter_results.pack_forget()


def next_third_round():
    """
    This function switches the labels of the player names in the third round forwards
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
        if not label_mode_16players['bg'] == "yellow":
            if check_if_all_labels_filled3():
                label_result_semi2['bg'] = "white"
                calculate3()
        else:
            label_result_semi2['bg'] = "white"
            label_result_semi3['bg'] = "yellow"

    elif label_result_semi3['bg'] == "yellow":
        label_result_semi3['bg'] = "white"
        label_result_semi4['bg'] = "yellow"

    elif label_result_semi4['bg'] == "yellow":
        if check_if_all_labels_filled4():
            label_result_semi4['bg'] = "white"
            calculate4()


def next_fourth_round():
    """
    This function switches the labels of the player names in the fourth round forwards
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

    if label_result_final1['bg'] == "yellow":
        label_result_final1['bg'] = "white"
        label_result_final2['bg'] = "yellow"

    elif label_result_final2['bg'] == "yellow":
        if check_if_all_labels_filled5():
            label_result_final2['bg'] = "white"
            calculate5()


def check_if_all_labels_filled():
    """
    After entering the results we need a check if all labels are filled
    :return: true if check of the labels are successful, otherwise false
    """
    if label_result_player1['text'] == "" or label_result_player2['text'] == "" \
            or label_result_player3['text'] == "" or label_result_player4['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.1")
        return False

    if int(label_result_player1['text']) == int(label_result_player2['text']) \
            or int(label_result_player3['text']) == int(label_result_player4['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.2")
        return False

    if label_mode_8players['bg'] == "yellow" or label_mode_16players['bg'] == "yellow":
        if label_result_player5['text'] == "" or label_result_player6['text'] == "" \
                or label_result_player7['text'] == "" or label_result_player8['text'] == "":
            messagebox.showinfo("Error", "Check if everything has been entered correctly.3")
            return False

        if int(label_result_player5['text']) == int(label_result_player6['text']) \
                or int(label_result_player7['text']) == int(label_result_player8['text']):
            messagebox.showinfo("Error", "Check if everything has been entered correctly.4")
            return False

        if label_mode_16players['bg'] == "yellow":
            if not check_if_all_labels_filled_16_players():
                return False

    return True


def check_if_all_labels_filled_16_players():
    """
    Check if all labels filled when 16 players participate
    :return: true if check of the labels are successful, otherwise false
    """
    if label_result_player9['text'] == "" or label_result_player10['text'] == "" \
            or label_result_player11['text'] == "" or label_result_player12['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if label_result_player13['text'] == "" or label_result_player14['text'] == "" \
            or label_result_player15['text'] == "" or label_result_player16['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if int(label_result_player9['text']) == int(label_result_player10['text']) \
            or int(label_result_player11['text']) == int(label_result_player12['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if int(label_result_player13['text']) == int(label_result_player14['text']) \
            or int(label_result_player15['text']) == int(label_result_player16['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    return True


def check_if_all_labels_filled2():
    """
    After entering the results of the second round we need a check if all labels are filled
    :return: true if check of the labels are successful, otherwise false
    """
    if label_result_quarter1['text'] == "" or label_result_quarter2['text'] == "" \
            or int(label_result_quarter1['text']) == int(label_result_quarter2['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if label_mode_8players['bg'] == "yellow" or label_mode_16players['bg'] == "yellow":
        if label_result_quarter3['text'] == "" or label_result_quarter4['text'] == "" \
                or int(label_result_quarter3['text']) == int(label_result_quarter4['text']):
            messagebox.showinfo("Error", "Check if everything has been entered correctly.")
            return False

    if label_mode_16players['bg'] == "yellow":
        if label_result_quarter5['text'] == "" or label_result_quarter5['text'] == "":
            messagebox.showinfo("Error", "Check if everything has been entered correctly.")
            return False

        if label_result_quarter7['text'] == "" or label_result_quarter8['text'] == "":
            messagebox.showinfo("Error", "Check if everything has been entered correctly.")
            return False

        if int(label_result_quarter5['text']) == int(label_result_quarter6['text']) \
                or int(label_result_quarter7['text']) == int(label_result_quarter8['text']):
            messagebox.showinfo("Error", "Check if everything has been entered correctly.")
            return False

    return True


def check_if_all_labels_filled3():
    """
    After entering the results of the third round we need a check if all labels are filled
    :return: true if check of the labels are successful, otherwise false
    """
    if label_result_semi1['text'] == "" or label_result_semi2['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if int(label_result_semi1['text']) == int(label_result_semi2['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    return True


def check_if_all_labels_filled4():
    """
    After entering the results of the third round we need a check if all labels are filled
    Check only if 16 players were chosen
    :return: true if check of the labels are successful, otherwise false
    """
    if not check_if_all_labels_filled3():
        return False

    if label_result_semi3['text'] == "" or label_result_semi4['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    if int(label_result_semi3['text']) == int(label_result_semi4['text']):
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    return True


def check_if_all_labels_filled5():
    """
    After entering the results of the fourth round we need a check if all labels are filled
    :return: true if check of the labels are successful, otherwise false
    """
    if label_result_final1['text'] == "" or label_result_final2['text'] == "":
        messagebox.showinfo("Error", "Check if everything has been entered correctly.")
        return False

    return True


def calculate1():
    """
    Calculate the winners of the first round
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
    if label_mode_8players['bg'] == "yellow" or label_mode_16players['bg'] == "yellow":
        if int(label_result_player5['text']) > int(label_result_player6['text']):
            label_quarter3['text'] = label_player5_name['text']
        else:
            label_quarter3['text'] = label_player6_name['text']

        if int(label_result_player7['text']) > int(label_result_player8['text']):
            label_quarter4['text'] = label_player7_name['text']
        else:
            label_quarter4['text'] = label_player8_name['text']

        if label_mode_16players['bg'] == "yellow":
            calculate_help_16players()

    button_enter_results.pack()
    button_enter_results.place(x=5, y=10, height=30, width=130)


def calculate_help_16players():
    """
    Calculate the winners of the first round when 16 player participate
    :return:
    """
    if int(label_result_player9['text']) > int(label_result_player10['text']):
        label_quarter5['text'] = label_player9_name['text']
    else:
        label_quarter5['text'] = label_player10_name['text']

    if int(label_result_player11['text']) > int(label_result_player12['text']):
        label_quarter6['text'] = label_player11_name['text']
    else:
        label_quarter6['text'] = label_player12_name['text']

    if int(label_result_player13['text']) > int(label_result_player14['text']):
        label_quarter7['text'] = label_player13_name['text']
    else:
        label_quarter7['text'] = label_player14_name['text']

    if int(label_result_player15['text']) > int(label_result_player16['text']):
        label_quarter8['text'] = label_player15_name['text']
    else:
        label_quarter8['text'] = label_player16_name['text']


def calculate2():
    """
    Calculate the winners of the second round
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

    # check which player has won the second round und set him to the
    # quarter, semi-finals or winner (4 players)
    if label_mode_4players['bg'] == "yellow":
        if int(label_result_quarter1['text']) > int(label_result_quarter2['text']):
            label_winner_4players['text'] = label_quarter1['text']
        else:
            label_winner_4players['text'] = label_quarter2['text']

        label_winner_4players['bg'] = "yellow"
        messagebox.showinfo("Info", label_winner_4players['text'] +
                            " is the winner of the tournament!")

        end_game()

    elif label_mode_8players['bg'] == "yellow" or label_mode_16players['bg'] == "yellow":
        if int(label_result_quarter1['text']) > int(label_result_quarter2['text']):
            label_semi1['text'] = label_quarter1['text']
        else:
            label_semi1['text'] = label_quarter2['text']

        if int(label_result_quarter3['text']) > int(label_result_quarter4['text']):
            label_semi2['text'] = label_quarter3['text']
        else:
            label_semi2['text'] = label_quarter4['text']

        if label_mode_16players['bg'] == "yellow":
            calculate2_1()
        else:
            button_enter_results.pack()
            button_enter_results.place(x=5, y=10, height=30, width=130)


def calculate2_1():
    """
    Calculate the winners of the second round
    :return:
    """
    if int(label_result_quarter5['text']) > int(label_result_quarter6['text']):
        label_semi3['text'] = label_quarter5['text']
    else:
        label_semi3['text'] = label_quarter6['text']

    if int(label_result_quarter7['text']) > int(label_result_quarter8['text']):
        label_semi4['text'] = label_quarter7['text']
    else:
        label_semi4['text'] = label_quarter8['text']

    button_enter_results.pack()
    button_enter_results.place(x=5, y=10, height=30, width=130)


def calculate3():
    """
    Calculate the winners of the third round
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


def calculate4():
    """
    Calculate the winners of the fourth round
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
        label_final1['text'] = label_semi1['text']
    else:
        label_final1['text'] = label_semi2['text']

    if int(label_result_semi3['text']) > int(label_result_semi4['text']):
        label_final2['text'] = label_semi3['text']
    else:
        label_final2['text'] = label_semi4['text']

    button_enter_results.pack()
    button_enter_results.place(x=5, y=10, height=30, width=130)


def calculate5():
    """
    Calculate the winners of the last round
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

    if int(label_result_final1['text']) > int(label_result_final2['text']):
        label_winner_16players['text'] = label_final1['text']
    else:
        label_winner_16players['text'] = label_final2['text']

    label_winner_16players['bg'] = "yellow"
    messagebox.showinfo("Info", label_winner_16players['text'] +
                        " is the winner of the tournament!")
    end_game()


def plus_first_round():
    """
    This function increments the score of the players in the first round
    :return:
    """
    if label_mode_16players['bg'] == "yellow" and label_final1['text'] != "":
        plus_fourth_round()

    elif label_semi1['text'] != "":
        plus_third_round()

    elif label_quarter1['text'] != "":
        plus_second_round()

    else:
        plus_first_round2()


def plus_first_round2():
    """
    This function increments the score of the players in the first round
    :return:
    """
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

    else:
        plus_first_round3()


def plus_first_round3():
    """
    This function increments the score of the players in the first round
    :return:
    """
    if label_result_player4['bg'] == "yellow":
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

    else:
        plus_first_round4()


def plus_first_round4():
    """
    This function increments the score of the players in the first round
    :return:
    """
    if label_result_player7['bg'] == "yellow":
        if label_result_player7['text'] == "":
            label_result_player7['text'] = "1"
        else:
            label_result_player7['text'] = int(label_result_player7['text']) + 1

    elif label_result_player8['bg'] == "yellow":
        if label_result_player8['text'] == "":
            label_result_player8['text'] = "1"
        else:
            label_result_player8['text'] = int(label_result_player8['text']) + 1

    elif label_result_player9['bg'] == "yellow":
        if label_result_player9['text'] == "":
            label_result_player9['text'] = "1"
        else:
            label_result_player9['text'] = int(label_result_player9['text']) + 1

    else:
        plus_first_round5()


def plus_first_round5():
    """
    This function increments the score of the players in the first round
    :return:
    """
    if label_result_player10['bg'] == "yellow":
        if label_result_player10['text'] == "":
            label_result_player10['text'] = "1"
        else:
            label_result_player10['text'] = int(label_result_player10['text']) + 1

    elif label_result_player11['bg'] == "yellow":
        if label_result_player11['text'] == "":
            label_result_player11['text'] = "1"
        else:
            label_result_player11['text'] = int(label_result_player11['text']) + 1

    elif label_result_player12['bg'] == "yellow":
        if label_result_player12['text'] == "":
            label_result_player12['text'] = "1"
        else:
            label_result_player12['text'] = int(label_result_player12['text']) + 1

    else:
        plus_first_round6()


def plus_first_round6():
    """
    This function increments the score of the players in the first round
    :return:
    """
    if label_result_player13['bg'] == "yellow":
        if label_result_player13['text'] == "":
            label_result_player13['text'] = "1"
        else:
            label_result_player13['text'] = int(label_result_player13['text']) + 1

    elif label_result_player14['bg'] == "yellow":
        if label_result_player14['text'] == "":
            label_result_player14['text'] = "1"
        else:
            label_result_player14['text'] = int(label_result_player14['text']) + 1

    elif label_result_player15['bg'] == "yellow":
        if label_result_player15['text'] == "":
            label_result_player15['text'] = "1"
        else:
            label_result_player15['text'] = int(label_result_player15['text']) + 1

    else:
        plus_first_round7()


def plus_first_round7():
    """
    This function increments the score of the players in the first round
    :return:
    """
    if label_result_player16['bg'] == "yellow":
        if label_result_player16['text'] == "":
            label_result_player16['text'] = "1"
        else:
            label_result_player16['text'] = int(label_result_player16['text']) + 1


def minus_first_round():
    """
    This function decrements the score of the players in the first round
    :return:
    """
    if label_mode_16players['bg'] == "yellow" and label_final1['text'] != "":
        minus_fourth_round()

    elif label_semi1['text'] != "":
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

        else:
            minus_first_round2()


def minus_first_round2():
    """
    This function decrements the score of the players in the first round
    :return:
    """
    if label_result_player3['bg'] == "yellow":
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

    else:
        minus_first_round3()


def minus_first_round3():
    """
    This function decrements the score of the players in the first round
    :return:
    """
    if label_result_player6['bg'] == "yellow":
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
            label_result_player8['text'] = int(label_result_player8['text'])

    else:
        minus_first_round4()


def minus_first_round4():
    """
    This function decrements the score of the players in the first round
    :return:
    """
    if label_result_player9['bg'] == "yellow":
        if label_result_player9['text'] == "":
            label_result_player9['text'] = "0"
        elif int(label_result_player9['text']) > 0:
            label_result_player9['text'] = int(label_result_player9['text']) - 1

    elif label_result_player10['bg'] == "yellow":
        if label_result_player10['text'] == "":
            label_result_player10['text'] = "0"
        elif int(label_result_player10['text']) > 0:
            label_result_player10['text'] = int(label_result_player10['text']) - 1

    elif label_result_player11['bg'] == "yellow":
        if label_result_player11['text'] == "":
            label_result_player11['text'] = "0"
        elif int(label_result_player11['text']) > 0:
            label_result_player11['text'] = int(label_result_player11['text']) - 1

    else:
        minus_first_round5()


def minus_first_round5():
    """
    This function decrements the score of the players in the first round
    :return:
    """
    if label_result_player12['bg'] == "yellow":
        if label_result_player12['text'] == "":
            label_result_player12['text'] = "0"
        elif int(label_result_player12['text']) > 0:
            label_result_player12['text'] = int(label_result_player12['text']) - 1

    elif label_result_player13['bg'] == "yellow":
        if label_result_player13['text'] == "":
            label_result_player13['text'] = "0"
        elif int(label_result_player13['text']) > 0:
            label_result_player13['text'] = int(label_result_player13['text']) - 1

    elif label_result_player14['bg'] == "yellow":
        if label_result_player14['text'] == "":
            label_result_player14['text'] = "0"
        elif int(label_result_player14['text']) > 0:
            label_result_player14['text'] = int(label_result_player14['text']) - 1

    else:
        minus_first_round6()


def minus_first_round6():
    """
    This function decrements the score of the players in the first round
    :return:
    """
    if label_result_player15['bg'] == "yellow":
        if label_result_player15['text'] == "":
            label_result_player15['text'] = "0"
        elif int(label_result_player15['text']) > 0:
            label_result_player15['text'] = int(label_result_player15['text']) - 1

    elif label_result_player16['bg'] == "yellow":
        if label_result_player16['text'] == "":
            label_result_player16['text'] = "0"
        elif int(label_result_player16['text']) > 0:
            label_result_player16['text'] = int(label_result_player16['text']) - 1


def plus_second_round():
    """
    This function increments the score of the players in the second round
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

    else:
        plus_second_round2()


def plus_second_round2():
    """
    This function increments the score of the players in the second round
    :return:
    """
    if label_result_quarter4['bg'] == "yellow":
        if label_result_quarter4['text'] == "":
            label_result_quarter4['text'] = "1"
        else:
            label_result_quarter4['text'] = int(label_result_quarter4['text']) + 1

    elif label_result_quarter5['bg'] == "yellow":
        if label_result_quarter5['text'] == "":
            label_result_quarter5['text'] = "1"
        else:
            label_result_quarter5['text'] = int(label_result_quarter5['text']) + 1

    elif label_result_quarter6['bg'] == "yellow":
        if label_result_quarter6['text'] == "":
            label_result_quarter6['text'] = "1"
        else:
            label_result_quarter6['text'] = int(label_result_quarter6['text']) + 1

    else:
        plus_second_round3()


def plus_second_round3():
    """
    This function increments the score of the players in the second round
    :return:
    """
    if label_result_quarter7['bg'] == "yellow":
        if label_result_quarter7['text'] == "":
            label_result_quarter7['text'] = "1"
        else:
            label_result_quarter7['text'] = int(label_result_quarter7['text']) + 1

    elif label_result_quarter8['bg'] == "yellow":
        if label_result_quarter8['text'] == "":
            label_result_quarter8['text'] = "1"
        else:
            label_result_quarter8['text'] = int(label_result_quarter8['text']) + 1


def minus_second_round():
    """
    This function decrements the score of the players in the second round
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

    else:
        minus_second_round2()


def minus_second_round2():
    """
    This function decrements the score of the players in the second round
    :return:
    """
    if label_result_quarter4['bg'] == "yellow":
        if label_result_quarter4['text'] == "":
            label_result_quarter4['text'] = "0"
        elif int(label_result_quarter4['text']) > 0:
            label_result_quarter4['text'] = int(label_result_quarter4['text']) - 1

    elif label_result_quarter5['bg'] == "yellow":
        if label_result_quarter5['text'] == "":
            label_result_quarter5['text'] = "0"
        elif int(label_result_quarter5['text']) > 0:
            label_result_quarter5['text'] = int(label_result_quarter5['text']) - 1

    elif label_result_quarter6['bg'] == "yellow":
        if label_result_quarter6['text'] == "":
            label_result_quarter6['text'] = "0"
        elif int(label_result_quarter6['text']) > 0:
            label_result_quarter6['text'] = int(label_result_quarter6['text']) - 1

    else:
        minus_second_round3()


def minus_second_round3():
    """
    This function decrements the score of the players in the second round
    :return:
    """
    if label_result_quarter7['bg'] == "yellow":
        if label_result_quarter7['text'] == "":
            label_result_quarter7['text'] = "0"
        elif int(label_result_quarter7['text']) > 0:
            label_result_quarter7['text'] = int(label_result_quarter7['text']) - 1

    elif label_result_quarter8['bg'] == "yellow":
        if label_result_quarter8['text'] == "":
            label_result_quarter8['text'] = "0"
        elif int(label_result_quarter8['text']) > 0:
            label_result_quarter8['text'] = int(label_result_quarter8['text']) - 1


def plus_third_round():
    """
    This function increments the score of the players in the third round
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

    elif label_result_semi3['bg'] == "yellow":
        if label_result_semi3['text'] == "":
            label_result_semi3['text'] = "1"
        else:
            label_result_semi3['text'] = int(label_result_semi3['text']) + 1

    elif label_result_semi4['bg'] == "yellow":
        if label_result_semi4['text'] == "":
            label_result_semi4['text'] = "1"
        else:
            label_result_semi4['text'] = int(label_result_semi4['text']) + 1


def plus_fourth_round():
    """
    This function increments the score of the players in the fourth round
    :return:
    """
    if label_result_final1['bg'] == "yellow":
        if label_result_final1['text'] == "":
            label_result_final1['text'] = "1"
        else:
            label_result_final1['text'] = int(label_result_final1['text']) + 1

    elif label_result_final2['bg'] == "yellow":
        if label_result_final2['text'] == "":
            label_result_final2['text'] = "1"
        else:
            label_result_final2['text'] = int(label_result_final2['text']) + 1


def minus_third_round():
    """
    This function decrements the score of the players in the third round
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

    elif label_result_semi3['bg'] == "yellow":
        if label_result_semi3['text'] == "":
            label_result_semi3['text'] = "0"
        elif int(label_result_semi3['text']) > 0:
            label_result_semi3['text'] = int(label_result_semi3['text']) - 1

    elif label_result_semi4['bg'] == "yellow":
        if label_result_semi4['text'] == "":
            label_result_semi4['text'] = "0"
        elif int(label_result_semi4['text']) > 0:
            label_result_semi4['text'] = int(label_result_semi4['text']) - 1


def minus_fourth_round():
    """
    This function decrements the score of the players in the fourth round
    """
    if label_result_final1['bg'] == "yellow":
        if label_result_final1['text'] == "":
            label_result_final1['text'] = "0"
        elif int(label_result_final1['text']) > 0:
            label_result_final1['text'] = int(label_result_final1['text']) - 1

    elif label_result_final2['bg'] == "yellow":
        if label_result_final2['text'] == "":
            label_result_final2['text'] = "0"
        elif int(label_result_final2['text']) > 0:
            label_result_final2['text'] = int(label_result_final2['text']) - 1


def end_game():
    """
    This function is called when the tournament tree is completely full
    :return:
    """
    button_enter_results.pack()
    button_enter_results.pack_forget()


def start():
    """
    After the mode has been selected, all names must be entered
    """
    start_button.pack()
    label_mode_4players.pack()
    label_mode_8players.pack()
    label_mode_16players.pack()
    switch_mode_button.pack()

    start_button.pack_forget()
    label_mode_4players.pack_forget()
    label_mode_8players.pack_forget()
    label_mode_16players.pack_forget()
    switch_mode_button.pack_forget()

    label_name_order1.pack()
    label_name_order2.pack()
    button_switch_order.pack()
    label_name_order1.place(x=637.5, y=30, height=30, width=100)
    label_name_order2.place(x=537.5, y=30, height=30, width=100)
    button_switch_order.place(x=587.5, y=0, height=30, width=100)

    # 4 names always required
    input_name1.pack()
    input_name2.pack()
    input_name3.pack()
    input_name4.pack()

    input_name1.place(x=337.5, y=132.5, height=30, width=250)
    input_name2.place(x=337.5, y=182.5, height=30, width=250)
    input_name3.place(x=337.5, y=232.5, height=30, width=250)
    input_name4.place(x=337.5, y=282.5, height=30, width=250)

    start2()


def start2():
    """
    This functions starts the tournament tree
    :return:
    """
    if label_mode_8players['bg'] == "yellow":
        input_name5.pack()
        input_name6.pack()
        input_name7.pack()
        input_name8.pack()

        input_name5.place(x=687.5, y=132.5, height=30, width=250)
        input_name6.place(x=687.5, y=182.5, height=30, width=250)
        input_name7.place(x=687.5, y=232.5, height=30, width=250)
        input_name8.place(x=687.5, y=282.5, height=30, width=250)

        # enable label with entering all names
        label_info_names.pack()
        label_info_names.place(x=537.5, y=82.5, height=30, width=200)

    elif label_mode_16players['bg'] == "yellow":
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

        # enable label with entering all names
        label_info_names.pack()
        label_info_names.place(x=537.5, y=82.5, height=30, width=200)

    else:
        # for 4 players
        # enable label with entering all names
        label_info_names.pack()
        label_info_names.place(x=362.5, y=82.5, height=30, width=200)

    # enable button for next step and read the given names
    button_enter_names.pack()
    button_enter_names.place(x=1175, y=282.5, height=30, width=100)


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

    # define button for switching mode (4, 8 or 16 players)
    switch_mode_button = Button(gui, text="Switch mode", bd=1, fg="black", bg="white",
                                font=('Arial', 10), command=switch_mode)

    switch_mode_button.place(x=412.4, y=0, height=30, width=100)

    # define labels for switching mode (4 or 8 players)
    label_mode_4players = Label(gui, text="4 Players", bg="yellow", font=('Arial', 10))
    label_mode_8players = Label(gui, text="8 Players", bg="white", font=('Arial', 10))
    label_mode_16players = Label(gui, text="16 Players", bg="white", font=('Arial', 10))

    label_mode_4players.place(x=532.5, y=0, height=30, width=70)
    label_mode_8players.place(x=602.5, y=0, height=30, width=70)
    label_mode_16players.place(x=672.5, y=0, height=30, width=70)

    # define start-button after the mode was chosen the tournament tree can be created
    start_button = Button(gui, text="Start", bg="lightgreen", font=('Arial', 10),
                          command=start)
    start_button.place(x=762.5, y=0, height=30, width=100)

    # define reset - button
    reset_button = Button(gui, text="Reset", bg="red", font=('Arial', 10, 'bold'), command=reset)
    reset_button.place(x=1175, y=80, height=30, width=100)

    # define button for entering results
    button_enter_results = Button(gui, text="Enter results", bd=1, fg="black", bg="lightgreen",
                                  font=('Arial', 10), command=enter_results)

    # define next-button for entering results
    button_next = Button(gui, text="Next", bd=1, fg="black", bg="lightgreen",
                         font=('Arial', 10), command=next_button_first_round)

    # define back-button for entering results
    button_back = Button(gui, text="Back", bd=1, fg="black", bg="lightgreen",
                         font=('Arial', 10), command=back_button_first_round)

    # define plus and minus buttons
    button_minus = Button(gui, text="-", bd=1, fg="black", bg="red",
                          font=('Arial', 10), command=minus_first_round)

    button_plus = Button(gui, text="+", bd=1, fg="black", bg="lightgreen",
                         font=('Arial', 10), command=plus_first_round)

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

    # define label for entering names
    label_info_names = Label(gui, text="Please enter all names", font=('Arial', 10))

    # define button for entering names

    button_enter_names = Button(gui, text="Continue", bg="lightgreen",
                                font=('Arial', 10), command=check_names)

    # define button and label for name - order
    label_name_order1 = Label(gui, text="Random order", bg="yellow", font=('Arial', 10))
    label_name_order2 = Label(gui, text="Entered order", bg="white", font=('Arial', 10))
    button_switch_order = Button(gui, text="Choose order", bg="lightgreen",
                                 font=('Arial', 10), command=switch_order)

    # ---------------------------------------------------------------------------------------------#
    # define labels for 16 player names
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

    # define labels for 8 quarter finals
    label_quarter1 = Label(gui, text="", font=('Arial', 10))
    label_quarter2 = Label(gui, text="", font=('Arial', 10))
    label_quarter3 = Label(gui, text="", font=('Arial', 10))
    label_quarter4 = Label(gui, text="", font=('Arial', 10))

    label_quarter5 = Label(gui, text="", font=('Arial', 10))
    label_quarter6 = Label(gui, text="", font=('Arial', 10))
    label_quarter7 = Label(gui, text="", font=('Arial', 10))
    label_quarter8 = Label(gui, text="", font=('Arial', 10))

    # define labels for 4 semi finals
    label_semi1 = Label(gui, text="", font=('Arial', 10))
    label_semi2 = Label(gui, text="", font=('Arial', 10))

    label_semi3 = Label(gui, text="", font=('Arial', 10))
    label_semi4 = Label(gui, text="", font=('Arial', 10))

    # define labels for 2 finals
    label_final1 = Label(gui, text="", font=('Arial', 10))
    label_final2 = Label(gui, text="", font=('Arial', 10))

    # define label for winner for 4 players
    label_winner_4players = Label(gui, text="", font=('Arial', 10))

    # define label for winner for 8 players
    label_winner_8players = Label(gui, text="", font=('Arial', 10))

    # define label for winner for 16 players
    label_winner_16players = Label(gui, text="", font=('Arial', 10))

    # define result - labels for players 1-16
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

    # define result - labels for 8 quarter
    label_result_quarter1 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter2 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter3 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter4 = Label(gui, text="", font=('Arial', 10))

    label_result_quarter5 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter6 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter7 = Label(gui, text="", font=('Arial', 10))
    label_result_quarter8 = Label(gui, text="", font=('Arial', 10))

    # define result - labels for 4 semi
    label_result_semi1 = Label(gui, text="", font=('Arial', 10))
    label_result_semi2 = Label(gui, text="", font=('Arial', 10))
    label_result_semi3 = Label(gui, text="", font=('Arial', 10))
    label_result_semi4 = Label(gui, text="", font=('Arial', 10))

    # define labels for 2 finals
    label_result_final1 = Label(gui, text="", font=('Arial', 10))
    label_result_final2 = Label(gui, text="", font=('Arial', 10))

    gui.mainloop()
