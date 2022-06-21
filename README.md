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

DESIGN DOCUMENT:

# Peter

MAIN CLASS

- create two instances of Snake class in main

SNAKE CLASS:

- add "player" variable inside snake, and initialize it when creating the class to be either "first" or "second"
- make sure snakes start at correct positions in prepare_body method
- color both snakes differently

# Rachel

Create a class to increase the size of snakes

HandleGrowthAction (child of Action)

- create an instance in Main class and add it to the do-updates script list
- needs access to Cast so that it can access Snakes in order to call their grow_tail() method
- override execute method
- in execute method, use a timer variable (for instance multiplies seconds by frame rate constant) to count certain number of frames
- then calls grow_tail on snakes and resets timer

# Kyle

CONTROL ACTORS ACTIONS CLASS

- use cast groups to make sure keyboard controls apply to each snake
- create get_player() accessor method for snakes so we can retreive whether they are "first" or "second" player

HANDLE COLLISIONS CLASS:

- using get_actors("snakes") and for-each loop, perform self-collision check on both snakes > if true call game_over()
- using get_actors("snakes") and nested for-each loops, perform this.head vs other.segments check on both snakes > if true call game_over()
- create self.\_who_won variable inside HandleCollisionsAction to be set when a player wins
- game over() needs to turn both snakes white, display game over message
- display who won (use snake color to distinguish)

GAME RESTART

- inside HandleCollisionsAction, display an option to "Play again? (y)"
- must pass in keyboard service to HandleCollisionsAction
- must add press "y" key to keyboard service
- if player chooses y, call a method on both instances of Snake that resets their positions and colors
- set game over variable to false
- destroy Actors that display game over messages

# Alex

SCORES(child of Actor)

- child of actor, only difference is it keeps track of a score number variable
- create two instances of Scores class at the beginning of the game
- update each score when a player wins (HandleCollisionsAction class)

ALL OTHER CLASSES SHOULD BE SIMILAR TO THE PREPARE GAME SOURCE
