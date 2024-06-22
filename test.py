import json
import os

def read_accident_log(file_path):
    """
    Membaca file accident_log.json dan mengembalikan datanya sebagai dictionary.
    
    :param file_path: Path ke file accident_log.json
    :return: Dictionary berisi data kecelakaan
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Contoh penggunaan fungsi
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "accident_log.json")
accident_data = read_accident_log(file_path)

# Cetak data untuk verifikasi
print(accident_data['0'])
