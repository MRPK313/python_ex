
import subprocess
import sys

# install python libraries
required_packages = ["numpy","pandas","mlxtend","matplotlib"]

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

# Load dataset and prepare it for processing
def load_and_prepare_data():
    # Example dataset (Groceries dataset or user-provided data can be replaced here)
    dataset = [
        ['milk', 'bread', 'butter'],
        ['bread', 'butter', 'beer'],
        ['milk', 'bread', 'butter', 'beer'],
        ['milk', 'bread'],
        ['butter', 'beer']
    ]

    # Convert transactions to one-hot encoded format
    te = TransactionEncoder()
    te_data = te.fit(dataset).transform(dataset)
    data = pd.DataFrame(te_data, columns=te.columns_)
    return data

# Apriori Algorithm Implementation
def run_apriori(data, min_support):
    start_time = time.time()
    frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0, num_itemsets=len(frequent_itemsets))
    end_time = time.time()
    return frequent_itemsets, rules, end_time - start_time

# FP-Growth Algorithm Implementation
def run_fpgrowth(data, min_support):
    start_time = time.time()
    frequent_itemsets = fpgrowth(data, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0, num_itemsets=len(frequent_itemsets))
    end_time = time.time()
    return frequent_itemsets, rules, end_time - start_time

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
    explore(vertical_data)
    end_time = time.time()
    return frequent_itemsets, end_time - start_time

# Compare Algorithm Performance
def compare_algorithms(data, min_supports):
    results = []

    for min_support in min_supports:
        print(f"\nEvaluating for min_support = {min_support}")
        
        apriori_results, apriori_rules, apriori_time = run_apriori(data, min_support)
        print(f"Apriori: Found {len(apriori_results)} itemsets in {apriori_time:.4f} seconds")

        fpgrowth_results, fpgrowth_rules, fpgrowth_time = run_fpgrowth(data, min_support)
        print(f"FP-Growth: Found {len(fpgrowth_results)} itemsets in {fpgrowth_time:.4f} seconds")

        eclat_results, eclat_time = eclat(data, int(min_support * len(data)))
        print(f"Eclat: Found {len(eclat_results)} itemsets in {eclat_time:.4f} seconds")

        results.append({
            "min_support": min_support,
            "apriori_time": apriori_time,
            "fpgrowth_time": fpgrowth_time,
            "eclat_time": eclat_time
        })

    return pd.DataFrame(results)

# Plot the comparison results
def plot_results(results):
    plt.plot(results["min_support"], results["apriori_time"], label="Apriori", marker='o')
    plt.plot(results["min_support"], results["fpgrowth_time"], label="FP-Growth", marker='x')
    plt.plot(results["min_support"], results["eclat_time"], label="Eclat", marker='s')
    plt.xlabel("Minimum Support")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Algorithm Performance Comparison")
    plt.legend()
    plt.grid()
    plt.show()

# Main execution
if __name__ == "__main__":
    data = load_and_prepare_data()
    min_supports = [0.2, 0.4, 0.6, 0.8]  # Example minimum support values
    results = compare_algorithms(data, min_supports)
    print("\nPerformance Comparison:")
    print(results)
    plot_results(results)
