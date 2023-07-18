def integral(a: int, b:int= 1, x1=0, x2=0):
    koef = a / (b + 1)
    pangkat = b + 1
    if x1 == 0 and x2 == 0:
        print(f"Hasil integrasi = {koef}x^{pangkat} + C")
    else:
        print(f"Hasil integrasi = {(koef * (int(x1) ** pangkat)) - (koef * (int(x2) ** pangkat))}")


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
