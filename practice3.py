#substring
s = "abcdef"
for i in range(1, len(s) + 1):
    for j in range(len(s) - i + 1):
        substring = s[i:i + j]
        print(substring)
