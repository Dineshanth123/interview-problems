l=list(map(int,input().split()))
len=len(l)
sum=0
i=0
if(len%2==0):
  for x in range(len//2):
    res=l[i]
    sum=sum+res
    i=i+2
  print(sum)
else:
  for x in range((len//2)+1):
    res=l[i]
    sum=sum+res
    i=i+2
  print(sum)



  