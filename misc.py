from is_active import *
from seznam_2 import seznam_karet_2
from seznam import seznam_karet
from hrac import *
import copy
#from hrac import Karta




def recovery(user, karta, index):
    """obnoví atributy vrácené karty"""
    novy_seznam = copy.deepcopy(seznam_karet_2)

    if karta.efekt2 != None:
        karta.efekt2 = novy_seznam[index]['efekt2']

    if karta.efekt3 != None:
        karta.efekt3 = novy_seznam[index]['efekt3']


    karta.aktiv = True
    karta.postih_stav = True

def recovery_ruka(user):
    """obnoví atributy všech karet na ruce"""
    from hrac import list_karet
    from hrac import ind
    for x in user.ruka:
        karta = list_karet[ind(x.name)]
        index = list_karet.index(karta)
        recovery(user, karta, index)
        

def spocitej_body(user):
    from is_active import obnova
    """spočítá body třídě Hrac a ošetří aktivní status karty"""
    user.bodova_hodnota_efekty = 0
    user.bodova_hodnota = 0
    user.bodova_hodnota_celek = 0

    obnova(user); aktive_true(user)
    recovery_ruka(user)
    postihy_none(user)
    postihy_ostraneni(user)
    is_it_active(user)      
        
        
    for x in user.ruka:
        user.bodova_hodnota += x.body 
        if x.bonus == 'post':
            x.postupka(user)
        if x.bonus == 'bkt':
            x.bonus_karta_typ(user, x.ID, *x.efekt)
        if x.postih == 'bkt' and x.postih_stav == True:
            x.bonus_karta_typ(user, x.ID, *x.efekt2)
        if x.bonus == 'ret':
            x.max_hodnota(user, *x.efekt)
        if x.bonus == 'mt':
            x.max_typ(user)
        if x.bonus == 'pl':
            x.plus_limit(user)
        if x.bonus == 'lc':
            x.licha_cisla(user)
        if x.bonus == 'nt':
            x.nestejne_typy(user)
    user.bodova_hodnota_celek = (user.bodova_hodnota +
                                user.bodova_hodnota_efekty)

def postihy_ostraneni(user):
    """odstraní postihy podle ruzných požadavků"""
    for x in user.ruka:
        if x.odstran == 'odstr':
            x.ostran_postih(user, x.efekt4)
        if x.odstran == 'slovo':
            x.odstran_slovo(user, x.efekt4)
        if x.odstran == 'exclusive':
            x.odstran_slovo_ex(user, x.efekt4)

def postihy_none(user):
    """Nastaví všechny postihy na None, musí být první"""
    if any('11-Ochranná runa' == x.ID for x in user.ruka):
        for x in user.ruka:
            x.postih_stav = False



            







        
    

    
