def print_mirrored_triangle(size):
    # Upper part of the pattern
    for i in range(1, size + 1):
        print(" " * (size - i) + "* " * i)

    # Lower part of the pattern
    for i in range(size - 1, 0, -1):
        print(" " * (size - i) + "* " * i)


size = 7
print_mirrored_triangle(size)
