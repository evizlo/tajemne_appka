from seznam import seznam_typu


def bonus_karta_typ(user, ID, bonus_typ, bonus_karta, podmínka,
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
        if typ not in typy_karet_v_ruce:
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
                            
def ruzne_efekty_typu(user, podmínka, typy_karet):
    """nespecifikované bonusy"""

    if podmínka == 'přidej':
        body = [] 
        for x in user.ruka:
            if x.typ in typy_karet:
                body.append(x.body)                  
        user.bodova_hodnota_efekty += max(body)

        
def max_typ(user):
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

def postupka(user):
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

def licha_cisla(user):
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

def nestejne_typy(user):
    """zjistí zda jsou všehny typy karet na ruce rozdílné"""
    if len([x.typ for x in user.ruka]) == len(set([x.typ for x in user.ruka])):
        user.bodova_hodnota_efekty += 50

            


def plus_limit(user):
    """zvýší hráčův limit karet v ruce o jedna"""
    if user.max_limit == 7: ##- len(user.ruka) + len(user.ruka_pasiv):
        user.limit += 1
        user.max_limit += 1

def postihy_none(user):
    """Nastaví všechny postihy na None, musí být první"""
    if any('11-Ochranná runa' == x.ID for x in user.ruka):
        for x in user.ruka:
            x.postih_stav = False



def vymazani_karet(user, ID, karta = [], typ = []):
    """maže sepcifické typy, kromě specifických karet"""
    for x in user.ruka:
        if x.typ in typ and x.ID != ID and x.name not in karta:
            x.aktiv = False


def vymazani_sebe_nemas_li(user, ID, karta = [], typ = []):
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


def vymazani_sebe_mas_li(user, ID, karta = [], typ = []):   
    """vymazána pokud mám aspon jeden typ"""
    typy_karet_v_ruce = set([x.typ for x in user.ruka])
    if any(x in typy_karet_v_ruce for x in typ[1]):
        for x in user.ruka:
            if x.ID == ID:
                x.aktiv = False


def ostran_postih(user, typ):
    """nastaví všechny postihy karet na False"""
    for x in user.ruka:
        if x.typ == typ:
            x.postih_stav = False



def odstran_slovo(user, typ):
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

def odstran_slovo_ex(user, typ):
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

    
               



                        
