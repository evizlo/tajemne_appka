from seznam import seznam_karet
from funkce_karet import *
from is_active import *
from misc import *
from PyQt5.QtCore import QObject, pyqtSignal
seznam_karet_použité = []
list_karet = []



class Karta():

    instancí = 0


    def __init__(self, name, body, typ, bonus, efekt, postih, efekt2,
                 mazani, efekt3, vymaz_masli, vymaz_nemasli, odstran,
                 efekt4, aktiv = True, postih_stav = True):
        self.name = name
        self.body = body
        self.typ  = typ
        self.bonus = bonus
        self.efekt = efekt
        self.postih = postih
        self.efekt2 = efekt2
        self.mazani = mazani
        self.efekt3 = efekt3
        self.vymaz_masli = vymaz_masli
        self.vymaz_nemasli = vymaz_nemasli
        self.odstran = odstran
        self.efekt4 = efekt4
        self.aktiv = aktiv
        self.postih_stav = postih_stav
        self.ID = f'{Karta.instancí}-{name}'
        Karta.instancí += 1
        
    def __repr__(self):
        return self.name
        


class Hrac(QObject):

    počet_hráčů = 0
    bodova_hodnota_celek_changed = pyqtSignal(int)
    limit_change = pyqtSignal(int)
    max_limit_change = pyqtSignal(int)
    karet_ruka_change = pyqtSignal(int)
    string_ruka_change = pyqtSignal(str)
    string_ruka_pasiv_change = pyqtSignal(str)
    
    
    def __init__(self,jmeno_hrace):
        super().__init__()
        self.jmeno_hrace = jmeno_hrace
        self.limit = 7
        self.max_limit = 7
        self.ruka = []
        self.ruka_pasiv = []
        self.string_ruka = ""
        self.string_ruka_pasiv= ""
        self.bodova_hodnota = 0
        self.bodova_hodnota_efekty = 0
        self.bodova_hodnota_celek = 0
        Hrac.počet_hráčů += 1
        self.karet_ruka = len(self.ruka) + len(self.ruka_pasiv)

    @property
    def string_ruka_pasiv(self):
        return self._string_ruka

    @string_ruka_pasiv.setter
    def string_ruka_pasiv(self, value):
        self._string_ruka_pasiv = value
        self.string_ruka_pasiv_change.emit(value)
        print(value)

        

    @property
    def string_ruka(self):
        return self._string_ruka

    @string_ruka.setter
    def string_ruka(self, value):
        self._string_ruka = value
        self.string_ruka_change.emit(value)
        print(value)

        
    @property
    def bodova_hodnota_celek(self):
        return self._bodova_hodnota_celek

    @bodova_hodnota_celek.setter
    def bodova_hodnota_celek(self, value):
        self._bodova_hodnota_celek = value
        self.bodova_hodnota_celek_changed.emit(value)
        print(value)

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
        self.limit_change.emit(value)
        print(value)

    @property
    def max_limit(self):
        return self._max_limit

    @max_limit.setter
    def max_limit(self, value):
        self._max_limit = value
        self.max_limit_change.emit(value)
        print(value)
        


    def __repr__(self):
        return self.jmeno_hrace

    def pridat_kartu(self, name):
        nova = list_karet[ind(name)]
        if nova in seznam_karet_použité or self.limit == 0:        
            print("Nelze přidat")
        else:
            self.limit -= 1 ##sníží o jedna
            seznam_karet_použité.append(nova) ##hodí novou kartu do použitých
            
            self.ruka.append(nova)## hodí novou kartu na ruku
 
            spocitej_body(self)
            spocitej_body(self)
            
            
            
    def odebrat_kartu(self, name):
        karta = list_karet[ind(name)]
        index = list_karet.index(karta)
        self.limit += 1
        if karta in self.ruka:
            self.ruka.remove(karta)
        else:
            self.ruka_pasiv.remove(karta)
        seznam_karet_použité.remove(karta)
        recovery(self, karta, index)
        is_it_active(self)
        spocitej_body(self)

    def reset(self):
        """resetuje hráče do stavu bez karet a
            obnoví všechny atributy karet"""
        for x in self.ruka:
            self.odebrat_kartu(x.name)
        for x in self.ruka_pasiv:
            self.odebrat_kartu(x.name)
        self.limit = 7
        self.max_limit = 7
        self.ruka = []
        self.ruka_pasiv = []
        self.string_ruka = ""
        self.string_ruka_pasiv= ""
        self.bodova_hodnota = 0
        self.bodova_hodnota_efekty = 0
        self.bodova_hodnota_celek = 0
        seznam_karet_použité.clear()
        

list_karet = [Karta(karta['name'], karta['body'], karta['typ'],
                          karta.get('bonus'), karta.get('efekt'),
                          karta.get('postih'), karta.get('efekt2'),
                          karta.get('mazani'), karta.get('efekt3'),
                          karta.get('vymaz_masli'), karta.get('vymaz_nemasli'),
                          karta.get('odstran'), karta.get('efekt4')                           
                          ) for karta in seznam_karet]


