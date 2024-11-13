'''
Pascal's Triangle
'''


rows = int(input("Enter number of rows to print: "))
print()

first_row = [1]
last_row = [1, 1]

j = 1
while j < rows:
    print(' ', end='')
    j += 1

for i in first_row:
    # print(str(i) + ' ', end='')
    print('▲', end='')
    
print()

j = 1
while j < rows - 1:
    print(' ', end='')
    j += 1

for i in last_row:
    # print(str(i) + ' ', end='')
    print('▲ ', end='')

next_row = last_row.copy()

index = 0
iteration = 2

while iteration < rows:
    print("")
    
    next_row = [0] * (len(last_row) + 1)
    
    last_row.insert(0, 0)
    shifted_row = last_row.copy()
    last_row.pop(0)
    last_row += [0]
    
    while index < len(next_row):
        next_row[index] = last_row[index] + shifted_row[index]
        index += 1
        
    index = 0
    
    j = 1
    while j < (rows - iteration):
        print(' ', end='')
        j += 1
        
    for i in next_row:
        # print(str(i) + ' ', end='')
        if i % 2 == 0:
            print('  ', end='')
        else:
            print('▲ ', end='')
    
    iteration += 1
    last_row = next_row.copy()
