x = input("Enter the main string: ")
y = input("Enter the substring: ")

len1 = len(x)
len2 = len(y)
positions = []


for i in range(len1 - len2 + 1):  
    if x[i:i+len2] == y:  
        positions.append(i)  

if positions:
    print(f"The substring '{y}' is found at positions: {positions}")
else:
    print(f"The substring '{y}' was not found in the main string.")
