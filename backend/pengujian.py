import time
import math
from algoritma import modusIteratif, modusRekursif
from config import jumPengujian

def rataRata(data):
    return sum(data) / len(data)

def deviasi(data):
    mean = rataRata(data)
    return math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))

def ujiModus(data):
    hasil = {}

    # Iteratif
    waktu = []
    for _ in range(jumPengujian):
        start = time.perf_counter()
        modusIteratif(data)
        waktu.append(time.perf_counter() - start)

    hasil["iteratif"] = {
        "rataRata": rataRata(waktu),
        "deviasi": deviasi(waktu)
    }

    # Rekursif
    waktu = []
    for _ in range(jumPengujian):
        start = time.perf_counter()
        modusRekursif(data)
        waktu.append(time.perf_counter() - start)

    hasil["rekursif"] = {
        "rataRata": rataRata(waktu),
        "deviasi": deviasi(waktu)
    }

    return hasil
