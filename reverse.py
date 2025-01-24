def reverse(n):
    
    low = 0 
    high = len(n) - 1 
    
    while(low < high):
        n[low] ,n[high] = n[high] ,n[low]
        
        low += 1
        high -= 1
    return n 
input = reverse([1,3,1,0,2])
print(input)
