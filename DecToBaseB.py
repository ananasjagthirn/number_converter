import math

base = int(input("Gib eine Basis ein: "))
vk = input("Gib die Vorkommazahl ein: ")
nk = input("Gib die Nachkommazahl ein: ")
bitsv = []
bitsn = []

def DecToBaseBV(base, vk):
    D = int(vk)
    while D != 0:
        x = D % base
        bitsv.insert(0, x)
        D = math.floor(D / base)
    return D

def DecToBaseBN(base, nk):
    D = float(nk)
    while D != 0:
        x = math.floor(D * base)
        bitsn.append(x)
        D = (D * base) - (math.floor(D * base))
    return D

DecToBaseBV(base, vk)
#print(''.join(str(i) for i in bitsv))

DecToBaseBN(base, nk)
#print(''.join(str(j) for j in bitsn))

print(''.join(str(i) for i in bitsv) + "." + ''.join(str(j) for j in bitsn))