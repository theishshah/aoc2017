valid = 0

check1_valid = []

with open('inp') as f:
    lines = f.readlines()

def is_valid(line):
    words =  line.split()
    count = dict()
    for w in words:
        count[w] = count.get(w,0) + 1
    for key in count:
        if count[key] != 1:
            return False
    
    return True

for l in lines:
    flag = is_valid(l)
    if flag:
        check1_valid.append(l)

print valid