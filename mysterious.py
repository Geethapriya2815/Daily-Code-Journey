#1.Imagine you have two mysterious numbers.
#Your task is to write a program that reveals which one of them is the bigger one. How will you solve this puzzle?

def mysterious(a,b):
  if a>b:
    print(a)
  elif b>a:
    print(b)
  else:
        return "Both are equal"  

example = mysterious(10,5)
    print("Bigger one is :",example)
