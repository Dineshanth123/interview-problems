n=int(input('enter binary code:'))
l=list(str(n))
l.reverse()
sum=0
for x in range(len(l)):
  sum=sum+int(l[x])*(2**x)
print(sum)
