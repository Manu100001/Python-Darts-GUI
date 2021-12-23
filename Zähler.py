#!/usr/bin/python3
"""
This script will help you play darts.
If you don't have an electric dartboard but a normal one,
this script will help you to calculate the scores.

:author: Manuel Milde manuelmilde@gmx.net
:copyright: 2021 Manuel Milde
"""
import sqlite3
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os

global_darts_counter = 0


def T20():
    """

    :return:
    """
    label_dart_score['text'] = "60"


def T19():
    """"
    """
    label_dart_score['text'] = "57"


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


def button_name_1():
    """

    :return:
    """
    name = eingabefeld_p1.get()
    eingabefeld_p1.delete("0", "end")
    label_player_1_name['text'] = name


def button_name_2():
    """

    :return:
    """
    name = eingabefeld_p2.get()
    eingabefeld_p2.delete("0", "end")
    label_player_2_name['text'] = name


def button_name_3():
    """


    :return:
    """
    name = eingabefeld_p3.get()
    eingabefeld_p3.delete("0", "end")
    label_player_3_name['text'] = name


def button_name_4():
    """

    :return:
    """
    name = eingabefeld_p4.get()
    eingabefeld_p4.delete("0", "end")
    label_player_4_name['text'] = name


def button_switch_score_inc():
    """

    :return:
    """
    label_switch_score['text'] = "501"
    label_1_score['text'] = "501"
    label_2_score['text'] = "501"
    label_3_score['text'] = "501"
    label_4_score['text'] = "501"


def button_switch_score_dec():
    """

    :return:
    """
    label_switch_score['text'] = "301"
    label_1_score['text'] = "301"
    label_2_score['text'] = "301"
    label_3_score['text'] = "301"
    label_4_score['text'] = "301"


def button_stop_game_function():
    """

    :return:
    """
    button_stop_game.pack()
    button_stop_game.pack_forget()

    next_button.pack()
    next_button.pack_forget()

    button_start_game.pack()
    button_start_game.place(x=850, y=90, height=30, width=100)

    button_name_1.pack()
    button_name_2.pack()
    button_name_3.pack()
    button_name_4.pack()

    button_name_1.place(x=850, y=5, height=30)
    button_name_2.place(x=850, y=35, height=30)
    button_name_3.place(x=1000, y=5, height=30)
    button_name_4.place(x=1000, y=35, height=30)

    eingabefeld_p1.pack()
    eingabefeld_p2.pack()
    eingabefeld_p3.pack()
    eingabefeld_p4.pack()

    eingabefeld_p1.place(x=750, y=5, width=100, height=30)
    eingabefeld_p2.place(x=750, y=35, width=100, height=30)
    eingabefeld_p3.place(x=900, y=5, width=100, height=30)
    eingabefeld_p4.place(x=900, y=35, width=100, height=30)

    label_switch_score.pack()
    button_switch_score_dec.pack()
    button_switch_score_inc.pack()

    label_switch_score.place(x=1030, y=90, height=30, width=110)
    button_switch_score_dec.place(x=1140, y=90, height=30, width=30)
    button_switch_score_inc.place(x=1170, y=90, height=30, width=30)

    label_dart_score.pack()
    button_dart_score.pack()

    label_dart_score.pack_forget()
    button_dart_score.pack_forget()

    label_first_dart.pack()
    label_second_dart.pack()
    label_third_dart.pack()
    zwischen_label.pack()

    label_first_dart.pack_forget()
    label_second_dart.pack_forget()
    label_third_dart.pack_forget()
    zwischen_label.pack_forget()


def button_start_game_function():
    """

    :return:
    """
    label_1_score['bg'] = "yellow"

    button_start_game.pack()
    button_start_game.pack_forget()
    button_name_1.pack()
    button_name_1.pack_forget()
    button_name_2.pack()
    button_name_2.pack_forget()
    button_name_3.pack()
    button_name_3.pack_forget()
    button_name_4.pack()
    button_name_4.pack_forget()

    eingabefeld_p1.pack()
    eingabefeld_p1.pack_forget()
    eingabefeld_p2.pack()
    eingabefeld_p2.pack_forget()
    eingabefeld_p3.pack()
    eingabefeld_p3.pack_forget()
    eingabefeld_p4.pack()
    eingabefeld_p4.pack_forget()

    button_switch_score_inc.pack()
    button_switch_score_inc.pack_forget()
    button_switch_score_dec.pack()
    button_switch_score_dec.pack_forget()
    label_switch_score.pack()
    label_switch_score.pack_forget()

    button_stop_game.pack()
    button_stop_game.place(x=950, y=90, height=30, width=100)

    next_button.pack()
    next_button.place(x=610, y=60, height=30, width=100)

    label_dart_score.pack()
    button_dart_score.pack()

    label_dart_score.place(x=0, y=300, height=30, width=90)
    button_dart_score.place(x=90, y=300, height=30, width=80)

    label_first_dart.pack()
    label_second_dart.pack()
    label_third_dart.pack()
    zwischen_label.pack()

    label_first_dart.place(x=210, y=300, height=30, width=30)
    label_second_dart.place(x=250, y=300, height=30, width=30)
    label_third_dart.place(x=290, y=300, height=30, width=30)
    zwischen_label.place(x=340, y=300, height=30, width=100)


