#30-12: Child
#13-19: Teenager
#20-64: Adult
#65 and above: Senior
def age_classify(age):
  if 0 <= age <= 12:
    return "Child"
  elif 13 <= age <= 19:
    return "Teenager"
  elif 20 <= age <= 64:
    return "Adult"
  else:
    return "Senior"
input = age_classify(35)
print(input)
    
  

    
