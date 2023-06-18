# Street Fighter Game Documentation

**Street Fighter** is a 2D fighting game that allows two players to control individual fighters on the screen. The objective is to deplete the opponent's health bar. Each fighter has unique attack styles and animations.

## Code Overview

The code base for the game consists of two Python files:

1. `fighter.py` - Defines the `Fighter` class, which represents a game character. This class includes methods to handle character animation, movement, attacks, health, and more.

2. `main.py` - The main game loop is located in this file. It is responsible for handling game initialization, rendering the graphics, playing sounds, controlling the game states, and managing game rounds.

## Game Initialization

The game is initialized using the Pygame library. The game window is set to 1000x600 pixels. The frame rate is set to 60 frames per second. Game variables, fighter variables, sounds, images, and fonts are all loaded at the start.

## Requirements

To run this game, you need Python 3 and Pygame installed on your system.

## How to Run the Game

To run the game, navigate to the directory containing the `main.py` script and run the following command:

**python3 main.py** or **python main.py**

## Game Mechanics

The game consists of rounds where two players battle each other. At the start of each round, there's a 3-second countdown before the fight begins.

The fighters can perform several actions:

- Running: by pressing `A` or `D` for Player 1, and `Left arrow key` or `Right arrow key` for Player 2.
- Jumping: by pressing `W` for Player 1, and `Up arrow key` for Player 2.
- Attacking: by pressing `R` or `T` for Player 1, and `K` or `L` for Player 2.

When a fighter's health reaches zero, the round ends, the opponent scores a point, and a new round begins after a cooldown period.

## Controls

Player 1:

- `A` : Move left
- `D` : Move right
- `W` : Jump
- `R` / `T` : Attack

Player 2:

- `Left Arrow Key` : Move left
- `Right Arrow Key` : Move right
- `Up Arrow Key` : Jump
- `K` / `L` : Attack

## Game Loop

The game loop is the heart of the game. It controls the game flow, handles user input, updates the game state, renders the graphics, and checks for game over conditions.

## Game Exit

The game can be exited at any time by closing the game window.

## Assets

This game uses various assets which are stored in the 'assets' directory. This includes the following:

- `audio`: Contains audio files for game music and sound effects.
- `fonts`: Contains font files used in the game.
- `images`: Contains sprite sheets for fighters, background images, and victory icon.

## Enjoy the game!

That's it! Engage in a thrilling battle with the Street Fighter game. Test your reflexes, outwit your opponent, and see who can dominate the arena! Enjoy playing and may the best fighter win!
