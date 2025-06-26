# src/streaming_app/visualizer.py
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def print_summary(batch_details):
    headers = ["Batch Number","Timestamp","Words Count > 5 Letters","List of Long Words"]
    table = [[bd[h] for h in headers] for bd in batch_details]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid", showindex=False))

def plot_long_word_counts(results_data, max_y=10):
    batches = [r["batch"] for r in results_data]
    lw = [r["long_words"] for r in results_data]
    plt.figure(figsize=(8,4))
    bars = plt.bar(batches, lw, color="#1f77b4")
    plt.xlabel("Batch Number"); plt.ylabel("Long Words Count")
    plt.yticks(range(0, max(max_y, max(lw))+1))
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    for b, count in zip(batches, lw):
        plt.text(b, count+0.2, str(count), ha="center", va="bottom")
    plt.tight_layout(); plt.show()
