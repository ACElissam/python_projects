"""
Configuration module for the slot machine game.

This module contains all the configurable constants and parameters
used throughout the slot machine game, including betting limits,
machine dimensions, symbol distributions, and payout values.
"""

# =============================================================================
# GAME BETTING LIMITS
# =============================================================================

MAX_LINES = 3
"""int: Maximum number of lines a player can bet on.
This determines the maximum number of horizontal rows that can be selected
for betting in a single spin. With 3 lines, players can bet on:
- Line 1: Top row
- Line 2: Middle row  
- Line 3: Bottom row
"""

MAX_BET = 100
"""int: Maximum bet amount per line in dollars.
This is the highest amount a player can wager on each individual line.
The total bet for a spin equals (bet_per_line × number_of_lines).
Example: $100 per line × 3 lines = $300 maximum total bet.
"""

MIN_BET = 1
"""int: Minimum bet amount per line in dollars.
This is the smallest amount a player can wager on each line.
Setting this to 1 ensures players can afford to play with small budgets.
Example: $1 per line × 1 line = $1 minimum total bet.
"""

# =============================================================================
# SLOT MACHINE DIMENSIONS
# =============================================================================

ROWS = 3
"""int: Number of horizontal rows in the slot machine grid.
This defines the height of the slot machine display. Each row can contain
winning combinations when all symbols in that row match across all columns.
Standard slot machines typically use 3 rows for classic gameplay.
"""

COLS = 3
"""int: Number of vertical columns (reels) in the slot machine.
This defines the width of the slot machine display. Each column represents
a spinning reel that stops to show one symbol per row. Three columns create
a 3×3 grid which is the classic slot machine format.
"""

# =============================================================================
# SYMBOL CONFIGURATION
# =============================================================================

SYMBOLS_COUNT = {"A": 2, "B": 4, "C": 6, "D": 8}
"""dict[str, int]: Distribution of symbols in the symbol pool.

This dictionary defines how many times each symbol appears in the pool
of available symbols for random selection. The total pool size is 20 symbols:
- "A": 2 occurrences (10% probability) - Rarest, highest value
- "B": 4 occurrences (20% probability) - Uncommon, high value
- "C": 6 occurrences (30% probability) - Common, medium value  
- "D": 8 occurrences (40% probability) - Most common, lowest value

Lower frequency = rarer symbol = higher payout value.
The game randomly selects from this pool without replacement for each spin.
"""

SYMBOL_VALUES = {"A": 5, "B": 4, "C": 3, "D": 2}
"""dict[str, int]: Payout multiplier for each winning symbol.

This dictionary defines how much each symbol pays when forming a winning line.
The payout calculation is: symbol_value × bet_per_line = total_winnings

Payout structure (inverse relationship with frequency):
- "A": 5x multiplier - Highest payout for rarest symbol
- "B": 4x multiplier - High payout for uncommon symbol
- "C": 3x multiplier - Medium payout for common symbol
- "D": 2x multiplier - Lowest payout for most common symbol

Example: 3 "A" symbols on a line with $10 bet = 5 × $10 = $50 winnings
"""
