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

print spiral_boi(12)
