x=input("enter a string:")
letters=list(x)
len=len(letters)
y=[]
for x in range(len):
  len=len-1
  y.append(letters[len])
print(''.join(y))