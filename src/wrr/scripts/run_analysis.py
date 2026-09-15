"""Placeholder analysis pipeline: replace each step with your own project logic.

The example computes a normal depth, writes it to a CSV, and saves a
longitudinal profile figure - so you can see where results and figures
are supposed to end up.
"""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # write figures to files; works without a display (e.g. on a server/CI)
import matplotlib.pyplot as plt
import numpy as np

from wrr.standard_step import normal_depth_rectangular

RESULTS_DIR = Path("results")
FIGURES_DIR = Path("figures")


def main():
    print("This is a placeholder analysis. Replace it with your pipeline steps.")

    # Example channel: discharge, width, Manning's n, bed slope
    Q, b, n, S0 = 25.0, 5.0, 0.035, 0.001
    yn = normal_depth_rectangular(Q, b, n, S0)
    print(f"Normal depth: yn = {yn:.3f} m")

    # Write a small results table
    RESULTS_DIR.mkdir(exist_ok=True)
    with open(RESULTS_DIR / "normal_depth.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Q_m3s", "b_m", "n", "S0", "yn_m"])
        writer.writerow([Q, b, n, S0, yn])

    # Plot bed and water surface elevation along a 500 m reach
    x = np.linspace(0, 500, 51)
    bed = 100.0 - S0 * x
    wse = bed + yn

    FIGURES_DIR.mkdir(exist_ok=True)
    plt.figure()
    plt.plot(x, bed, label="Bed")
    plt.plot(x, wse, label="Water surface")
    plt.xlabel("x [m]")
    plt.ylabel("Elevation [m]")
    plt.legend()
    plt.savefig(FIGURES_DIR / "profile.png", dpi=150)
    print(f"Wrote {RESULTS_DIR / 'normal_depth.csv'} and {FIGURES_DIR / 'profile.png'}")


if __name__ == "__main__":
    main()
