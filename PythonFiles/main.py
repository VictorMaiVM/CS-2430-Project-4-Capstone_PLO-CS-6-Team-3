#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 4

import os
import csv
from engine import MonopolySimulation


# Runs 10 independent simulations for each jail-exit strategy for each n turns.
def run_batch_experiments():
    n_turns = [1000, 10000, 100000, 1000000]
    strategies = ["A", "B"]

    os.makedirs("output_data", exist_ok=True)

    for strategy in strategies:
        print(f"\n--- Running Strategy {strategy} ---")
        sim = MonopolySimulation(jail_strategy=strategy)

        for n in n_turns:
            print(f"Simulating n = {n:,} turns...")
            for run_idx in range(1, 11):
                sim.reset_simulation()
                sim.run_simulation(n)

                filename = f"output_data/strategy_{strategy}_n_{n}_run_{run_idx}.csv"
                with open(filename, mode="w", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Index", "SquareName", "LandingCount", "Percentage"])
                    for sq in sim.board:
                        pct = (sq.landing_count / n) * 100
                        writer.writerow([sq.index, sq.name, sq.landing_count, pct])

    print("\nAll 80 simulation datasets successfully generated and saved to /output_data/")

if __name__ == "__main__":
    run_batch_experiments()