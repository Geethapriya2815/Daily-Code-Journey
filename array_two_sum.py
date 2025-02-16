def Twosum(arr,target):
  c=set()
  for i in arr:
    c1=target-i
    if c1 in c:
      return True
    c.add(i)
  return False