def next_button():
    """

    :return:
    """
    zwischen_label['text'] = "0"
    label_first_dart['bg'] = "yellow"
    label_second_dart['bg'] = "white"
    label_third_dart['bg'] = "white"

    if label_1_score['bg'] == "yellow":
        label_1_score['bg'] = "white"
        label_2_score['bg'] = "yellow"
        return

    if label_2_score['bg'] == "yellow":
        label_2_score['bg'] = "white"
        label_3_score['bg'] = "yellow"
        return

    if label_3_score['bg'] == "yellow":
        label_3_score['bg'] = "white"
        label_4_score['bg'] = "yellow"
        return

    if label_4_score['bg'] == "yellow":
        label_4_score['bg'] = "white"
        label_1_score['bg'] = "yellow"
        return


def next():
    """

    :return:
    """
    if label_1_score['bg'] == "yellow":
        label_1_score['bg'] = "white"
        label_2_score['bg'] = "yellow"
        return

    if label_2_score['bg'] == "yellow":
        label_2_score['bg'] = "white"
        label_3_score['bg'] = "yellow"
        return

    if label_3_score['bg'] == "yellow":
        label_3_score['bg'] = "white"
        label_4_score['bg'] = "yellow"
        return

    if label_4_score['bg'] == "yellow":
        label_4_score['bg'] = "white"
        label_1_score['bg'] = "yellow"
        return


def count_down():
    """
    This function counts the score down
    :return:
    """
    flag = False
    count_down_button.pack()
    count_down_button.pack_forget()

    button_dart_score.pack()
    button_dart_score.place(x=90, y=300, height=30, width=80)

    result = int(zwischen_label['text'])
    zwischen_label['text'] = "0"

    label_third_dart['bg'] = "white"
    label_first_dart['bg'] = "yellow"

    if label_1_score['bg'] == "yellow":
        current = int(label_1_score['text'])
        if result > current:
            messagebox.showinfo("Achtung", "Sie haben überworfen!")
        elif current > result:
            current = current - result
            label_1_score['text'] = current
        elif result == current:
            current = current - result
            label_1_score['text'] = current
            messagebox.showinfo("Info", label_player_1_name['text'] + "wins")
        else:
            messagebox.showerror("Error", "Systemerror. Bitte neustarten.")

    if label_2_score['bg'] == "yellow":
        current = int(label_2_score['text'])
        if result > current:
            messagebox.showinfo("Achtung", "Sie haben überworfen!")
        elif current > result:
            current = current - result
            label_2_score['text'] = current
        elif result == current:
            current = current - result
            label_2_score['text'] = current
            messagebox.showinfo("Info", label_player_2_name['text'] + "wins")
        else:
            messagebox.showerror("Error", "Systemerror. Bitte neustarten.")

    if label_3_score['bg'] == "yellow":
        current = int(label_3_score['text'])
        if result > current:
            messagebox.showinfo("Achtung", "Sie haben überworfen!")
        elif current > result:
            current = current - result
            label_3_score['text'] = current
        elif result == current:
            current = current - result
            label_3_score['text'] = current
            messagebox.showinfo("Info", label_player_3_name['text'] + "wins")
        else:
            messagebox.showerror("Error", "Systemerror. Bitte neustarten.")

    if label_4_score['bg'] == "yellow":
        current = int(label_4_score['text'])
        if result > current:
            messagebox.showinfo("Achtung", "Sie haben überworfen!")
        elif current > result:
            current = current - result
            label_4_score['text'] = current
        elif result == current:
            current = current - result
            label_4_score['text'] = current
            messagebox.showinfo("Info", label_player_4_name['text'] + "wins")
        else:
            messagebox.showerror("Error", "Systemerror. Bitte neustarten.")

    next()





