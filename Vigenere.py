simbol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def prosesPesan(pesan,kunci,mode):
    hasil = []
    index = 0
    kunci = kunci.upper()
    for Simbol in pesan:
        num = simbol.find(Simbol)
        if num != -1:
            if mode == 'e':
                num += simbol.find(kunci[index])
            elif mode == 'd':
                num -= simbol.find(kunci[index])

            num %= len(simbol)

            if Simbol.isupper():
                hasil.append(simbol[num])
            elif Simbol.islower():
                hasil.append(simbol[num].lower())

            index += 1
            if index == len(kunci):
                index = 0
        else:
            hasil.append(Simbol)
    return ''.join(hasil)

pesan = input("Masukkan Kalimat: ")
kunci = input("Masukkan Kunci: ")
mode = input("\'e\' untuk encrypt, \'d\' untuk decrypt: ")
hasil = prosesPesan(pesan,kunci,mode)

print("Vigenere Key:",kunci)
print()
print("Vigenere chipertext:")
if mode == 'e':
    print(hasil)
elif mode == 'd':
    print(pesan)
print()
print("Vigenere plaintext:")
if mode == 'e':
    print(pesan)
elif mode == 'd':
    print(hasil)

#THE VIGENÈRE CIPHER, WAS INVENTED BY A FRENCHMAN, BLAISE DE VIGENÈRE IN THE 16TH CENTURY. TO FIND THE ENCRYPTION, WE TAKE THE LETTER FROM THE INTERSECTION OF THE KEY LETTER ROW, AND THE PLAINTEXT LETTER COLUMN. TO DECIPHER THE MESSAGE, THE RECIPIENT NEEDS TO WRITE OUT THE KEY ABOVE THE CIPHERTEXT AND REVERSE THE PROCESS.