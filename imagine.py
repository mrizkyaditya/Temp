"""
Menyeberangi Jembatan Gantung

Setelah membantu penduduk dengan makanan, mereka mengizinkanmu melintasi jembatan gantung. 
Namun, jembatan ini sangat rapuh. Hanya orang-orang dengan berat badan tertentu yang boleh menyeberang. 
Kamu harus menulis program untuk menentukan apakah kamu bisa menyeberang jembatan.

Contoh 1
Input:
weight = 50

Output:
Kamu tidak boleh menyeberang jembatan

Contoh 2
Input:
weight = 90

Output:
Kamu boleh menyeberang jembatan
"""
weight = int(input("Masukkan berat badan kamu :")  

# Contoh input berat badan
if weight >= 90:
    print("Kamu tidak boleh menyeberang jembatan")
else:
    print("Kamu boleh menyeberang jembatan")
