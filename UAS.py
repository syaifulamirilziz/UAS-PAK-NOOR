import random

# komputer memilih angka acak
angka = random.randint(1, 100)

print("=== GAME TEBAK ANGKA ===")
print("Saya sudah memilih angka antara 1 sampai 100")

while True:
    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan > angka:
        print("Angkaku lebih ke bawah")
    elif tebakan < angka:
        print("Angkaku lebih ke atas")
    else:
        print("Selamat! Tebakan kamu benar 🎉")
        break
