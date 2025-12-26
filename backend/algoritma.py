def modusIteratif(data):
    frekuensi = {}

    for angka in data:
        frekuensi[angka] = frekuensi.get(angka, 0) + 1

    return max(frekuensi, key=frekuensi.get)



def _hitungFrekuensi(data, index, frekuensi):
    if index == len(data):
        return frekuensi

    angka = data[index]
    frekuensi[angka] = frekuensi.get(angka, 0) + 1
    return _hitungFrekuensi(data, index + 1, frekuensi)


def modusRekursif(data):
    frekuensi = _hitungFrekuensi(data, 0, {})
    return max(frekuensi, key=frekuensi.get)
