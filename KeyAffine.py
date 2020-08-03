#Untuk mencari key, keyA, keyB, dan ModInverseKeyA
import cryptomath

simbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pesan = input("Masukkan cipher: ")
pesan1 = input("Masukkan plain: ")
hasil = ''

def getKey(kunci):
    ka = kunci // len(simbol)
    kb = kunci % len(simbol)
    return (ka,kb)

def decryptpesan(pesan,ka,kb):
    hasil = ''
    modInverseOfka = cryptomath.findModInverse(ka,len(simbol))
    for Simbol in pesan:
        if Simbol in simbol:
            index = simbol.find(Simbol)
            hasil += simbol[(index - kb) * modInverseOfka % len(simbol)]
        else :
            hasil += Simbol
    return hasil,modInverseOfka

kunci = 0
while True:
    ka, kb = getKey(kunci)

    hasil,modInverseOfka = decryptpesan(pesan,ka,kb)
    
    if hasil == pesan1:
        print("Affine Key:",kunci)
        print("Affine Key-a:",ka)
        print("Affine Key-b:",kb)
        print("Affine ModInverse Key-a:",modInverseOfka)
        break
    kunci += 1