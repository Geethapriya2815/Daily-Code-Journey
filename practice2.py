#reverse without slice using
def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


input_string = "hellos"
print(reverse_string_loop(input_string)) 
