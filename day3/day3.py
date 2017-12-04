import math

def spiral_boi(num):
    side_len = int(math.sqrt(num))
    if side_len%2==0:
        side_len += 1
    else:
        side_len += 2
    v_dist = (side_len)/2

    #off = (side_len*side_len)-num
    off = num - (side_len - 2) **2
    while off>side_len:
        off -= side_len
    h_dist = v_dist - off

    return v_dist+h_dist

val = 312051

def dist1(n): 
    g = int(n**0.5)**2 
    if g == n: 
        g = int((n-1)**0.5)**2 
    r = int(n**0.5 / 2) 
    if g % 2 == 1: 
        if n - (g + 1) <= g**0.5: 
            return abs(n - (g + 1 + r)) + r + 1 
        elif n - (g + 1) <= g**0.5 + (g**0.5 + 1): 
            return abs(n - (g + 1 + r + (g**0.5 + 1))) + r + 1 
        elif n - (g + 1) <= g**0.5 + 2*(g**0.5 + 1): 
            return abs(n - (g + 1 + r + 2*(g**0.5 + 1))) + r + 1 
        else: 
            return abs(n - (g + 1 + r + 3*(g**0.5 + 1))) + r + 1
    else:
        print "broken"

print dist1(val)
