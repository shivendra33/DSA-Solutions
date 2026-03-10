limit = 20

for a in range(1,limit):
    for b in range(a+1,limit):
        c = (a*a + b*b)**0.5
        if c.is_integer() and c <= limit:
            print(a,b,int(c))