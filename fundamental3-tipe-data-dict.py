"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""
kamus_ind_eng = {'anak': 'son', 'istri': 'wive', 'ibu': 'mother', 'ayah': 'father'}

print(kamus_ind_eng)
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['ayah'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-08-30',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 25},
        {'nama': 'Tri', 'jarak': 30},
        {'nama': 'Catur', 'jarak': 100},
    ]
}

print(data_dari_server_gojek)
print(f"\nDriver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #3 {data_dari_server_gojek['driver_list'][2]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter ")
