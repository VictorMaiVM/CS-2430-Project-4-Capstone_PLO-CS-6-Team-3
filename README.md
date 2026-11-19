# CS-2430-Project-4-Capstone_PLO-CS-6-Team-3

# Monopoly Movement Simulation (rough draft, will be edited throughout project)

**Team:** Team 3
**Members:** Dominique Frank, Victor Mai, Erich Mundt
**Course:** CS 2430, section 502
**Project:** Programming Project 4 (Capstone) - Fall 2026

## What This Project Does

This program simulates a single player moving around a standard Monopoly board (2018 U.S. rules). It does not model money, property purchases, or other players. It only tracks movement: dice rolls, doubles, Chance and Community Chest cards that move the player, and Jail.

The goal is to answer two questions using large numbers of simulated turns:

1. Which squares are landed on most often?
2. Does the "get out of jail" strategy change those probabilities?

The program runs two jail strategies:

- **Strategy A (Immediate Exit):** Use a Get Out of Jail Free card if held. Otherwise pay $50 and leave Jail on the next turn.
- **Strategy B (Try for Doubles):** Use a Get Out of Jail Free card if held. Otherwise try to roll doubles for up to 3 turns, then pay $50 and leave on the 4th turn.

For each strategy it runs 10 independent simulations at n = 1,000, 10,000, 100,000, and 1,000,000 turns, producing 80 datasets in total.

## Requirements

- Python 3.14
- No third-party libraries. The program uses only the Python standard library (random, csv, os).
- (Extra credit only, if used) matplotlib for the bar chart: pip install matplotlib

## Files

| File               | Purpose                                                      |
| ------------------ | ------------------------------------------------------------ |
| `main.py`          | Entry point; runs all experiments and writes output files.   |
| `engine.py`        | Simulation engine: dice, turns, movement, cards, Jail rules. |
| `board.py`         | Board squares, square types, and landing counts.             |
| `deck.py`          | Chance and Community Chest decks with discard and reshuffle. |
| `player.py`        | Player state: position, jail status, doubles, jail cards.    |
| `output_data/`     | Generated CSV files (created when the program runs).         |
| `docs/`            | Project Plan, design artifacts, and test plan.               |
| `CONTRIBUTIONS.md` | Who did what, with evidence pointers.                        |

## How to Run

1. Put all .py files in the same folder.
2. Open a terminal in that folder.
3. Run:

   ```
   python main.py
   ```

   (On some systems use python3 main.py.)

4. The program prints progress for each strategy and each value of n. When finished, it prints a confirmation message.

**Expected run time:** about ___ minutes (fill in after a full run). The n = 1,000,000 runs take the longest.

## Output

All results are saved in the output_data/ folder (created automatically). There is one CSV file per dataset, named:

```
strategy_<A or B>_n_<n>_run_<1-10>.csv
```

For example, strategy_A_n_1000000_run_3.csv is run 3 of Strategy A at 1,000,000 turns.

Each CSV has one row per square (40 rows) and these columns:

| Column         | Meaning                                              |
| -------------- | ---------------------------------------------------- |
| `Index`        | Square number, 0 (GO) to 39 (Boardwalk)             |
| `SquareName`   | Name of the square                                   |
| `LandingCount` | Number of times the simulation landed on that square |
| `Percentage`   | `LandingCount / n * 100`                             |

The comparative run summary (top squares per strategy, Strategy A vs. B at n = 1,000,000, and anomalies) is saved to: ___ (fill in the file name and location).

## Modeling Decisions

These are the choices our team made where the rules or assignment leave room for interpretation.

- **What counts as a landing:** ___ (for example: one landing is counted per turn, on the square where the player ends the turn, after all movement effects are resolved)
- **Go to Jail square (30):** never receives a count. The player ends in Jail (square 10), and that square is counted.
- **Turns spent sitting in Jail:** ___ (counted / not counted)
- **Doubles:** a double gives the player another roll in the same turn. The third consecutive double in one turn sends the player to Jail without moving.
- **Get Out of Jail Free cards:** removed from the deck while held, and returned to the bottom of their deck when used.
- **Batch runs:** ___ (for example: each value of n is its own independent run, or the four results are snapshots of one longer run)
- **Random numbers:** Python's built-in random module. ___ (state whether a seed is used)

## Testing

Test cases and expected results are listed in docs/ (test plan). To run the tests: ___ (add the command once tests exist).

## Sources

- Hasbro Monopoly rules (2018 U.S. edition)
- Monopoly board reference image provided with the assignment
- Chance and Community Chest card list provided with the assignment
- ___ (add any published probability distribution used for cross-validation)
