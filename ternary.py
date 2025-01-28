#You have three hidden numbers, and your mission is to find out which one is the greatest. 
#Write a program that can reveal the highest of these three numbers.8A.
#Perform the above operation using ternary operator.

def ternary(a,b,c):
  highest = a if a > b and a > c else (b if b > c else c)
    print(f"The highest number is: {highest}")
ternary(10,20,8)

    
