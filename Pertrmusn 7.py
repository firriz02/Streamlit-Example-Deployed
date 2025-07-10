'''
#percabangan if,elif,dan else
nilai= int(input("Masukkan nilai ujian: "))

if nilai >=75 and nilai <=100:
    print("Selamat,Anda lulus! ")
elif nilai >100:
    print("Maaf, nilai tidak sesuai.")
else:
    print("Maaf, Anda Tidak lulus.")
    
#menghitung total belanja
total_pembelian=int(input("Masukkan total belanja: "))
if total_pembelian <= 50000:
    diskon= 0;
elif total_pembelian < 100000:
    diskon= 0.1
else:
   diskon=0.15

total_diskon=total_pembelian*diskon
total_bayar=total_pembelian-total_diskon
print("total bayar: Rp.",total_bayar,"\n total diskon:Rp.",total_diskon)
'''


#loop and Dictionary
kamus={'jkt':'jakarta',
      'bdg':'Bandung',
      'jog':'Jogja',
      'sby':'Surabaya'
      }
for key,value in kamus.items():
    print("Kunci: ",key,"\tNilai: ",value)
