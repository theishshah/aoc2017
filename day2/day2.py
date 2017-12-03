def row_checksum(row):
    maxi = 0
    nums = row.split()
    for n in nums:
        if int(n)>= maxi:
            maxi = int(n)
    
    mini = maxi

    for n in nums:
        if int(n)<= mini:
            mini = int(n)

    return maxi-mini

def row_evendivide(row):
    nums = row.split()
    for n in nums:
        for i in nums:
            if int(n)%int(i)==0 and int(n)!=int(i):
                return int(n)/int(i)
    return 0

total = 0

with open('day2_inp') as f:
    lines = f.readlines()

for l in lines:
    total += row_evendivide(l)

print total