# input=dinesh
# output=glqhvk (d=e,f,g.. so printing g for d)

name=input("enter your name:")
listofletters=list(name)
print(listofletters)
len=len(listofletters)
alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
indexes=[]
for i in listofletters:
  indexes.append(alph.index(i))
print(indexes)
empty=[]
for j in indexes:
  empty.append(alph[j+3])
print(empty)

print(''.join(empty))






