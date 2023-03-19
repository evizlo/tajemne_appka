from seznam import seznam_karet
from seznam import seznam_typu
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

    def bonus_karta_typ(self, user, ID, bonus_typ, bonus_karta, podmínka,
                    karta = [],typ = []):
        """Spočítá bonusy a postihy na kartách,
        které mají plus a mínus nějaká hodnota"""

        typy_karet_v_ruce  = set([x.typ for x in user.ruka])
        jmena_karet_v_ruce = [x.name for x in user.ruka]



        if podmínka == 'plus':
            #bonus za specifickou kartu, karty, typ nebo obojí
            if typ in typy_karet_v_ruce or typ == 'bez':
                if set(karta).issubset(jmena_karet_v_ruce):
                   user.bodova_hodnota_efekty += (bonus_typ + bonus_karta)                  
                else:
                    user.bodova_hodnota_efekty += bonus_typ

        if podmínka == 'plus_every':
            #za každý specifický typ plus s bonusem pokud má i specifickou kartu
            for x in user.ruka:
                if x.typ == typ:
                    if set(karta).issubset(jmena_karet_v_ruce):
                        user.bodova_hodnota_efekty += (bonus_typ + bonus_karta)
                    else:
                        user.bodova_hodnota_efekty += bonus_typ
                                        

        if podmínka == 'nope':
            #ověřuje že nemá daný typ
            if any(typ) not in typy_karet_v_ruce:
                user.bodova_hodnota_efekty += bonus_typ
            

        if podmínka == 'any_karta':
            #ověřuje zda má aspoň jednu kartu co je potřeba
            for x in jmena_karet_v_ruce:
                if any(x == prvek for prvek in karta):
                    user.bodova_hodnota_efekty += bonus_karta
                    break

        if podmínka == 'any_typ':
            #ověřuje zda máš aspoň jeden typ co je potřeba
            for x in typy_karet_v_ruce:
                if any(x == prvek for prvek in typ):
                    user.bodova_hodnota_efekty += bonus_typ
                    break
                    
        if podmínka == "every":
            #za každý další stejný nebo jiný typ a/nebo kartu
            for x in user.ruka:
                if x.typ in typ and x.ID != ID:
                    user.bodova_hodnota_efekty += bonus_typ
            if set(karta).issubset(jmena_karet_v_ruce):
                user.bodova_hodnota_efekty += bonus_karta
                
        if podmínka == 'součet':
            #sčíta hodnoty karet
            for x in user.ruka:
                if x.typ == typ:
                    user.bodova_hodnota_efekty += x.body

        if podmínka == 'vice_spec':
            #specifická karta společně s jinou, jinými specifickými kartami
            podminka1 = set(karta[0])
            podminka2 = set(karta[1])
            if podminka1.issubset(jmena_karet_v_ruce):
                if any(x in jmena_karet_v_ruce for x in podminka2):
                    user.bodova_hodnota_efekty += bonus_karta

        if podmínka == 'mene_spec':
            podminka1 = set(karta[0])
            podminka2 = set(karta[1])
            if podminka1.issubset(jmena_karet_v_ruce):
                user.bodova_hodnota_efekty += bonus_karta[0]
            else:
                if any(x in jmena_karet_v_ruce for x in podminka2):
                    user.bodova_hodnota_efekty += bonus_karta[1]

    def max_typ(self, user):
        """Spočítá počet stejných typů karet pro kartu Sběratel"""
        max_count = 0
        index = 9
        while index > -1:
            typ = seznam_typu[index]
            count = sum(1 for karta in user.ruka if karta.typ == typ)
            if count > max_count:
                max_count = count
            index -= 1
        if max_count > 4:
            user.bodova_hodnota_efekty += 100
        elif max_count > 3:
            user.bodova_hodnota_efekty += 40
        elif max_count > 2:
            user.bodova_hodnota_efekty += 10

    def max_hodnota(self, user, podmínka, typy_karet):
        """přidá největší základní bodovou hodnotu karty z výběru typů karet"""

        if podmínka == 'přidej':
            body = [] 
            for x in user.ruka:
                if x.typ in typy_karet:
                    body.append(x.body)                  
            user.bodova_hodnota_efekty += max(body)

    def postupka(self, user):
        """Spočíta sekvence základních bodových hodnot pro krystal řádu"""
        max_count = 1
        current_count = 1
        serazene_karty = sorted(user.ruka, key=lambda karta: karta.body)
        for i in range(1, len(serazene_karty)):
            if serazene_karty[i].body == serazene_karty[i-1].body + 1:
                current_count += 1
                max_count = max(max_count, current_count)
            elif serazene_karty[i].body == serazene_karty[i-1].body:
                current_count += 0
                max_count = max(max_count, current_count)
            else:
                current_count = 1
        body = {8 : 150, 7 : 150, 6 : 100, 5 : 60, 4 : 30, 3: 10}
        if max_count > 2:
            user.bodova_hodnota_efekty += body[max_count]

    def licha_cisla(self, user):
        """počítá liché základní hodnoty karet"""
        not_even = True
        součet_bodu = -3
        for x in user.ruka:
            if x.body % 2 == 1:
                součet_bodu += 3
            else:
                not_even = False
        if not_even == True:
            user.bodova_hodnota_efekty += 50
        else:
            user.bodova_hodnota_efekty += součet_bodu

    def nestejne_typy(self, user):
        """zjistí zda jsou všehny typy karet na ruce rozdílné"""
        if len([x.typ for x in user.ruka]) == len(set([x.typ for x in user.ruka])):
            user.bodova_hodnota_efekty += 50

    def plus_limit(self, user):
        """zvýší hráčův limit karet v ruce o jedna"""
        if user.max_limit == 7: 
            user.limit += 1
            user.max_limit += 1

    def postihy_none(self, user):
        """Nastaví všechny postihy na None, musí být první"""
        if any('11-Ochranná runa' == x.ID for x in user.ruka):
            for x in user.ruka:
                x.postih_stav = False

    def vymazani_karet(self, user, ID, karta = [], typ = []):
        """maže sepcifické typy, kromě specifických karet"""
        for x in user.ruka:
            if x.typ in typ and x.ID != ID and x.name not in karta:
                x.aktiv = False

    def vymazani_sebe_nemas_li(self, user, ID, karta = [], typ = []):
        """vymazána nemáš li alespon jedn typ"""
        typy_karet_v_ruce = set([x.typ for x in user.ruka])
        if any(x in typy_karet_v_ruce for x in typ[0]):
            for x in user.ruka:
                if x.ID == ID:
                    x.aktiv = True
        else:
            for x in user.ruka:
                if x.ID == ID:
                    x.aktiv = False

    def vymazani_sebe_mas_li(self, user, ID, karta = [], typ = []):   
        """vymazána pokud mám aspon jeden typ"""
        typy_karet_v_ruce = set([x.typ for x in user.ruka])
        if any(x in typy_karet_v_ruce for x in typ[1]):
            for x in user.ruka:
                if x.ID == ID:
                    x.aktiv = False

    def ostran_postih(self, user, typ):
        """nastaví všechny postihy karet na False"""
        for x in user.ruka:
            if x.typ == typ:
                x.postih_stav = False

    def odstran_slovo(self, user, typ):
        """vymaze zadaný typ ze všech postihu karet"""
        for x in user.ruka:
            if x.efekt2 != None: 
                if typ in x.efekt2[4] and x.name != "Požár":
                    x.efekt2[4].remove(typ)
            if x.efekt3 != None:
                if x.name == "Bojová vzducholoď":
                    pass
                else:
                    if typ in x.efekt3[1] and x.name != "Požár":
                        x.efekt3[1].remove(typ)

    def odstran_slovo_ex(self, user, typ):
        """vymaze zadaný typ ze všech postihu karet
            specifického druhu"""
        for x in user.ruka:
            if x.typ == typ[0]:
                if x.efekt2 != None: 
                    if typ in x.efekt2[4] and x.name != "Požár":
                        x.efekt2[4].remove(typ[1])
                if x.efekt3 != None:
                    if typ in x.efekt3[1] and x.name != "Požár":
                        x.efekt3[1].remove(typ[1])



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

        

    @property
    def string_ruka(self):
        return self._string_ruka

    @string_ruka.setter
    def string_ruka(self, value):
        self._string_ruka = value
        self.string_ruka_change.emit(value)

        
    @property
    def bodova_hodnota_celek(self):
        return self._bodova_hodnota_celek

    @bodova_hodnota_celek.setter
    def bodova_hodnota_celek(self, value):
        self._bodova_hodnota_celek = value
        self.bodova_hodnota_celek_changed.emit(value)

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
        self.limit_change.emit(value)

    @property
    def max_limit(self):
        return self._max_limit

    @max_limit.setter
    def max_limit(self, value):
        self._max_limit = value
        self.max_limit_change.emit(value)
        


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

def ind(name):
    """vrátí index objektu v list_karet podle atributu name"""
    from hrac import list_karet
    cont = True
    index = 0
    while cont == True:
        if list_karet[index].name.lower() != name.lower():
            index +=1
        else:
            cont = False
    return index
        

list_karet = [Karta(karta['name'], karta['body'], karta['typ'],
                          karta.get('bonus'), karta.get('efekt'),
                          karta.get('postih'), karta.get('efekt2'),
                          karta.get('mazani'), karta.get('efekt3'),
                          karta.get('vymaz_masli'), karta.get('vymaz_nemasli'),
                          karta.get('odstran'), karta.get('efekt4')                           
                          ) for karta in seznam_karet]


