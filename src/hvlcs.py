from itertools import islice
import sys


# Usage: python hvlcs.py <input-file>
def main():
    if len(sys.argv) != 2:
        print("Usage: python hvlcs.py <input-file>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        n = int(file.readline().strip())

        # character values dict
        values = {
            line.split()[0]: line.split()[1]
            for line in islice(file, n)
        }

        # input strings
        A = file.readline().strip()
        B = file.readline().strip()

    # TODO: call hvlcs()

    # TODO: call backtrack()

    # TODO: file write

if __name__ == "__main__":
    main()
    sys.exit(0)
