n = int(input("Enter a number: "))
l = []
x = 0
y = 1

for i in range(n):
    l.append(x)  
    z = x + y    
    x = y        
    y = z        

print(l)
