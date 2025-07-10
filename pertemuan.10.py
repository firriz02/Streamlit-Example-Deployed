'''class mobil:
    def __init__(self, merk, model, tahun):
        self.merk=merk
        self.model=model
        self.tahun=tahun

    def info(self):
        return "mobil {} {} ({})".format(self.merk, self.model, self.tahun)

    def nyalakan_mesin(self):
        return "mesin {} {} menyala!".format(self.merk, self.model)

    def matikan_mesin(self):
        return "mesin {} {} mati.".format(self.merk, self.model)
    
if __name__ =="__main__":
    mobil1=mobil("Toyota", "Corolla", 2020)
    mobil2=mobil("Honda", "Civic", 2018)

    print("---Informasi mobil---")
    print(mobil1.info())
    print(mobil2.info())

    print("\n---aksi mesin--")
    print(mobil1.nyalakan_mesin())
    print(mobil2.nyalakan_mesin())
    print(mobil1.matikan_mesin())
'''

class mobil:
    def __init__(self, merk, model, tahun):
      self.__merk=merk
      self.__model=model
      self.__tahun=tahun

    def get_merk(self):
        return self.__merk

    def set_merk(self, merk):
        self.__merk = merk

    def set_model(self,model):
        self.__model= model

    def get_model(self):
        return self.__model

    def get_tahun(self):
        return self.__tahun

    def set_tahun(self, tahun):
        self.__tahun = tahun

    def info(self):
        return "{} {} ({})".format(self.__merk, self.__model, self.__tahun)
    
    def nyalakan_mesin(self):
        return "mesin {} {} menyala!".format(self.__merk, self.__model)

    def matikan_mesin(self):
        return "mesin {} {} mati.".format(self.__merk, self.__model)
    
mobil1=mobil("Toyota", "Corolla", 2020)
mobil2=mobil("Honda", "Civic", 2018)

print(mobil1.info())
print(mobil2.info())

print(mobil1.nyalakan_mesin())
print(mobil2.nyalakan_mesin())

mobil1.set_merk("Nissan")
mobil1.set_model("Altima")
mobil1.set_tahun(2021)

print(mobil1.info())
