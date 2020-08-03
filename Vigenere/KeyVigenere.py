import secrets

simbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

pesan = input("Masukkan cipher: ")
pesan1 = input("Masukkan plain: ")

def prosesPesan(pesan,kunci):
    hasil = []
    index = 0
    for Simbol in pesan:
        num = simbol.find(Simbol)
        if num != -1:
            num -= simbol.find(kunci[index])

            num %= len(simbol)

            hasil.append(simbol[num])
            
            if index == len(kunci):
                index = 0
        else:
            hasil.append(Simbol)
        index += 1
    return ''.join(hasil)

truekey = []
for l in range(len(pesan)):
    truekey.append(' ')

a = 0 #index untuk pesan
while True:
    kunci = []
    for i in range(len(pesan)):
        a = secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        kunci.append(a)
        if truekey[i] in simbol:
            kunci[i] = truekey[i]

    hasil = prosesPesan(pesan,kunci)

    for z in range(len(pesan)):
        if hasil[z] == pesan1[z] and pesan[z] in simbol:
            truekey[z] = kunci[z]

    if hasil == pesan1:
        break

truekey = ''.join(truekey)
truekey = truekey.replace(' ','')

a = 0; b = 1
for m in range(len(truekey)-1):
    if truekey[a] == truekey[b]:
        a += 1; b += 1
    elif truekey[a] != truekey[b]:
        b += 1

print('Vigenere Key:',truekey[:b-a])

#THE VIGENÈRE CIPHER, WAS INVENTED BY A FRENCHMAN, BLAISE DE VIGENÈRE IN THE 16TH CENTURY. TO FIND THE ENCRYPTION, WE TAKE THE LETTER FROM THE INTERSECTION OF THE KEY LETTER ROW, AND THE PLAINTEXT LETTER COLUMN. TO DECIPHER THE MESSAGE, THE RECIPIENT NEEDS TO WRITE OUT THE KEY ABOVE THE CIPHERTEXT AND REVERSE THE PROCESS.

#XFI ZGKILÈVI AMTFIV, UEW GRZCRXCH FW E JPIRALQYR, FJEMQI HC ZMEIRÈPI ML XLC 16XL AIRRYVW. XS DMRB XLC IRAVCNXMMR, AC XEII XFI PCXXCV JPSQ RLI GRXCVWCGXGSR MJ XFI OCC PCXXCV VMA, ELH XFI TJEMLXIVX PCXXCV GMPYKR. XM HIAMTFIV RLI KIWQEKC, XLC VIAMTGIRR RICHW RS APMXC SYR XLC OIW EFMZI RLI AMTFIVRIBR ERB VITIVQI XFI TPSGCWW.