print("PROBLEM 37")

array = [1,2,3]
array_output = []
for x in array:
  for y in range(x+1,len(array)+1):
    array_output.append([x,y])
  array_output.append([x])

print(array_output)
