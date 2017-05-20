# -*- coding: UTF-8 -*-

a = []

with open("test04.txt") as f:
    x, y, r = f.readline().split()
    x = int(x)
    y = int(y)
    r = int(r)

    n = int(f.readline())

    a = []
    for i in range(n):
        x1, y1 = f.readline().split()
        x1 = int(x1)
        y1 = int(y1)
        a.append((x1, y1))

a.append((a[0][0], a[0][1]))

min_x = x-r
min_y = y-r
max_x = x+r
max_y = y+r

for i in range(n):
    if a[i][0] < min_x:
        min_x = a[i][0]
    if a[i][1] < min_y:
        min_y = a[i][1]
    if a[i][0] > max_x:
        max_x = a[i][0]
    if a[i][1] > max_y:
        max_y = a[i][1]

i = 1
s1 = 0

while i <= n-2:
    _s = abs(0.5*((a[0][0] - a[i+1][0])*(a[i][1] - a[i+1][1]) - (a[i][0] - a[i+1][0])*(a[0][1] - a[i+1][1])))
    s1 += _s
    i += 1

union = 0
intersection = 0

x1 = min_x
while x1 <= max_x:
    y1 = min_y
    while y1 <= max_y:

        i = 0
        s2 = 0
        while i <= n-1:
            _s = abs(0.5*((x1 - a[i+1][0])*(a[i][1] - a[i+1][1]) - (a[i][0] - a[i+1][0])*(y1 - a[i+1][1])))
            s2 += _s
            i += 1

        flag1 = False;
        flag2 = False;

        if ((x1 - x)*(x1 - x) + (y1 - y)*(y1 - y) < r*r): 
            flag1 = True

        if abs(s1-s2) < 0.01:
            flag2 = True
          
        if (flag1 and flag2):
            union += 1
            intersection += 1
 
        if (flag1 and not flag2 or not flag1 and flag2):
             union += 1
         
        y1+=0.01
    x1+=0.01

with open("output.txt", "w") as f:
    f.write('%f' % (intersection/float(union)))



