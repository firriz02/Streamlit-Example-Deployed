#menambah list item

#
buah=['tomat','ceri','durian','jeruk','ceri']
print(buah)


#menampilkan data dari index
'''
print(buah[-2])
'''

##Merubah Isi List
#namalist[index ke-] = perubahan
'''
buah[0:2]='markisa','pepaya'
print(buah)
'''

#menambahkan isi list
#namalist.append(value)
'''
buah.append(["mangga","pir"])
print(buah)
'''

#menambahkan index berdasarkan index
#namalist.insert(index,value)
'''
buah.insert(0,"jambu")
print(buah)
'''

##Menambahkan item baru di akhir list
# namalist.extend(value)
'''
buah.extend(["jambu"])
print(buah)
'''

##menghapus item list
'''
del buah[2]
print(buah)

buah.remove("markisa")
print(buah)
'''

#mengurutkan data
'''
buah.sort()
print(buah)
##menampilkan list secara perbaris
for elemen in buah:
    print(elemen)
'''
'''
#tuple
tup_buah=('tomat','ceri','durian','jeruk')
print(tup_buah)
#tup_buah.append("pepaya")
#pencarian data tuple
print(tup_buah[2])
'''

#set
buah.append("ceri")
print(buah)
set_buah= set(buah)
print(set_buah)
set= {'A'
