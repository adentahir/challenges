def averagelist(l):
  total=0
  i=0
  for value in l:
    total = total + value
    i +=1
  average=total/i
  return average
  

l2=[2,5,6,8,56,3]
print(averagelist(l2))


 
