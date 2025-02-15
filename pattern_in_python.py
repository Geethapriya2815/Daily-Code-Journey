def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def increasing_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def decreasing_triangle(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()

def right_side_triangle(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()

def left_side_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        for j in range(n - i - 1):
            print(" ", end=" ")
        print()

def hill_pattern(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("*", end=" ")
        print()

def reverse_hill_pattern(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(2 * (n - i) - 1):
            print("*", end=" ")
        print()

def diamond_pattern(n):
    hill_pattern(n)
    reverse_hill_pattern(n - 1)

n = 5

print("Square Pattern:")
square(n)

print("\nIncreasing Triangle Pattern:")
increasing_triangle(n)

print("\nDecreasing Triangle Pattern:")
decreasing_triangle(n)

print("\nRight Side Triangle Pattern:")
right_side_triangle(n)

print("\nLeft Side Triangle Pattern:")
left_side_triangle(n)

print("\nHill Pattern:")
hill_pattern(n)

print("\nReverse Hill Pattern:")
reverse_hill_pattern(n)

print("\nDiamond Pattern:")
diamond_pattern(n)
