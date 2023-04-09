from hrac import *


def erase_by_priority(user, priority):
    """Spustí mazání ostatních karet v závislosti na zadané prioritě"""
    for x in user.hand:
        if x.erase == priority and x.activ == True and x.penalty_condition == True:
            x.erase_cards(user, x.ID, *x.effect3)


def erase(user, count):
    """postupně provede mazani podle priorit od jedné
    do počtu druhů priorit celkem"""
    priority = 1
    while priority != count + 1:
        erase_by_priority(user, f'priorita_{priorita}')
        cards_mgmt(user)
        priority += 1

def cards_mgmt(user):
    """přeseune neaktivní karty do listu pasivních karet"""
    for x in user.hand:
        if x.activ == False:
            user.hand.remove(x)
            user.hand_pasiv.append(x)
        
def pasiv_if_not(user):
    """Zneaktivní karty, které nemají specifickou kartu do páru"""
    for x in user.hand:
        if x.erase_not_if == True and x.penalty_condition == True:
            x.erase_no_color(user, x.ID, *x.effect3)
    cards_mgmt(user)
    
def pasiv_if(user):
    """Zneaktivní karty, kteréjsou blokovány jinou kartou"""
    for x in user.hand:
        if x.erase_if == True and x.penalty_condition == True:
            x.erase_if_color(user, x.ID, *x.effect3)
    cards_mgmt(user)
            
def all_activ(user):
    """Hodí všechny karty do aktivní ruky"""
    for x in user.hand_pasiv:
        user.hand.append(x)
        user.hand_pasiv.remove(x)

def active_true(user):
    """Zaktivní všechny karty na ruce"""
    for x in user.hand:
        x.activ = True

def cards_string(user):
    """převádí názvy karet na ruce na stringy
        s aktivními a vymazanými kartami"""
    user.string_hand = ""
    string_list = [str(obj) for obj in user.hand]
    separator = ", "
    user.string_hand = separator.join(string_list)
    
    user.string_hand_pasiv = ""
    string_list2 = [str(obj) for obj in user.hand_pasiv]
    separator = ", "
    user.string_hand_pasiv = separator.join(string_list2)
    
def is_it_active(user):
    """projede ruku hráče a rozdělí ruku na aktivní a pasivní karty"""
    all_activ(user)
    active_true(user)
    erase(user, 4)
    pasiv_if_not(user)
    pasiv_if(user)   
    cards_string(user)




