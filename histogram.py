# histogram.py

import sys

def read_input():
    data = []
    for line in sys.stdin:
        label, count = line.strip().split()
        data.append((label, int(count)))
    return data

def generate_histogram(data):
    total_count = sum(count for _, count in data)
    for label, count in data:
        percentage = (count / total_count) * 100
        bar = '#' * int((percentage / 2))  # Scale down the bar for a better display
        print(f"{label.ljust(10)} | {bar} {percentage:.2f}%")

if __name__ == "__main__":
    data = read_input()
    generate_histogram(data)
