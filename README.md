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
  
## Setup for normal dartboard
  
Step into directory 
```bash
cd Python-Darts-GUI
```

Run:

```bash
python zähler.py  # to start the gui for counting
```

Description
- First, enter your names in the text fields on the top right-hand side. By pressing the Buttons `P1`, `P2`, `P3` and `P4` the names appear on the left side. \
  If there are only two of you, simply leave the third and fourth fields empty.
- Then set whether you want to play 501 or 301.
- After that press `Start`.
- Now you can type in what you have thrown and press respectively `Add`. After 3 entries press `Count Down` to count down your thrown number of points from your stand.
- The next player will be chosen automatically.
- If you throw more, e.g. 60, but you only have 50 left, a message appears that you have overthrown and it is the next players turn.
- If the first player has 0 points left, a new game will be started automatically. If there are three or four players, the game will continue until there is only one player left
- When you have finished playing, you can press `Calculate Score`, which will create an Excel file where you can view your average and various statistics.

![Screenshot](Images/zähler.png?raw=true)

## Setup for around-the-clock
Step into directory 
```bash
cd Python-Darts-GUI
```

Run:

```bash
python around_the_clock.py  # to start the gui for counting
```

Description:
- You can use the `Switch` button to set whether you want to play on the single, double or triple fields.
- You always start with `1` and end with `20` or `Bull`.
- Use the `+` and `-` buttons to set the number of darts hit, minimum 0 and maximum 3. Use the `next` button to move to the next field.
- When you have finished, an excel file is automatically created in which everything important is listed.

![Screenshot: around-the-clock](Images/around-the-clock.png?raw=true)
