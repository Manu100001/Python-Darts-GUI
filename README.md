# Python-Darts-GUI
Different GUIs for playing darts

## Usage
This project is intended for private use only. \
For all other uses, my consent is mandatory. Requests for use at tournaments are possible.

## Contact
For questions, suggestions, wishes, problems and requests \
Contact me: manuelmilde@gmx.net

## Created Excel - files
The created excel - files can be found here: `../Python-Darts-GUI/Spielstände/..`

## Setup for counter (normal dartboard)
  
Step into directory 
```bash
cd Python-Darts-GUI
```

Run:

```bash
python counter.py  # to start the gui for counting
```

Description
- First, select the starting points (301 or 501), then select the number of players (minimum 2, maximum 4).
- Then enter all player names and press `Continue`.
- Now you can type in what you have thrown and press respectively `Add`. After 3 entries press `Count Down` to count down your thrown number of points from your stand.
- The next player will be chosen automatically.
- If you throw more, e.g. 60, but you only have 50 left, a message appears that you have overthrown, and it is the next players turn.
- If the first player has 0 points left, a new game will be started automatically. If there are three or four players, the game will continue until there is only one player left.
- When you have finished playing, you can press `Calculate Score`, which will create an Excel file where you can view your average and various statistics. This button appears after the first leg has been played.

Images:
- In the directory `Images/counter` are a few more pictures, which also show the processes. 

![Screenshot](Images/counter/02_counter.png?raw=true)

## Setup for tournament tree
Step into directory 
```bash
cd Python-Darts-GUI
```

Run:

```bash
python tournament_tree.py  # to start the tournament tree
```

Description:
- First select the mode (4, 8 or 16 players).
- After that enter all names for the players.
- The tree will be generated automatically.
- As you can see the tree, press the button `Enter results`. Now you are able to fill in the results.
- With `Back`, `-`, `+` and `Next` you can control the input. Once all results have been entered, simply press `Next` again.
- The next round will be caculated automatically.

Images:
- In the directory `Images/tournament_tree` are a few more pictures, which also show the processes.

![Screenshot](Images/tournament_tree/04_full_tree.png?raw=true)

## Setup for electronic dartboard
#### This can be used for an electronic dartboard or for playing best of sets/legs or for getting suggestions for checkouts
Step into directory 
```bash
cd Python-Darts-GUI
```

Run first:

```bash
python init_database.py  # to setup the database for the checkouts
```

Run second:
```bash
python darts_with_gui.py  # to start the Gui for the game 
```

Description
- On the left side you can search for a checkout (between 170 and 2) \
  The checkouts are intended for finishing the game with a double - field.

- On the top you can play Best of 7 (3,5,9,11, ...) - Legs. \
  Best of 7 legs means that whoever has 4 legs first wins the game. \
  The switch - button shows which player will start the first leg. The beginner will be switched every leg. 

- On the bottom you can play First to 3 (1,2,4,5,6 ..) - Sets. \
  First to 3 sets means that whoever has 3 sets first wins the game. \
  To achieve a set, you have to win 3 legs. \
  The switch - button has the same function here. 

![Screenshot](Images/darts-with-gui.png?raw=true)

## Setup for around-the-clock
Step into directory 
```bash
cd Python-Darts-GUI
```

Run:

```bash
python around_the_clock.py  # to start the gui for around-the-clock game
```

Description:
- First enter your name.
- Then you can use the `Switch` button to set whether you want to play on the single, double or triple fields.
- You always start with `1` and end with `20` or `Bull`.
- Use the `+` and `-` buttons to set the number of darts hit, minimum 0 and maximum 3. Use the `next` button to move to the next field.
- When you have finished, an Excel file is automatically created in which everything important is listed.

Images:
- In the directory `Images/around-the-clock` are a few more pictures, which also show the processes.

![Screenshot: around-the-clock](Images/around-the-clock/03_around_the_clock.png?raw=true)
