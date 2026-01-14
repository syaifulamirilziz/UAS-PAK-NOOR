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

skor = 2000

angka = random.randint(batas_bawah, batas_atas)


print("\nSaya sudah memilih angka antara 1 sampai 100")

for i in range(kesempatan):
    print(f"\nKesempatan ke-{i+1}")
    print(f"skor saat ini: {skor}")


    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan > angka:
        print("Angkaku lebih ke bawah")
        skor -= 5
    elif tebakan < angka:
        print("Angkaku lebih ke atas")
        skor -= 5
    else:
        print(f"🎉 Selamat {nama}, tebakan kamu BENAR!")
        skor += 20
        break
else:
    print("❌ Kesempatan habis!")
    print(f"Angka yang benar adalah: {angka}")
    print("\n=== GAME SELESAI ===")
    print(f"Nama : {nama}")
    print(f"skor akhir : {skor}")
    exit()

# ================= LEVEL 2 =================
print("\n--- LEVEL 2 --- : MENENGAH ---")
print("Peraturan")
print("1. Tebak angka dari 1 sampai 1000")
print("2. Kesempatan 15 kali")


batas_bawah = 1
batas_atas  = 1000
kesempatan  = 15

angka = random.randint(batas_bawah, batas_atas)

for i in range(kesempatan):
    print(f"\nKesempatan ke-{i+1}")
    print(f"Skor saat ini: {skor}")

    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan > angka:
        print("Angkaku lebih ke bawah")
        skor -= 5
    elif tebakan < angka:
        print("Angkaku lebih ke atas")
        skor -= 5
    else:
        print("🎉 Tebakan kamu BENAR!")
        skor += 30
        break
else:

    print("❌ Kesempatan habis!")
    print(f"Angka yang benar adalah: {angka}")
    print("\n=== GAME SELESAI ===")
    print(f"Skor akhir: {skor}")
    exit()

# ================= LEVEL 3 =================
print("\n--- LEVEL 3 --- : SULIT ---")
print("Peraturan")
print("1. Tebak angka dari 1 sampai 2500")
print("2. Kesempatan 15 kali")


batas_bawah = 1
batas_atas  = 2500
kesempatan  = 15

angka = random.randint(batas_bawah, batas_atas)

for i in range(kesempatan):
    print(f"\nKesempatan ke-{i+1}")
    print(f"Skor saat ini: {skor}")

    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan > angka:
        print("Angkaku lebih ke bawah")
        skor -= 10
    elif tebakan < angka:
        print("Angkaku lebih ke atas")
        skor -= 10
    else:
        print("🔥 Tebakan kamu BENAR! Kamu menamatkan game!")
        skor += 50
        break
else:
    print("❌ Kesempatan habis!")
    print(f"Angka yang benar adalah: {angka}")

print("\n=== GAME SELESAI ===")
print(f"Nama : {nama}")
print(f"Skor akhir : {skor}")

# ================= LEADERBOARD =================

leaderboard = []

# menyimpan data pemain
leaderboard.append({
    "nama": nama,
    "skor": skor
})

# mengurutkan leaderboard berdasarkan skor (tertinggi ke terendah)
leaderboard = sorted(leaderboard, key=lambda x: x["skor"], reverse=True)

print("\n=== LEADERBOARD ===")
for i, data in enumerate(leaderboard, start=1):
    print(f"{i}. {data['nama']} - {data['skor']} poin")
