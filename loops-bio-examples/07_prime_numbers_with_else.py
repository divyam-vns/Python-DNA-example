# Loop with inner for + else.

N = 10
for y in range(2, N):
    for x in range(2, y):
        if y % x == 0:
            print(y, "=", x, "*", y // x)
            break
    else:
        print(y, "is a prime number")

# Output:
# 2 is a prime number
# 3 is a prime number
# 4 = 2 * 2
# 5 is a prime number
# 6 = 2 * 3
# 7 is a prime number
# 8 = 2 * 4
# 9 = 3 * 3
