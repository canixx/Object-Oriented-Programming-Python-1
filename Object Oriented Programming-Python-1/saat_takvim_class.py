# Örnek 
# Saat ve Takvim olarak 2 sınıfımız olsun
# Saatli takvim iksinden de kalıtım alacak

class Saat:
    """Saati simüle eder"""
    def __init__(self,saat,dakika,saniye):
        self.__saat=saat
        self.__dakika=dakika
        self.__saniye=saniye


    def saati_kur(self,saat,dakika,saniye):
        self.__saat=saat
        self.__dakika=dakika
        self.__saniye=saniye


    def saat_kac(self):
        return "{0}:{1}:{2}".format(self.__saat,self.__dakika,self.__saniye)

print("---------------SAAT------------------")



clock = Saat(0,0,0)

print(clock.saat_kac())     # DENEME
clock.saati_kur(10,4,28)
print(clock.saat_kac())
print("saat:",clock._Saat__dakika)


class Takvim:
    def __init__(self,d,m,y):
        self.takvim_kur(d,m,y)


    def takvim_kur(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y

    def bugun_ne(self):
        return "{0}:{1}:{2}".format(self.d,self.m,self.y)    

print("----------TAKVİM-------------")

takvim = Takvim(6,11,2019)
print(takvim.d)                # DENEME
print(takvim.bugun_ne())


# Saatli Takvim Classı oluşturma

class Saatli_Takvim(Saat,Takvim):
    """
    Saat ve takvimi beraber tutar.
    """
    def __init__(self,gun,ay,yil,saat,dakika,saniye):
        Saat.__init__(self,saat,dakika,saniye)
        Takvim.__init__(self,gun,ay,yil)

print("------------------SAATLİ TAKVİM-------------")

saatli_takvim= Saatli_Takvim(8,12,2020,16,45,7)
print(saatli_takvim.saat_kac())
print(saatli_takvim.bugun_ne())







