import subprocess
import sys

# Install Python libraries
required_packages = ["numpy", "pandas", "mlxtend", "matplotlib", "memory_profiler", "urllib3"]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} is not installed. Installing...\n\n")
        install(package)

# Import necessary libraries
import pandas as pd
import numpy as np
import time
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder
import matplotlib.pyplot as plt
from memory_profiler import memory_usage
import urllib.request
import os

# Load and prepare dataset
def load_and_prepare_data():

    # Define the absolute path for saving the file
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
    file_path = os.path.join(current_dir, "retail.dat")

    

    # Download the retail dataset
    url = "http://fimi.uantwerpen.be/data/retail.dat"
    # file_path = "retail.dat"
    urllib.request.urlretrieve(url, file_path)

    # Read the dataset and prepare transactions
    with open(file_path, "r") as f:
        dataset = [line.strip().split() for line in f.readlines()]

    # Convert transactions to one-hot encoded format
    te = TransactionEncoder()
    te_data = te.fit(dataset).transform(dataset)
    data = pd.DataFrame(te_data, columns=te.columns_)
    return data

# Apriori Algorithm Implementation
def run_apriori(data, min_support):
    start_time = time.time()
    start_mem = memory_usage()[0]
    frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0, num_itemsets=len(frequent_itemsets))
    end_time = time.time()
    end_mem = memory_usage()[0]
    memory_used = end_mem - start_mem
    return frequent_itemsets, rules, end_time - start_time, memory_used

# FP-Growth Algorithm Implementation
def run_fpgrowth(data, min_support):
    start_time = time.time()
    start_mem = memory_usage()[0]
    frequent_itemsets = fpgrowth(data, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0, num_itemsets=len(frequent_itemsets))
    end_time = time.time()
    end_mem = memory_usage()[0]
    memory_used = end_mem - start_mem
    return frequent_itemsets, rules, end_time - start_time, memory_used

# Eclat Algorithm Implementation
def eclat(data, min_support):
    vertical_data = {item: set(data.index[data[item]]) for item in data.columns}
    frequent_itemsets = {}

    def explore(items, prefix=[]):
        for item, tids in items.items():
            if len(tids) >= min_support:
                new_prefix = prefix + [item]
                frequent_itemsets[tuple(new_prefix)] = len(tids)
                new_items = {key: tids.intersection(value) for key, value in items.items() if key != item}
                explore(new_items, new_prefix)

    start_time = time.time()
    start_mem = memory_usage()[0]
    explore(vertical_data)
    end_time = time.time()
    end_mem = memory_usage()[0]
    memory_used = end_mem - start_mem
    return frequent_itemsets, end_time - start_time, memory_used

# Compare Algorithm Performance
def compare_algorithms(data, min_supports):
    results = []

    for min_support in min_supports:
        print(f"\nEvaluating for min_support = {min_support}")

        apriori_results, apriori_rules, apriori_time, apriori_mem = run_apriori(data, min_support)
        print(f"Apriori: Found {len(apriori_results)} itemsets in {apriori_time:.4f} seconds, Memory Used: {apriori_mem:.2f} MB")

        fpgrowth_results, fpgrowth_rules, fpgrowth_time, fpgrowth_mem = run_fpgrowth(data, min_support)
        print(f"FP-Growth: Found {len(fpgrowth_results)} itemsets in {fpgrowth_time:.4f} seconds, Memory Used: {fpgrowth_mem:.2f} MB")

        eclat_results, eclat_time, eclat_mem = eclat(data, int(min_support * len(data)))
        print(f"Eclat: Found {len(eclat_results)} itemsets in {eclat_time:.4f} seconds, Memory Used: {eclat_mem:.2f} MB")

        results.append({
            "min_support": min_support,
            "apriori_time": apriori_time,
            "fpgrowth_time": fpgrowth_time,
            "eclat_time": eclat_time,
            "apriori_mem": apriori_mem,
            "fpgrowth_mem": fpgrowth_mem,
            "eclat_mem": eclat_mem
        })

    return pd.DataFrame(results)

# Plot the comparison results
def plot_results(results):
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.set_xlabel("Minimum Support")
    ax1.set_ylabel("Execution Time (seconds)", color="tab:blue")
    ax1.plot(results["min_support"], results["apriori_time"], label="Apriori Time", marker='o', color="tab:blue")
    ax1.plot(results["min_support"], results["fpgrowth_time"], label="FP-Growth Time", marker='x', color="tab:cyan")
    ax1.plot(results["min_support"], results["eclat_time"], label="Eclat Time", marker='s', color="tab:purple")
    ax1.tick_params(axis='y', labelcolor="tab:blue")
    ax1.legend(loc="upper left")

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel("Memory Usage (MB)", color="tab:red")
    ax2.plot(results["min_support"], results["apriori_mem"], label="Apriori Memory", marker='o', linestyle="--", color="tab:red")
    ax2.plot(results["min_support"], results["fpgrowth_mem"], label="FP-Growth Memory", marker='x', linestyle="--", color="tab:orange")
    ax2.plot(results["min_support"], results["eclat_mem"], label="Eclat Memory", marker='s', linestyle="--", color="tab:pink")
    ax2.tick_params(axis='y', labelcolor="tab:red")
    ax2.legend(loc="upper right")

    plt.title("Algorithm Performance Comparison: Time vs Memory")
    fig.tight_layout()  # to prevent overlapping of labels
    plt.grid()
    plt.show()

# Main execution
if __name__ == "__main__":
    data = load_and_prepare_data()
    min_supports = [0.1, 0.2, 0.3, 0.4]  # Example minimum support values
    results = compare_algorithms(data, min_supports)
    print("\nPerformance Comparison:")
    print(results)
    plot_results(results)
