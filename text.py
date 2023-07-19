y = 0
g = ['x', 'x']
ygy=input("Integral dari (format: Koefisien x^ pangkat):")
limit = int(input("Limit 1: "))
limit2=int(input ("Limit 2: "))
for chai in ygy:
    # noinspection PyBroadException
    try:
        d = int(chai)
        g.append(d)
    except:
        pass
print(g)
integral(g[2], g[3], limit, limit2)
