base = int(input("Gib eine Basis ein: "))
vk = input("Gib die Vorkommazahl ein: ")
nk = input("Gib die Nachkommazahl ein: ")

def baseBToDecV(base, vk):
    D = int(vk[0])
    for i in range(1,len(vk)):
        D = (D * base) + int(vk[i])
    return D

def baseBToDecN(base, nk):
    N = 0
    for i in range(1,len(nk)+1):
        N = (N + int(nk[-i]))/base
    return N

dv = baseBToDecV(base, vk)
print(dv)
dn = baseBToDecN(base, nk)
print(dn)
print(dv+dn)