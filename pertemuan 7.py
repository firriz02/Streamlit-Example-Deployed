


'''
kamus={'jkt':'jakarta',
       'bdg':'bandung',
       'jog':'Jogja'}

#print(namaDict[key])
print(kamus['jog'])

#menambahkan data di Dict
'''
nomor=input("masukkan input 1/2/3: ")
nomor=input("pilih menu (1/2/3): ")
platnomor={}
if nomor== '1':
    key=input("BN")
    val=input("BANGKA ")
    platnomor[key]=val
elif nomor=='2':
    key=input("BH")
    val=input("JAMBI ")
    platnomor[key]=val
elif nomor=='3':
    key=input("DK")
    val=input("BALI ")
    platnomor[key]=val
else:
    print("tidak ada plat nomor:")
print(platnomor)
