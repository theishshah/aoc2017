with open('inp') as f:
    data = map(int, f.readlines())

steps = 0
index = 0

while index in range(len(data)):
    temp_index = index
    jump = data[temp_index]
    index += data[temp_index]
    
    #if abs(jump) >= 3:
     #   data[temp_index] -= 1
    #else:    
    data[temp_index] += 1

    #count
    steps += 1

print steps
