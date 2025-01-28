#You have two secret numbers, and you need to figure out how they relate to each other using a set of special tools. 
#Your challenge is to write a program that uses these tools—>,>=, <, <=, ==, and !=—to uncover all the secrets about how these numbers compare. 
#How will you use each tool to solve the puzzle?
#For example, consider two numbers 15 and 20. 
#15 < 20 is true.
#15 <= 20 is true.
#15 > 20 is false. 
#15 >= 20 is false. 
#15 == 20 is false. 
#15 != 20 is true.

def puzzle_special_tools(a, b):
    results = {
        "a < b": a < b,
        "a <= b": a <= b,
        "a > b": a > b,
        "a >= b": a >= b,
        "a == b": a == b,
        "a != b": a != b
    }
   #i = comparison #j = result true or false 
    for i,j  in results.items():
        print(f"{comparison} is {result}")


puzzle_special_tools(15, 20)
