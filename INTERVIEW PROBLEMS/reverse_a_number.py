numbers=list(map(str,input().split()))
len=len(numbers)
y=[]
for x in range(len):
  len=len-1
  y.append(numbers[len])
print(y)
fin=(' '.join(y))

print(fin)
print(type(fin))

