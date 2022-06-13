# cycle

Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them. You play this game
on a simulated terminal, with a textual interface.

## Getting Started

---

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cycle

```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```

root (project root folder)
+-- cycle (source code for game)
+-- game (specific game classes)
+-- **main**.py (entry point for program)
+-- README.md (general info)

```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
Kyle Coulon (kylejcoulon@gmail.com)
* TODO: Add your name and email here



```

MAIN CLASS

- create two snakes

CONTROL ACTORS ACTIONS CLASS

- use cast groups to make sure keyboard controls apply to each ("snake 1" vs "snake 2")

SNAKE CLASS:

- using "\_player" variable inside snake class make sure they start at correct positions in \_prepare_body method

GROWTH (child of Action) - CLASS TO INSCREASE SIZE OF SNAKES

- created in Main class
- needs access to Cast so that it can access snake1 and 2 in order to call their grow_tail() method
- execute method () add that to do updates script
- in execute method, somehow use timer variable (for instance multiplies seconds by frame rate constant) to count certain number of frames that calls grow tail on snakes

HANDLE COLLISIONS CLASS:

- using cast group name "snake 1" vs "snake 2", check each segment against each other to find collision, if true call game_over()
- game over() needs to turn both snakes white, display game over message
- if we want self collision, make method that checks each snake against its own segments

ALL OTHER CLASSES SHOULD BE SIMILAR TO THE PREPARE GAME SOURCE
