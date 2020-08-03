import secrets

simbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

pesan = input("Masukkan cipher: ")
pesan1 = input("Masukkan plain: ")

def decryptpesan(pesan,otp):
    hasil = ''
    a = 0
    for i in pesan:
        if i in simbol:
            idxpesan = simbol.find(i)
            idxotp = simbol.find(otp[a])
            angka = (idxpesan - idxotp) % len(simbol)
            hasil += simbol[angka]
            
        else:
            hasil += i
        a += 1
    return hasil

trueotp = []
for l in range(len(pesan)):
    trueotp.append(' ')

while True:
    otp = []
    for i in range(len(pesan)):
        a = secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        otp.append(a)
        if trueotp[i] in simbol:
            otp[i] = trueotp[i]
    
    hasil = decryptpesan(pesan,otp)
    
    for z in range(len(pesan)):
        if hasil[z] == pesan1[z] and pesan[z] in simbol:
            trueotp[z] = otp[z]
    
    if hasil == pesan1:
        print("One Time Pad Key:")
        print(''.join(trueotp).replace(' ',''))
        break
    