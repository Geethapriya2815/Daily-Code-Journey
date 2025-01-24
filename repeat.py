def repeat(lst):
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:  
            return lst[i] 
    return None  

input_list = [1, 2, 2, 1, 4]
result = repeat(input_list)
print(result) 
