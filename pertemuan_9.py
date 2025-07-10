'''
def luas_persegi_panjang(panjang, lebar):
    luas = panjang*lebar
    return luas
panjang=70
lebar=6

print("luas persegi panjang: ", luas_persegi_panjang(panjang,lebar))
'''


listmakanan={
    1:"Bakso",
    2:"Nasi goreng",
    3:"Gulai",
    4:"Sate"
    }
print("List makanan: ")
for key, value in listmakanan.items():
    print(key, value)

def pesan(nomor, jumlah):
    if pilih==1:
        harga==2000
    elif pilih==2:
        harga==15000
    elif pilih==3:
        harga==25000
    elif pilih==4:
        harga==10000
    total=harga*jumlah
    return total


menu=int(input("Jumlah pesanan anda : "))
if menu== 1:
    menu_makanan()
elif menu== 2:
    tampil_makanan()
else:
    break
