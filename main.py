from seznam import seznam_karet
from seznam import seznam_typu
from hrac   import Hrac
from hrac  import seznam_karet_použité
from hrac import list_karet
from hrac import ind as ind
from věci import bonus_karta_typ as bkt
from věci import ruzne_efekty_typu as ret
from věci import max_typ as mt
from věci import plus_limit as pl
from misc import *
import random



#print(list_karet)

user1 = Hrac("David")
user2 = Hrac("Nikča")
user3 = Hrac("Lereoy")


def pridavej(user):
    while user.limit > 0:
        user.pridani_karty_s_porovnanim(input("Jakou kartu chcete přidat?\n"))
##
####oheň
##        
##user1.pridat_kartu("Svíčka")
##user1.pridat_kartu("Blesk")
##user1.pridat_kartu("Požár")
##user1.pridat_kartu("Kovárna")
##user1.pridat_kartu("Elementál ohně")
##
####zbraň
##
##user1.pridat_kartu("Elfský luk")
##user1.pridat_kartu("Kethský meč")
#user1.pridat_kartu("Bojová vzducholoď")
##user1.pridat_kartu("Magická hůl")
##user1.pridat_kartu("Válečná loď")
##
####artefakt
##
##user1.pridat_kartu("Kniha proměn")
##user1.pridat_kartu("Ochranná runa")
##user1.pridat_kartu("Strom světa")
##user1.pridat_kartu("Kethský štít")
##user1.pridat_kartu("Krystal řádu")
####
####armáda
##
##user1.pridat_kartu("Trpasličí pěchota")
##user1.pridat_kartu("Těžká jízda")
##user1.pridat_kartu("Hraničáři")
##user1.pridat_kartu("Rytířky")
##user1.pridat_kartu("Elfí lučištníci")
##
####vůdce
##user1.pridat_kartu("Velitel")
##user1.pridat_kartu("Princezna")
##user1.pridat_kartu("Císařovna")
##user1.pridat_kartu("Královna")
##user1.pridat_kartu("Král")
##
####počasí
##
##user1.pridat_kartu("Bouře")
##user1.pridat_kartu("Tornádo")
##user1.pridat_kartu("Sněhová vánice")
#user1.pridat_kartu("Kouř")
##user1.pridat_kartu("Elementál vzduchu")
##
####země
##
##user1.pridat_kartu("Les")
##user1.pridat_kartu("Hora")
##user1.pridat_kartu("Jeskyně")
##user1.pridat_kartu("Zvonice")
##user1.pridat_kartu("Elementál země")
##
####potopa
##
##user1.pridat_kartu("Elementál vody")
#user1.pridat_kartu("Fontána života")
##user1.pridat_kartu("Stoletá voda")
##user1.pridat_kartu("Ostrov")
##user1.pridat_kartu("Bažina")
##
####tvor
##
##user1.pridat_kartu("Válečný oř")
##user1.pridat_kartu("Drak")
##user1.pridat_kartu("Bazilišek")
##user1.pridat_kartu("Jednorožec")
##user1.pridat_kartu("Hydra")
##
####čaroděj
##user1.pridat_kartu("Sběratel")
##user1.pridat_kartu("Kouzelnice")
##user1.pridat_kartu("Nekromant")
##user1.pridat_kartu("Nejvyšší mág")
##user1.pridat_kartu("Pán šelem")
##user1.pridat_kartu("Šašek")

#print(user1.bodová_hodnota_celek)
#user1.spocitej_body()
#print(user1.bodová_hodnota_celek)

##user1.pridat_kartu("Bojová vzducholoď")user1.pridat_kartu("Hraničáři")
##user1.pridat_kartu("Blesk")
##user1.pridat_kartu("Kouř")
##user1.pridat_kartu("Stoletá voda")
##user1.pridat_kartu("Bouře")
##user1.pridat_kartu('bazilišek')
##user1.pridat_kartu('požár')
##user1.pridat_kartu("Bojová vzducholoď")
##user1.pridat_kartu("Těžká jízda")
##user1.pridat_kartu("Hraničáři")
##print(user1.ruka)
##print(user1.ruka_pasiv)

##probléééééém
##Těžká jízda
##Požár
##Kouř
##Bouře
##Bazilišek
##Bojová vzducholoď
##Stoletá voda


###problém2
##Bazilišek
##Požár
##Těžká jízda
##Bojová vzducholoď
##Kouř
##Stoletá voda
##Bouře

##problééééééém
##Bazilišek
##Stoletá voda
##Požár
##Bojová vzducholoď
##Sněhová vánice
##Kouř
##Bouře

##user1.pridat_kartu("Těžká jízda")
##user1.pridat_kartu('požár')
##user1.pridat_kartu("Kouř")
##user1.pridat_kartu("Bouře")
##user1.pridat_kartu('bazilišek')
##user1.pridat_kartu("Bojová vzducholoď")
##user1.pridat_kartu("Stoletá voda")

##user1.pridat_kartu('bazilišek')
##user1.pridat_kartu('požár')
##
##user1.pridat_kartu("Těžká jízda")
##user1.pridat_kartu("Bojová vzducholoď")
##user1.pridat_kartu("Kouř")
##user1.pridat_kartu("Stoletá voda")
##user1.pridat_kartu("Bouře")

##user1.pridat_kartu('bazilišek')
##user1.pridat_kartu("Stoletá voda")
##user1.pridat_kartu('požár')
##user1.pridat_kartu("Bojová vzducholoď")
##user1.pridat_kartu("sněhová vánice")
##user1.pridat_kartu("Kouř")
##user1.pridat_kartu("Bouře")
#user1.pridat_kartu("Pán šelem")
#user1.pridat_kartu("Bazilišek")

##user1.pridat_kartu("Elfí lučištníci")
##user1.pridat_kartu("Hraničáři")
user1.pridat_kartu("Kethský štít")
##        
user1.pridat_kartu("Kethský meč")

##user1.pridat_kartu("Pán šelem")
x = ["Kouř", "Stoletá voda", "Bouře", 'bazilišek', 'požár',
     "Bojová vzducholoď", "Sněhová vánice"]

def nahodne_pridavani(parametry):
    random.shuffle(parametry)
    for x in parametry:
        user1.pridat_kartu(x)

from hrac import card_states
#nahodne_pridavani(x)
        
print(user1.ruka)
print(user1.ruka_pasiv)
 
                  
