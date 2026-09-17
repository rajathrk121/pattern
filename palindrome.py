n = 5

for i in range(1, n):
    # spaces
    for j in range(n - i):
        print(" ", end="")

    # decreasing numbers
    for j in range(i, 0, -1):
        print(j, end="")

    # increasing numbers
    for j in range(2, i + 1):
        print(j, end="")

    print()