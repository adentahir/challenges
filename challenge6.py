def averageList(l):
  sum =0
  average = 0.0
  for element in l:
    sum += element
  average = sum / len(l)
  return average
print(averageList([2,5,6,7,8,8]))