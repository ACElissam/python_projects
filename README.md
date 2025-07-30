# 🎰 Python Slot Machine

An interactive slot machine game developed in Python with a betting system, winnings calculation, and balance management.

## 📋 Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Game Rules](#game-rules)
- [Examples](#examples)
- [Contributing](#contributing)

## 📖 Description

This application simulates a classic slot machine where players can:
- Deposit money
- Bet on 1 to 3 lines
- Spin the reels
- Win money based on symbol combinations
- Manage their balance throughout the game

The game uses a symbol system with different values and appearance probabilities, creating a balanced and entertaining gaming experience.

## ✨ Features

### 🎮 Gameplay
- **Initial deposit**: Players start by depositing money
- **Flexible betting**: Ability to bet on 1, 2, or 3 lines
- **Variable amounts**: Bets from $1 to $100 per line
- **Balance validation**: Automatic verification of available funds
- **Winnings calculation**: Automatic system for calculating winnings

### 🎯 Game Mechanics
- **3x3 grid**: Slot machine with 3 reels and 3 rows
- **4 different symbols**: A, B, C, D with distinct values
- **Winning lines**: Up to 3 horizontal paying lines
- **Visual display**: Clear representation of results

### 💰 Financial Management
- **Balance tracking**: Real-time updates
- **Winnings history**: Display of winning and losing lines
- **Player protection**: Automatic stop if balance reaches zero

## 🚀 Installation

### Prerequisites
- Python 3.6 or newer
- No external dependencies required (uses only standard modules)

### Installation
1. Clone or download the project:
```bash
git clone [repo-url]
cd slot_mach
```

2. Verify Python is installed:
```bash
python --version
```

3. Launch the game:
```bash
python main.py
```

## 🎯 Usage

### Launching the Game
```bash
python main.py
```

### Game Steps
1. **Initial deposit**: Enter the amount you want to deposit
2. **Line selection**: Choose how many lines to bet on (1-3)
3. **Bet amount**: Set your wager per line ($1-$100)
4. **Spin**: Press Enter to spin the reels
5. **Results**: Check your winnings and new balance
6. **Continue**: Keep playing or quit with 'q'

### Commands
- **Enter**: Spin the reels
- **'q'**: Quit the game
- **Numbers**: Enter amounts and choices

## ⚙️ Configuration

The `config.py` file contains all configurable parameters:

### Game Limits
```python
MAX_LINES = 3      # Maximum number of lines
MAX_BET = 100      # Maximum bet per line
MIN_BET = 1        # Minimum bet per line
```

### Machine Dimensions
```python
ROWS = 3           # Number of rows
COLS = 3           # Number of columns
```

### Symbol Configuration
```python
SYMBOLS_COUNT = {
    "A": 2,        # Rare symbol (2 occurrences)
    "B": 4,        # Uncommon symbol (4 occurrences)
    "C": 6,        # Common symbol (6 occurrences)
    "D": 8         # Very common symbol (8 occurrences)
}

SYMBOL_VALUES = {
    "A": 5,        # Highest value
    "B": 4,        # High value
    "C": 3,        # Medium value
    "D": 2         # Lowest value
}
```

## 📁 Project Structure

```
slot_mach/
│
├── main.py           # Main file with game logic
├── config.py         # Configuration and constants
├── README.md         # Project documentation
└── __pycache__/      # Compiled Python files
    └── config.cpython-313.pyc
```

### Main Files

#### `main.py`
Contains all main functions:
- `main()`: Main function that manages game flow
- `deposit()`: Initial deposit management
- `get_number_of_lines()`: Line number selection
- `get_bet()`: Bet amount definition
- `spin()`: Complete round execution
- `get_slot_machine_spin()`: Random results generation
- `print_slot_machine()`: Visual display of results
- `check_winnings()`: Winnings calculation

#### `config.py`
Centralized configuration file containing:
- Betting and line limits
- Slot machine dimensions
- Symbol distribution and values

## 🎲 Game Rules

### Basic Principle
- The slot machine has a 3x3 grid (3 columns, 3 rows)
- Players can bet on 1, 2, or 3 horizontal lines
- To win, all symbols in a line must be identical

### Symbol System
| Symbol | Frequency | Value | Probability |
|---------|-----------|--------|-------------|
| A       | 2/20      | 5x     | 10% (Rare) |
| B       | 4/20      | 4x     | 20% (Uncommon) |
| C       | 6/20      | 3x     | 30% (Common) |
| D       | 8/20      | 2x     | 40% (Very common) |

### Winnings Calculation
**Winnings = Symbol value × Bet per line**

Examples:
- Line with 3 "A" and $10 bet = 5 × $10 = $50
- Line with 3 "D" and $5 bet = 2 × $5 = $10

### Winning Lines
```
Line 1: [0,0] [1,0] [2,0]
Line 2: [0,1] [1,1] [2,1]
Line 3: [0,2] [1,2] [2,2]
```

## 💡 Examples

### Example Game Session
```
Enter the amount to deposit: $100
You have successfully deposited $100.

Your current balance is $100.
Press Enter to spin or 'q' to quit: 

Enter the number of lines to bet on (1-3): 2
You have chosen to bet on 2 lines.

Enter your bet amount ($1-$100): 10
You have placed a bet of $10.

You are betting $20 on 2 lines. Your total bet is currently equal to $20.

A  |  B  |  C
A  |  A  |  A
D  |  C  |  B

You won $50
You won on lines 2

Your current balance is $130.
```

### Losing Result
```
D  |  A  |  C
B  |  D  |  A
C  |  B  |  D

You won $0
You lost with lines 1, 2

Your current balance is $80.
```

## 🔧 Customization

### Modifying Probabilities
To adjust difficulty, modify `SYMBOLS_COUNT` in `config.py`:
```python
# Easier game (more valuable symbols)
SYMBOLS_COUNT = {"A": 4, "B": 6, "C": 6, "D": 4}

# Harder game (fewer valuable symbols)
SYMBOLS_COUNT = {"A": 1, "B": 2, "C": 5, "D": 12}
```

### Modifying Winnings
Adjust `SYMBOL_VALUES` to change rewards:
```python
# Higher winnings
SYMBOL_VALUES = {"A": 10, "B": 7, "C": 5, "D": 3}
```

### Modifying Limits
Change betting limits in `config.py`:
```python
MAX_BET = 500      # Higher maximum bet
MIN_BET = 5        # Higher minimum bet
MAX_LINES = 5      # More lines (requires code modification)
```

## 🛠️ Technical Functions

### Random Generation
The game uses `random.choice()` to select symbols without replacement, ensuring no symbol appears more often than its configured frequency in a single spin.

### Input Validation
All user inputs are validated:
- Verification that amounts are numeric
- Control of betting limits
- Validation of available balance

### Error Handling
The game includes robust error handling:
- Non-numeric inputs
- Out-of-range amounts
- Insufficient balance

## 🤝 Contributing

To contribute to the project:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

### Possible Improvements
- Graphical interface (Tkinter, Pygame)
- Score saving
- Jackpot system
- Visual animations
- Sounds and effects
- Game statistics
- Multiple game modes

## 📜 License

This project is free to use for educational and personal purposes.

---

**Have fun and play responsibly! 🎰**
