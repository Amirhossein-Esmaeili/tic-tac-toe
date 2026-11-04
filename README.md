# Tic Tac Toe Game | Python & Pygame

## Introduction

When launched, this project shows a simple window as a traditional two player Tic Tac Toe game built with Python and Pygame. Rather than executing inside a typical console, it gives two players some visuals of a 3×3 grid and win themselves on the same computer together.

After launching the game, the main menu provides each player with a box into which they can type their names before starting a match. During the game, the top area everything easy to read is mapped to a player turn. If it's Player X, they turn use blue to make all marks stand out while Player O marks are purple.

Codes checks at all rows, columns and diagonals if a player attempts to place a mark in an empty cell. It stops the game as soon as three identical marks sit vertically, horizontally or diagonally. If all cells get filled with no line of three, a draw pops up automatically.

In terms of architecture, all the source code is inside a single script file, named `tic-tac-toe.py`. It uses separate functions—`draw_menu`, `draw_board`, `check_win` and `check_buttons`. It also has simple UI features, such as a button hover effect, a new rounds button and a back-to-menu button.

## Features

Here are some of the things I added to the game:

- **Two-player mode:** Both players can play on the same computer without needing a second device.
- **Player names:** Each player can enter their own name before starting a game.
- **Main menu:** Players can start a new game from the menu instead of opening the board immediately.
- **3×3 game board:** A simple board with 9 cells, just like the classic Tic Tac Toe game.
- **Mouse interaction:** Players can click on empty cells to place their marks.
- **Player colors:** X and O have different colors to make them easier to recognize.
- **Turn display:** The game shows which player should make the next move.
- **Winner detection:** Checks the board after every move and finds a winner.
- **Draw detection:** The game can detect when all cells are filled without a winner.
- **Restart option:** Players can clear the board and start another round.
- **Back to menu:** After finishing a game, players can return to the main menu.
- **Button hover effects:** Buttons change color when the mouse moves over them.

## Requirements

You don't need many things to run this project. Just make sure you have:

- Python 3
- Pygame

## Installation

First, make sure Python is installed on your computer.

Pygame is used for the game window, graphics and mouse and keyboard inputs. You can install it by opening your terminal and running:

```bash
pip install pygame
```

## How to Run

Download the repository or clone it using Git.

After that, open the project folder in your terminal. You should be in the same folder as the Python file before running the command.

```bash
python tic-tac-toe.py
```

Once you run it, the game window should open and the main menu will appear.

## How to Play

You don't need to do anything complicated to start playing. When the game opens, you will see two fields where both players can enter their names.

1. Enter a name for the first player.
2. Enter a name for the second player.
3. Click on **START GAME** to open the board.
4. Player X always makes the first move.
5. Player O gets the next turn.
6. Click on any empty cell to place your mark.
7. Keep taking turns until one player wins or the game ends in a draw.
8. Use **RESTART** to clear the board and play another round.
9. After the game ends, click **BACK TO MENU** to return to the main menu.

## Controls

The game mainly uses the mouse, but there are also a few keyboard controls for entering player names.

| Key / Input | Action |
| ----------- | ----------------------------------------- |
| Mouse Click | Select cells, buttons and name fields. |
| `Tab` | Switch between the two name fields. |
| `Enter` | Move to the next field or start the game. |
| `Backspace` | Remove the last character from a name. |

## Game Rules

The game follows the usual Tic Tac Toe rules. Both players take turns and try to get three of their marks in a line.

- The board has 3 rows and 3 columns, which gives 9 cells in total.
- X always starts the game.
- Players take turns placing X and O.
- A player cannot place a mark in a cell that is already occupied.
- Getting three marks in the same row, column or diagonal means that player wins.
- If all 9 cells are filled and neither player has won, the game ends in a draw.

##  Structure

The project is written in a single Python file called `tic-tac-toe.py`. I didn't split the menu, board and other parts into different files. Instead, I used functions to handle each part separately.

There are a few main parts that work together to make the game run:

### Main Components

| Component | Description |
| ------------ | ------------------------------------------------------------ |
| Game Window | The main window where everything is displayed. It contains the menu, game board, buttons and other game information. |
| Main Menu | The first screen players see. They can enter their names and start a new game from here. |
| Game Board | The 3×3 board where both players place their marks during the game. |
| Player Names | Stores the names entered by the players and uses them when showing turns and game results. |
| Input System | Handles mouse clicks and keyboard inputs, including selecting cells and typing player names. |
| Game State | Keeps track of which screen is currently active, such as the main menu or the game itself. |
| Game Result | Handles the result after a round ends and displays the winner's name or a draw message. |
| Buttons | Used for different actions, including starting a game, restarting it and returning to the menu. |

### Main Functions

I used different functions so the code for drawing the screens and checking the game doesn't all get mixed together. These are some of the main functions:

| Function | Description |
| ---------------- | ------------------------------------------------ |
| `draw_text()` | Displays text on the game window. It is used for player names, messages and other information. |
| `draw_button()` | Draws the buttons and changes their colors when the mouse moves over them. |
| `draw_menu()` | Draws the main menu, including the name fields and the start button. |
| `draw_board()` | Displays the 3×3 board, player marks and information about the current game. |
| `check_winner()` | Checks all rows, columns and diagonals to see if a player has won. |
| `reset_game()` | Clears the board and resets the game information for another round. |

### Important Variables

These are some variables used to keep track of the players, board and current game state.

| Variable | Description |
| ---------------- | ------------------------------------------ |
| `game_state` | Stores the current screen, such as the menu or game screen. |
| `player1` | Contains the first player's name. |
| `player2` | Contains the second player's name. |
| `current_player` | Keeps track of whose turn it is. |
| `winner` | Stores the mark of the player who wins the game. |
| `game_over` | Indicates whether the current round has finished. |
| `board` | Stores the marks placed in the 9 cells. |
| `active_input` | Keeps track of which name field is currently selected. |
| `name1` | Stores the text entered in the first name field. |
| `name2` | Stores the text entered in the second name field. |

### Game Flow

This is how a normal round works, starting from opening the game and ending with a new round.

| Step | What Happens |
| -------------- | ------------------------------------------------ |
| 1. Start | Pygame opens the game window. |
| 2. Main Menu | Both players enter their names before playing. |
| 3. Start Game | The board is cleared and Player X gets the first turn. |
| 4. Player Move | The current player clicks on an empty cell to place a mark. |
| 5. Check Result | The game checks if someone has won or if the board is full. |
| 6. Next Turn | When the game is not over, the other player gets their turn. |
| 7. Game End | The winner or draw message appears on the screen. |
| 8. Restart | The board is cleared and another round can begin. |

### Screen Design

I used a dark background for the game and added some visual details to make the different screens look better. The board and buttons also have rounded corners instead of simple square shapes.

| Element | Description |
| -------------- | ------------------------------------------ |
| Window Size | 700 × 750 pixels. |
| Background | Dark background with decorative circles. |
| Main Panel | Rounded panel used in the main menu. |
| Player X | Blue color. |
| Player O | Purple color. |
| Game Board | A 3×3 board with rounded cells. |
| Buttons | Rounded buttons with hover effects. |
| Status Message | Displays the current turn or the final game result. |

## Built With

These are the main tools I used to make the project:

- **Python** – The main programming language used for the game logic and different functions.
- **Pygame** – Used to create the game window, draw the board and buttons, display text and handle player inputs.