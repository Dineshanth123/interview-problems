n = int(input("Enter number of rows: "))
l=n
x=2*n-1
for i in range(n):
    n=n-1
    print(' ' * (n), end='')  
    print('*' * ((2*l)-x))   
    x=x-2       
