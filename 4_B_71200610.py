print("="*5+"GEBYAR DISKON"+"="*5)
print("="*5+"MASUKKAN JUMLAH BARANG YANG DIPESAN"+"="*5)
kipas = int(input("KIPAS ANGIN DISKON 10%   Rp 25.000,00    : "))
kipas = (25000.0 * 10/100) * kipas
sepeda = int(input("SEPEDA DISKON 55%   Rp 6.000,00    : "))
sepeda = (6000.0 * 55/100) * sepeda
helm = int(input("HELM ROSSI DISKON 77%   Rp 8.000,00    : "))
helm = (8000.0 * 77/100) * helm
print("="*5+"TOTAL"+"="*5)
print("TOTAL KIPAS ANGIN    : Rp", float(kipas) )
print("TOTAL SEPEDA    : Rp", float(sepeda) )
print("TOTAL HELM ROSSI    : Rp", float(helm) )
diskon = kipas + sepeda + helm
print("Jumlah total diskon yang didapat adalah", diskon )