Hunt the Wumpus

Python • Object-Oriented Programming

Overview

This project is a text-based implementation of the classic Hunt the Wumpus game, developed in Python using Object-Oriented Programming (OOP) principles.

The player explores a cave made up of connected rooms while trying to hunt and eliminate the Wumpus. Along the way, the player must avoid dangerous hazards such as bottomless pits and giant bats. The game ends when the player either defeats the Wumpus or encounters a fatal hazard.

This project demonstrates strong use of OOP concepts including encapsulation, abstraction, and modular class design.

Learning Objectives

This project was built to:

Practice Object-Oriented Programming in Python

Design clean class structures

Manage game state using objects

Implement logical decision-making systems

Handle user input and validation

Apply modular and reusable code design

Game Rules
Goal

Kill the Wumpus before it kills you.

Player Actions

On each turn, the player can:

Move to a connected room

Shoot an arrow into a connected room

Quit the game

Hazards

The cave contains the following dangers:

Wumpus

Entering the Wumpus’s room results in immediate death.

Shooting the Wumpus results in victory.

Bottomless Pits

Entering a pit causes instant death.

Super Bats

If you enter a room with bats, they carry you to a random room.

Warning Messages

The game provides clues when you are near danger:

Near Wumpus → “You smell something terrible.”

Near Pit → “You feel a cold breeze.”

Near Bats → “You hear flapping.”

These warnings help the player make strategic decisions.

Arrows

The player has a limited number of arrows.

Missing a shot reduces the arrow count.

If arrows run out before killing the Wumpus, the player loses.

How to Run the Game
Requirements

Python 3.x

No external libraries required

Run Instructions

From the project directory, run:

python main.py

If your entry file is different, replace main.py with your file name.

Project Structure (Example)
.
├── main.py
├── game.py
├── player.py
├── cave.py
├── room.py
├── hazards.py
└── README.md

File descriptions:

main.py → Entry point of the program

game.py → Controls game loop and win/lose logic

player.py → Manages player state (room, arrows, status)

cave.py → Creates and connects rooms

room.py → Represents individual rooms

hazards.py → Contains Wumpus, Pit, and Bat logic

Object-Oriented Design

The game is built around the following OOP principles:

Encapsulation

Each class controls its own data and behavior.
For example, the Player class manages arrows and movement logic internally.

Abstraction

The game loop interacts with high-level methods like:

move()

shoot()

check_status()

This keeps the main program clean and readable.

Modularity

Each component (Player, Cave, Hazards) is separated into different classes to improve clarity and maintainability.

Example Gameplay Flow

Player starts in a random room.

The game displays connected rooms and possible warnings.

Player chooses to move or shoot.

Game checks for hazards.

Repeat until win or lose condition is triggered.

Possible Extensions

Future improvements could include:

Difficulty levels

Graphical interface (GUI)

Arrow paths through multiple rooms

Score tracking

Unit testing

Save/load functionality

Author

Developed as a Python OOP project to demonstrate structured game design and object-oriented programming concepts.

License

This project is for educational purposes.
You may modify and extend it for learning and experimentation.
