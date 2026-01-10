import random

print("==== GAME TEBAK ANGKA ====")
nama = input("Masukan nama kamu: ")

print("\n--- LEVEL 1 --- : PEMANASAN ---")
print("Peraturan")
print("1. Tebak angka dari 1 sampai 100")
print("2. Kesempatan 15 kali")
print("3. Tidak ada batas waktu")
print("4. Setiap tebakan akan diberi petunjuk apakah angka terlalu ke atas atau terlalu ke bawah")

batas_bawah = 1   #
batas_atas  = 100 #
kesempatan  = 15  #

angka = random.randint(batas_bawah, batas_atas)


print("Saya sudah memilih angka antara 1 sampai 100")

for i in range(kesempatan):
    print(f"\nKesempatan ke-{i+1}")
    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan > angka:
        print("Angkaku lebih ke bawah")
    elif tebakan < angka:
        print("Angkaku lebih ke atas")
    else:
        print(f"🎉 Selamat {nama}, tebakan kamu BENAR!")
        break
else:
    print("❌ Kesempatan habis!")
    print(f"Angka yang benar adalah: {angka}")

print("\n=== GAME SELESAI ===")