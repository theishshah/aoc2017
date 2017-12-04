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

def check_two(line):
    words = line.split()
    sorty = set()
    
    for w in words:
        sorty.add(str(sorted(w)))
    return len(sorty) == len(words)

for l in lines:
    flag = is_valid(l)
    if flag:
        check1_valid.append(l)

for l in check1_valid:
    flag = check_two(l)
    if flag:
        valid += 1

print valid