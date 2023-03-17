#from hrac import card_states
from funkce_karet import *
from is_active import *
from seznam_2 import seznam_karet_2
from seznam import seznam_karet
from hrac import *
import copy




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
    from hrac import list_karet
    from hrac import ind
    for x in user.ruka:
        karta = list_karet[ind(x.name)]
        index = list_karet.index(karta)
        recovery(user, karta, index)
        

def spocitej_body(user):
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
            postupka(user)
        if x.bonus == 'bkt':
            bonus_karta_typ(user, x.ID, *x.efekt)
        if x.postih == 'bkt' and x.postih_stav == True:
            bonus_karta_typ(user, x.ID, *x.efekt2)
        if x.bonus == 'ret':
            ruzne_efekty_typu(user, *x.efekt)
        if x.bonus == 'mt':
            max_typ(user)
        if x.bonus == 'pl':
            plus_limit(user)
        if x.bonus == 'lc':
            licha_cisla(user)
        if x.bonus == 'nt':
            nestejne_typy(user)
    user.bodova_hodnota_celek = (user.bodova_hodnota +
                                user.bodova_hodnota_efekty)

def postihy_ostraneni(user):
    for x in user.ruka:
        if x.odstran == 'odstr':
            ostran_postih(user, x.efekt4)
        if x.odstran == 'slovo':
            odstran_slovo(user, x.efekt4)
        if x.odstran == 'exclusive':
            odstran_slovo_ex(user, x.efekt4)
            
        
            
            







        
    

    
