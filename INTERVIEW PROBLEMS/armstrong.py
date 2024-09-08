n=int(input("enter a number:"))
n1=n
length=len(str(n))
sum=0
for x in range(length):
  z=n1%10
  sum=sum+(z**length)
  n1=n1//10
print(sum)
if sum==n:
  print("armstrong")
else:
  print("not an armstrong")
