def missingNumber(self, arr):
        # code here
        n = len(arr)
        sums = (n+1) * (n+2)// 2
        arrsums = sum(arr)
        totalsum = sums - arrsums
        return totalsum
