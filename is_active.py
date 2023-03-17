from funkce_karet import *


def mazani_podle_priority(user, priorita):
    """Spustí mazání ostatních karet v závislosti na zadané prioritě"""
    for x in user.ruka:
        if x.mazani == priorita and x.aktiv == True and x.postih_stav == True:
            vymazani_karet(user, x.ID, *x.efekt3)


def mazani_karet(user, pocet):
    """postupně provede mazani podle priorit od jedné
    do počtu druhů priorit celkem"""
    priorita = 1
    while priorita != pocet + 1:
        mazani_podle_priority(user, f'priorita_{priorita}')
        sprava_karet(user)
        priorita += 1

def sprava_karet(user):
    """přeseune neaktivní karty do listu pasivních karet"""
    for x in user.ruka:
        if x.aktiv == False:
            user.ruka.remove(x)
            user.ruka_pasiv.append(x)
        
def vymazani_nemas(user):
    """Zneaktivní karty, které nemají specifickou kartu do páru"""
    for x in user.ruka:
        if x.vymaz_nemasli == True and x.postih_stav == True:
            vymazani_sebe_nemas_li(user, x.ID, *x.efekt3)
    sprava_karet(user)
    
def vymazani_mas(user):
    """Zneaktivní karty, kteréjsou blokovány jinou kartou"""
    for x in user.ruka:
        if x.vymaz_masli == True and x.postih_stav == True:
            vymazani_sebe_mas_li(user, x.ID, *x.efekt3)
    sprava_karet(user)
            
def obnova(user):
    """Hodí všechny karty do aktivní ruky"""
    for x in user.ruka_pasiv:
        user.ruka.append(x)
        user.ruka_pasiv.remove(x)

def aktive_true(user):
    """Zaktivní všechny karty na ruce"""
    for x in user.ruka:
        x.aktiv = True

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
    
def is_it_active(user):
    """projede ruku hráče a rozdělí ruku na aktivní a pasivní karty"""
    obnova(user)
    aktive_true(user)
    mazani_karet(user, 4)
    vymazani_nemas(user)
    vymazani_mas(user)   
    stringy_karet(user)




