import secrets

simbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def encryptpesan(pesan,otp):
    hasil = ''
    a = 0
    for i in pesan:
        if i in simbol:
            idxpesan = simbol.find(i)
            idxotp = simbol.find(otp[a])
            angka = (idxpesan + idxotp) % len(simbol)
            if i.isupper():
                hasil += simbol[angka].upper()
            elif i.islower():
                hasil += simbol[angka].lower()
            a += 1
        else:
            hasil += i
    return hasil

def decryptpesan(pesan,otp):
    hasil = ''
    a = 0
    for i in pesan:
        if i in simbol:
            idxpesan = simbol.find(i)
            idxotp = simbol.find(otp[a])
            angka = (idxpesan - idxotp) % len(simbol)
            if i.isupper():
                hasil += simbol[angka].upper()
            elif i.islower():
                hasil += simbol[angka].lower()
            a += 1
        else:
            hasil += i
    return hasil

otp = ''
pesan = input("Masukkan Kalimat: ")
mode = input("\'e\' untuk encrypt, \'d\' untuk decrypt: ")

for i in range(len(pesan)):
   otp += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

if mode == 'e':
    hasil = encryptpesan(pesan,otp)
elif mode == 'd':
    hasil = decryptpesan(pesan,otp)

print("One Time Pad Key:")
print(otp)
print()
print("One Time Pad chipertext:")
if mode == 'e':
    print(hasil)
elif mode == 'd':
    print(pesan)
print()
print("One Time Pad plaintext:")
if mode == 'e':
    print(pesan)
elif mode == 'd':
    print(hasil)