def add():
    """

    :return:
    """
    count = int(label_dart_score['text'])
    current = int(zwischen_label['text'])
    result = current + count
    zwischen_label['text'] = result
    label_dart_score['text'] = ""

    if label_first_dart['bg'] == "yellow":
        label_first_dart['bg'] = "white"
        label_second_dart['bg'] = "yellow"
        return

    if label_second_dart['bg'] == "yellow":
        label_second_dart['bg'] = "white"
        label_third_dart['bg'] = "yellow"
        return

    if label_third_dart['bg'] == "yellow":
        count_down_button.pack()
        count_down_button.place(x=440, y=300, height=30, width=90)
        button_dart_score.pack()
        button_dart_score.pack_forget()


if __name__ == "__main__":
    # configure the window to generate
    gui = Tk()
    gui.geometry('1275x645')
    gui.resizable(width=0, height=0)
    gui.title("Dart - User Interface")
    gui.configure(background='grey')

    # define the exit - button
    exit_button = Button(gui, text="Beenden", command=button_exit, fg="black", bg="lightgreen",
                         font=('Arial', 10, 'bold'))
    exit_button.place(x=1175, y=0, height=80, width=100)

    # ################# ---------------------- ##################
    # labels for 4 players
    label_player_1_name = Label(gui, text="Player 1: ", fg="black", font=('Arial', 13, 'bold'))
    label_player_2_name = Label(gui, text="Player 2: ", fg="black", font=('Arial', 13, 'bold'))
    label_player_3_name = Label(gui, text="Player 3: ", fg="black", font=('Arial', 13, 'bold'))
    label_player_4_name = Label(gui, text="Player 4: ", fg="black", font=('Arial', 13, 'bold'))

    label_player_1_name.place(x=10, y=10, height=30, width=110)
    label_player_2_name.place(x=160, y=10, height=30, width=110)
    label_player_3_name.place(x=310, y=10, height=30, width=110)
    label_player_4_name.place(x=460, y=10, height=30, width=110)

    # ################# ---------------------- ##################
    # text input for 4 player names and buttons
    eingabefeld_p1 = Entry(gui, bd=4, font=('Arial', 13))
    eingabefeld_p2 = Entry(gui, bd=4, font=('Arial', 13))
    eingabefeld_p3 = Entry(gui, bd=4, font=('Arial', 13))
    eingabefeld_p4 = Entry(gui, bd=4, font=('Arial', 13))

    eingabefeld_p1.place(x=750, y=5, width=100, height=30)
    eingabefeld_p2.place(x=750, y=35, width=100, height=30)
    eingabefeld_p3.place(x=900, y=5, width=100, height=30)
    eingabefeld_p4.place(x=900, y=35, width=100, height=30)

    button_name_1 = Button(gui, text="P1", bd=4, fg="black", bg="grey", font=('Arial', 10),
                           command=button_name_1)
    button_name_2 = Button(gui, text="P2", bd=4, fg="black", bg="white", font=('Arial', 10),
                           command=button_name_2)
    button_name_3 = Button(gui, text="P3", bd=4, fg="black", bg="grey", font=('Arial', 10),
                           command=button_name_3)
    button_name_4 = Button(gui, text="P4", bd=4, fg="black", bg="white", font=('Arial', 10),
                           command=button_name_4)

    button_name_1.place(x=850, y=5, height=30)
    button_name_2.place(x=850, y=35, height=30)
    button_name_3.place(x=1000, y=5, height=30)
    button_name_4.place(x=1000, y=35, height=30)

    # ################# ---------------------- ##################
    # labels for game score for 4 players
    label_1_score = Label(gui, text="501", fg="black", font=('Arial', 13, 'bold'))
    label_2_score = Label(gui, text="501", fg="black", font=('Arial', 13, 'bold'))
    label_3_score = Label(gui, text="501", fg="black", font=('Arial', 13, 'bold'))
    label_4_score = Label(gui, text="501", fg="black", font=('Arial', 13, 'bold'))

    label_1_score.place(x=10, y=60, height=30, width=110)
    label_2_score.place(x=160, y=60, height=30, width=110)
    label_3_score.place(x=310, y=60, height=30, width=110)
    label_4_score.place(x=460, y=60, height=30, width=110)

    # ################# ---------------------- ##################
    # label and button for switching points
    label_switch_score = Label(gui, text="501", fg="black", font=('Arial', 13, 'bold'))
    button_switch_score_inc = Button(gui, text="+", bd=4, fg="black", bg="lightgreen", font=('Arial', 10),
                                     command=button_switch_score_inc)
    button_switch_score_dec = Button(gui, text="-", bd=4, fg="black", bg="red", font=('Arial', 10),
                                     command=button_switch_score_dec)

    label_switch_score.place(x=1105, y=90, height=30, width=110)
    button_switch_score_dec.place(x=1215, y=90, height=30, width=30)
    button_switch_score_inc.place(x=1240, y=90, height=30, width=30)

    # ################# ---------------------- ##################
    # start - button und stop - button
    button_start_game = Button(gui, text="Start", bd=4, fg="black", bg="yellow", font=('Arial', 11),
                               command=button_start_game_function)
    button_start_game.place(x=850, y=90, height=30, width=100)

    button_stop_game = Button(gui, text="Stop", bd=4, fg="black", bg="red", font=('Arial', 11),
                              command=button_stop_game_function)
    button_stop_game.pack()
    button_stop_game.pack_forget()

    # ################# ---------------------- ##################
    # next - button
    next_button = Button(gui, text="Next", bd=4, fg="black", bg="yellow", font=('Arial', 11),
                         command=next_button)
    next_button.place(x=610, y=60, height=30, width=100)
    next_button.pack()
    next_button.pack_forget()

    # ################# ---------------------- ##################
    # eingabefeld für scoring (Punkte, die abgezogen werden sollen)
    label_dart_score = Label(gui, text="20", bd=4, font=('Arial', 13))
    button_dart_score = Button(gui, text="Add", bd=4, fg="black", bg="lightgreen", font=('Arial', 10),
                               command=add)
    label_dart_score.place(x=0, y=300, height=30, width=90)
    button_dart_score.place(x=100, y=300, height=30, width=80)

    label_dart_score.pack()
    button_dart_score.pack()

    label_dart_score.pack_forget()
    button_dart_score.pack_forget()

    # ################# ---------------------- ##################
    # create Label for 1,2 and 3 Darts and zwischen and count down button
    label_first_dart = Label(gui, text="1", bd=4, bg="yellow", font=('Arial', 13))
    label_second_dart = Label(gui, text="2", bd=4, bg="white", font=('Arial', 13))
    label_third_dart = Label(gui, text="3", bd=4, bg="white", font=('Arial', 13))

    zwischen_label = Label(gui, text="0", bd=4, bg="yellow", font=('Arial', 13))
    count_down_button = Button(gui, text="Count down", bd=4, fg="black", bg="lightgreen", font=('Arial', 10),
                               command=count_down)

    label_first_dart.place(x=210, y=300, height=30, width=30)
    label_second_dart.place(x=250, y=300, height=30, width=30)
    label_third_dart.place(x=290, y=300, height=30, width=30)
    zwischen_label.place(x=340, y=300, height=30, width=100)
    count_down_button.place(x=440, y=300, height=30, width=90)

    label_first_dart.pack()
    label_second_dart.pack()
    label_third_dart.pack()
    zwischen_label.pack()
    count_down_button.pack()

    label_first_dart.pack_forget()
    label_second_dart.pack_forget()
    label_third_dart.pack_forget()
    zwischen_label.pack_forget()
    count_down_button.pack_forget()
    # ################# ---------------------- ##################
    # here set the values for all numbers (Tripel, Double and Single)
    button_triple_20 = Button(gui, text="T20", bd=4, fg="black", bg="red", font=('Arial', 14),
                              command=T20)
    button_single_20 = Button(gui, text="S20", bd=4, fg="black", bg="red", font=('Arial', 14),
                              command=next_button)
    button_double_20 = Button(gui, text="D20", bd=4, fg="black", bg="red", font=('Arial', 14),
                              command=next_button)

    button_triple_19 = Button(gui, text="T19", bd=4, fg="black", bg="green", font=('Arial', 14),
                              command=T19)
    button_single_19 = Button(gui, text="S19", bd=4, fg="black", bg="green", font=('Arial', 14),
                              command=next_button)
    button_double_19 = Button(gui, text="D19", bd=4, fg="black", bg="green", font=('Arial', 14),
                              command=next_button)

    button_triple_18 = Button(gui, text="T18", bd=4, fg="black", bg="red", font=('Arial', 14),
                              command=next_button)
    button_single_18 = Button(gui, text="S18", bd=4, fg="black", bg="red", font=('Arial', 14),
                              command=next_button)
    button_double_18 = Button(gui, text="D18", bd=4, fg="black", bg="red", font=('Arial', 14),
                              command=next_button)

    button_triple_20.place(x=0, y=400, height=60, width=100)
    button_single_20.place(x=0, y=470, height=60, width=100)
    button_double_20.place(x=0, y=540, height=60, width=100)
    button_triple_19.place(x=110, y=400, height=60, width=100)
    button_single_19.place(x=110, y=470, height=60, width=100)
    button_double_19.place(x=110, y=540, height=60, width=100)
    button_triple_18.place(x=220, y=400, height=60, width=100)
    button_single_18.place(x=220, y=470, height=60, width=100)
    button_double_18.place(x=220, y=540, height=60, width=100)
    # ################# ---------------------- ##################
    gui.mainloop()
