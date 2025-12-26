from config import batasData

def validasiData(data):
    if not isinstance(data, list):
        raise ValueError("Data harus berupa array")

    if len(data) == 0:
        raise ValueError("Data tidak boleh kosong")

    if len(data) > batasData:
        raise ValueError(f"Jumlah data maksimal {batasData}")

    for x in data:
        if not isinstance(x, int):
            raise ValueError("Semua elemen data harus bilangan bulat")
