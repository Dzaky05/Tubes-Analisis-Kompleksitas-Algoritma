import random
import time
import sys  # Import sys untuk mengatur limit rekursi

# ===============================
# PENGATURAN LIMIT REKURSI
# ===============================
# Agar n > 1000 tidak error, kita naikkan batas rekursi sistem
sys.setrecursionlimit(2000) 

# ===============================
# GENERATE DATA RANDOM
# ===============================
def generate_data(n, batas_angka=10000):
    return [random.randint(1, batas_angka) for _ in range(n)]

# ===============================
# MODUS ITERATIF
# ===============================
def modusIteratif(data):
    if not data: return None
    frekuensi = {}
    for angka in data:
        frekuensi[angka] = frekuensi.get(angka, 0) + 1
    return max(frekuensi, key=frekuensi.get)

# ===============================
# MODUS REKURSIF
# ===============================
def _hitungFrekuensi(data, index, frekuensi):
    # Base case: jika index sudah mencapai ujung data
    if index == len(data):
        return frekuensi

    angka = data[index]
    frekuensi[angka] = frekuensi.get(angka, 0) + 1
    # Recursive call
    return _hitungFrekuensi(data, index + 1, frekuensi)

def modusRekursif(data):
    if not data: return None
    # Pastikan limit cukup untuk panjang data
    if len(data) >= sys.getrecursionlimit():
        sys.setrecursionlimit(len(data) + 100)
        
    frekuensi = _hitungFrekuensi(data, 0, {})
    return max(frekuensi, key=frekuensi.get)

# ===============================
# UKUR WAKTU EKSEKUSI
# ===============================
def ukur_waktu(fungsi, data):
    start = time.perf_counter()
    hasil = fungsi(data)
    end = time.perf_counter()
    return hasil, end - start

# ===============================
# FUNGSI UTAMA
# ===============================
def hitung_modus_dari_n(n):
    data = generate_data(n)

    hasil_iteratif, waktu_iteratif = ukur_waktu(modusIteratif, data)
    
    # Tambahkan handling agar rekursif tidak crash jika n terlalu besar bagi memori
    try:
        hasil_rekursif, waktu_rekursif = ukur_waktu(modusRekursif, data)
    except RecursionError:
        hasil_rekursif, waktu_rekursif = "Error: Terlalu Dalam", 0

    return {
        "n": n,
        "modus_iteratif": hasil_iteratif,
        "waktu_iteratif": f"{waktu_iteratif:.6f} s",
        "kompleksitas_iteratif": "O(n)",
        "modus_rekursif": hasil_rekursif,
        "waktu_rekursif": f"{waktu_rekursif:.6f} s",
        "kompleksitas_rekursif": "O(n)"
    }

# ===============================
# TEST MANUAL
# ===============================
if __name__ == "__main__":
    # Mencoba dengan n yang berbeda
    for n_test in [10, 100, 500, 1000]:
        print(f"Menguji n = {n_test}...")
        print(hitung_modus_dari_n(n_test))
        print("-" * 30)