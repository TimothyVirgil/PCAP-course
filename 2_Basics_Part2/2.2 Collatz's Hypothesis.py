c_0 = int(input("Enter a non-negative, non-zero integer."))

counter = 0

while c_0 != 1:
    
    counter += 1
    
    if c_0 % 2 == 0:
        
        c_0 //= 2
        
    else:
        
        c_0 = 3 * c_0 + 1
        
    print(c_0,end=' ')
    
print(f'steps = {counter}')
