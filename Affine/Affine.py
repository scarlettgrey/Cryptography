import cryptomath

simbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
mode = 'e'

def getKey(kunci):
    ka = kunci // len(simbol)
    kb = kunci % len(simbol)
    return (ka,kb)

def encryptpesan(pesan,ka,kb):
    hasil = ''
    for Simbol in pesan:
        if Simbol in simbol:
            index = simbol.find(Simbol)
            hasil += simbol[(index * ka + kb) % len(simbol)]
        else :
            hasil += Simbol
    return hasil

def decryptpesan(pesan,ka,kb):
    hasil = ''
    modInverseOfka = cryptomath.findModInverse(ka,len(simbol))
    for Simbol in pesan:
        if Simbol in simbol:
            index = simbol.find(Simbol)
            hasil += simbol[(index - kb) * modInverseOfka % len(simbol)]
        else :
            hasil += Simbol
    return hasil

pesan = input("Masukkan kalimat: ")
kunci = int(input("Masukkan kunci: "))
mode = input("\'e\' untuk encrypt, \'d\' untuk decrypt: ")
ka, kb = getKey(kunci)

if mode == 'e':
    hasil = encryptpesan(pesan,ka,kb)
elif mode == 'd':
    hasil = decryptpesan(pesan,ka,kb)

ka, kb = getKey(kunci)
modInverseOfka = cryptomath.findModInverse(ka,len(simbol))
print("Affine Key:",kunci)
print("Affine Key-a:",ka)
print("Affine Key-b:",kb)
print("Affine ModInverse Key-a:",modInverseOfka)
print()
print("Affine chipertext:")
if mode == 'e':
    print(hasil)
elif mode == 'd':
    print(pesan)
print()
print("Affine plaintext:")
if mode == 'e':
    print(pesan)
elif mode == 'd':
    print(hasil)

