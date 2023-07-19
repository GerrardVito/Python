def integral(a: int, b: int = 1, x1=0, x2=0):
    koef = a / (b + 1)
    pangkat = b + 1
    if x1 == 0 and x2 == 0:
        print(f"Hasil integrasi = {koef}x^{pangkat} + C")
    else:
        print(f"Hasil integrasi = {(koef * (int(x1) ** pangkat)) - (koef * (int(x2) ** pangkat))}")


import re

pattern = r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b"
ygy = input("Integral dari (format: Koefisien x^ pangkat):")
matches = re.findall(pattern, ygy)
limita = input('Limit atas? : ')
limitb = input('Limit bawah? : ')
pros = []
for bados in matches:
    pros.append(int(bados))
integral(pros[0], pros[1], int(limita), int(limitb))
