from itertools import islice
import sys


# computes a table of optimal values
def hvlcs(a, b, values):
    m = len(a)
    n = len(b)

    # initialize 0th row and 0th col to all 0s
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                # add value if matching
                table[i][j] = max(values[a[i - 1]] + table[i - 1][j - 1], table[i - 1][j], table[i][j - 1])
            else:
                # o.w. recurse
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table, table[m][n]

# compute the subsequence of max value
def backtrack(table, a, b, values):
    m = len(table) - 1
    n = len(table[0]) - 1
    res = []

    i, j = m, n
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and table[i][j] == values[a[i - 1]] + table[i - 1][j - 1]:
            res.append(a[i - 1])
            i -= 1
            j -= 1
        elif table[i][j] == table[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(res))

# Usage: python hvlcs.py <input-file>
def main():
    if len(sys.argv) != 2:
        print("Usage: python hvlcs.py <input-file>")
        sys.exit(1)

    # parse input file
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        n = int(file.readline().strip())

        # character values dict
        values = {
            line.split()[0]: int(line.split()[1])
            for line in islice(file, n)
        }

        # input strings
        a = file.readline().strip()
        b = file.readline().strip()

    # invoke hvlcs()
    table, max_val = hvlcs(a, b, values)
    print(max_val)

    # invoke backtrack()
    c = backtrack(table, a, b, values)
    print(c)

if __name__ == "__main__":
    main()
    sys.exit(0)
