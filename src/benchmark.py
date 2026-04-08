import time
import sys
import matplotlib.pyplot as plt
from hvlcs import hvlcs, parse


NUM_TRIALS = 10000

def main():
    in_files = [f"test{i}.in" for i in range(1, 11)]

    avg_times = []
    for in_file in in_files:
        values, a, b = parse(in_file)

        total = 0
        for _ in range(NUM_TRIALS):
            start = time.perf_counter()
            hvlcs(a, b, values)
            stop = time.perf_counter()
            total += stop - start

        avg_times.append(total / NUM_TRIALS)

    plt.plot(avg_times, color="skyblue")
    plt.axhline(sum(avg_times)/len(avg_times), color='lightgray')

    plt.xlabel("Input file")
    plt.ylabel("Elapsed time (s)")
    plt.title("Average Runtime Across 10 Input Files")
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
