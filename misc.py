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
    """obnoví atributy všech karet na ruce"""
    from hrac import list_karet
    from hrac import ind
    for x in user.ruka:
        karta = list_karet[ind(x.name)]
        index = list_karet.index(karta)
        recovery(user, karta, index)
        

def spocitej_body(user):
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
    """odstraní postihy podle ruzných požadavků"""
    for x in user.ruka:
        if x.odstran == 'odstr':
            ostran_postih(user, x.efekt4)
        if x.odstran == 'slovo':
            odstran_slovo(user, x.efekt4)
        if x.odstran == 'exclusive':
            odstran_slovo_ex(user, x.efekt4)


        
def ind(name):
    """vrátí index objektu v list_karet podle atributu name"""
    cont = True
    index = 0
    while cont == True:
        if list_karet[index].name.lower() != name.lower():
            index +=1
        else:
            cont = False
    return index


def stringy_karet(user):
    """převádí názvy karet na ruce na stringy
        s aktivními a vymazanými kartami"""
    user.string_ruka = ""
    string_list = [str(obj) for obj in user.ruka]
    separator = ", "
    user.string_ruka = separator.join(string_list)
    
    user.string_ruka_pasiv = ""
    string_list2 = [str(obj) for obj in user.ruka_pasiv]
    separator = ", "
    user.string_ruka_pasiv = separator.join(string_list2)
    

            
        
            
            







        
    

    
