blocks = int(input("Enter number of blocks: "))

height = 0

while (height+1) <= blocks:
    
    height += 1
    blocks -= height
    
    
print("Height of the pyramid:",height)
