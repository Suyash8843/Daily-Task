n = int(input("Enter width: "))

for i in range(n, 0, -2):
    for j in range((n - i) // 2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
