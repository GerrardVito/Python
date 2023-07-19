import re

def integral(a: int, b: int = 1, x1=0, x2=0):
    koef = a / (b + 1)
    pangkat = b + 1
    if x1 == 0 and x2 == 0:
        print(f"Hasil integrasi = {koef}x^{pangkat} + C")
    else:
        print(f"Hasil integrasi = {(koef * (int(x1) ** pangkat)) - (koef * (int(x2) ** pangkat))}")

ygy = input("Integral dari (format: Koefisien x^ pangkat): ")

# Extract Koefisien and pangkat using regular expressions
pattern = r"(-?\d+(?:,\d+)*(?:\.\d+)?)x\^(-?\d+)"
matches = re.findall(pattern, ygy)

if matches:
    koefisien, pangkat = matches[0]
    integral(float(koefisien.replace(',', '')), int(pangkat))
else:
    print("Format input tidak valid.")

limita = input("Limit atas: ")
limitb = input("Limit bawah: ")
integral(float(koefisien.replace(',', '')), int(pangkat), int(limita), int(limitb))