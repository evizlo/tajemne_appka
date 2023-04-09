from seznam import seznam_karet
from seznam import seznam_typu
from is_active import *
from misc import *
from PyQt5.QtCore import QObject, pyqtSignal
seznam_karet_použité = []
list_karet = []



class Card():

    instance = 0


    def __init__(self, name, points, color, bonus, effect, penalty, effect2,
                 erase, effect3, erase_if, erase_not_if, delete,
                 effect4, activ = True, penalty_condition = True):
        self.name = name
        self.points = points
        self.color  = color
        self.bonus = bonus
        self.effect = effect
        self.penalty = penalty
        self.effect2 = effect2
        self.erase = erase
        self.effect3 = effect3
        self.erase_if = erase_if
        self.erase_not_if = erase_not_if
        self.delete = delete
        self.effect4 = effect4
        self.activ = activ
        self.penalty_condition = penalty_condition
        self.ID = f'{Card.instance}-{name}'
        Card.instance += 1
        
    def __repr__(self):
        return self.name

    def card_bonus(self, user, ID, bonus_color, bonus_card, condition,
                    cards = [], colors = []):
        """Spočítá bonusy a postihy na kartách,
        které mají plus a mínus nějaká hodnota"""

        colors_in_hand  = set([x.color for x in user.hand])
        card_names_in_hand = [x.name for x in user.hand]



        if condition == 'plus':
            #bonus za specifickou kartu, karty, typ nebo obojí
            if colors in colors_in_hand or colors == 'bez':
                if set(karta).issubset(card_names_in_hand):
                   user.points_effects += (bonus_color + bonus_card)                  
                else:
                    user.points_effects += bonus_color

        if condition == 'plus_every':
            #za každý specifický typ plus s bonusem pokud má i specifickou kartu
            for x in user.hand:
                if x.color == colors:
                    if set(cards).issubset(card_names_in_hand):
                        user.points_effects += (bonus_color + bonus_card)
                    else:
                        user.bodova_hodnota_efekty += bonus_color
                                        

        if condition == 'nope':
            #ověřuje že nemá daný typ
            if any(color) not in card_names_in_hand:
                user.points_effects += bonus_color
            

        if condition == 'any_karta':
            #ověřuje zda má aspoň jednu kartu co je potřeba
            for x in card_names_in_hand:
                if any(x == element for element in cards):
                    user.points_effects += bonus_card
                    break

        if condition == 'any_typ':
            #ověřuje zda máš aspoň jeden typ co je potřeba
            for x in colors_in_hand:
                if any(x == element for element in colors):
                    user.points_effects += bonus_color
                    break
                    
        if condition == "every":
            #za každý další stejný nebo jiný typ a/nebo kartu
            for x in user.hand:
                if x.color in colors and x.ID != ID:
                    user.points_effects += bonus_color
            if set(cards).issubset(card_names_in_hand):
                user.points_effects += bonus_card
                
        if condition == 'součet':
            #sčíta hodnoty karet
            for x in user.hand:
                if x.color == colors:
                    user.points_effects += x.points

        if condition == 'vice_spec':
            #specifická karta společně s jinou, jinými specifickými kartami
            condition1 = set(karta[0])
            condition2 = set(karta[1])
            if condition1.issubset(card_names_in_hand):
                if any(x in card_names_in_hand for x in condition2):
                    user.points_effects += bonus_card

        if condition == 'mene_spec':
            condition1 = set(cards[0])
            condition2 = set(cards[1])
            if condition1.issubset(card_names_in_hand):
                user.points_effects += bonus_card[0]
            else:
                if any(x in card_names_in_hand for x in podminka2):
                    user.points_effects += bonus_card[1]

    def max_same_color(self, user):
        """Spočítá počet stejných typů karet pro kartu Sběratel"""
        max_count = 0
        index = 9
        while index > -1:
            color = seznam_typu[index]
            count = sum(1 for card in user.hand if karta.color == color)
            if count > max_count:
                max_count = count
            index -= 1
        if max_count > 4:
            user.points_effects += 100
        elif max_count > 3:
            user.points_effects += 40
        elif max_count > 2:
            user.points_effects += 10

    def max_points(self, user, condition, colors):
        """přidá největší základní bodovou hodnotu karty z výběru typů karet"""

        if condition == 'přidej':
            points = [] 
            for x in user.ruka:
                if x.color in colors:
                    points.append(x.points)                  
            user.points_effects += max(points)

    def sequence(self, user):
        """Spočíta sekvence základních bodových hodnot pro krystal řádu"""
        max_count = 1
        current_count = 1
        sorted_cards = sorted(user.hand, key=lambda card: card.body)
        for i in range(1, len(sorted_cards)):
            if sorted_cards[i].points == sorted_cards[i-1].points + 1:
                current_count += 1
                max_count = max(max_count, current_count)
            elif sorted_cards[i].points == sorted_cards[i-1].points:
                current_count += 0
                max_count = max(max_count, current_count)
            else:
                current_count = 1
        points = {8 : 150, 7 : 150, 6 : 100, 5 : 60, 4 : 30, 3: 10}
        if max_count > 2:
            user.points_effects += points[max_count]

    def odd_points(self, user):
        """počítá liché základní hodnoty karet"""
        not_even = True
        all_points = -3
        for x in user.hand:
            if x.points % 2 == 1:
                all_points += 3
            else:
                not_even = False
        if not_even == True:
            user.points_effects += 50
        else:
            user.points_effects += all_points

    def defferent_colors(self, user):
        """zjistí zda jsou všehny typy karet na ruce rozdílné"""
        if len([x.color for x in user.hand]) == len(set([x.color for x in user.hand])):
            user.points_effects += 50

    def plus_limit(self, user):
        """zvýší hráčův limit karet v ruce o jedna"""
        if user.max_limit == 7: 
            user.limit += 1
            user.max_limit += 1

    def penalty_off_all(self, user):
        """Nastaví všechny postihy na False, musí být první"""
        if any('11-Ochranná runa' == x.ID for x in user.hand):
            for x in user.hand:
                x.penalty_condition = False

    def erase_cards(self, user, ID, cards = [], colors = []):
        """maže sepcifické typy, kromě specifických karet"""
        for x in user.hnad:
            if x.color in colors and x.ID != ID and x.name not in cards:
                x.activ = False

    def erase_no_color(self, user, ID, cards = [], colors = []):
        """vymazána nemáš li alespon jedn typ"""
        colors_in_hand = set([x.color for x in user.hand])
        if any(x in colors_in_hand for x in colors[0]):
            for x in user.hand:
                if x.ID == ID:
                    x.activ = True
        else:
            for x in user.hand:
                if x.ID == ID:
                    x.activ = False

    def erase_if_color(self, user, ID, cards = [], colors = []):   
        """vymazána pokud mám aspon jeden typ"""
        colors_in_hand = set([x.color for x in user.hand])
        if any(x in colors_in_hand for x in colors[1]):
            for x in user.hnad:
                if x.ID == ID:
                    x.activ = False

    def penalty_off(self, user, color):
        """nastaví všechny postihy karet na False"""
        for x in user.hand:
            if x.color == color:
                x.penalty_condition = False

    def erase_color(self, user, color):
        """vymaze zadaný typ ze všech postihu karet"""
        for x in user.hand:
            if x.effect2 != None: 
                if color in x.effect2[4] and x.name != "Požár":
                    x.effect2[4].remove(color)
            if x.effect3 != None:
                if x.name == "Bojová vzducholoď":
                    pass
                else:
                    if color in x.effect3[1] and x.name != "Požár":
                        x.effect3[1].remove(color)

    def erase_color_ex(self, user, color):
        """vymaze zadaný typ ze všech postihu karet
            specifického druhu"""
        for x in user.hand:
            if x.color == color[0]:
                if x.effect2 != None: 
                    if color in x.effect2[4] and x.name != "Požár":
                        x.effect2[4].remove(color[1])
                if x.effect3 != None:
                    if color in x.effect3[1] and x.name != "Požár":
                        x.effect3[1].remove(color[1])



class Player(QObject):

    players = 0
    points_all_changed = pyqtSignal(int)
    limit_change = pyqtSignal(int)
    max_limit_change = pyqtSignal(int)
    cards_hand_change = pyqtSignal(int)
    string_hand_change = pyqtSignal(str)
    string_hand_pasiv_change = pyqtSignal(str)
    
    
    def __init__(self,jmeno_hrace):
        super().__init__()
        self.player_name = player_name
        self.limit = 7
        self.max_limit = 7
        self.hand = []
        self.hand_pasiv = []
        self.string_hand = ""
        self.string_hand_pasiv= ""
        self.points = 0
        self.points_effects = 0
        self.points_all = 0
        Player.players += 1
        self.cards_hand = len(self.hand) + len(self.hand_pasiv)

    @property
    def string_hand_pasiv(self):
        return self._string_hand

    @string_hand_pasiv.setter
    def string_ruka_pasiv(self, value):
        self._string_hand_pasiv = value
        self.string_hand_pasiv_change.emit(value)

        

    @property
    def string_hand(self):
        return self._string_hand

    @string_hand.setter
    def string_hand(self, value):
        self._string_hand = value
        self.string_hand_change.emit(value)

        
    @property
    def points_all(self):
        return self._points_all

    @points_all.setter
    def points_all(self, value):
        self._points_all = value
        self.poins_all_changed.emit(value)

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
        return self.player_name

    def add_card(self, name):
        new = list_karet[ind(name)]
        if nova in seznam_karet_použité or self.limit == 0:        
            print("Nelze přidat")
        else:
            self.limit -= 1 ##sníží o jedna
            seznam_karet_použité.append(new) ##hodí novou kartu do použitých
            
            self.hand.append(new)## hodí novou kartu na ruku
 
            spocitej_body(self)
            spocitej_body(self)
            
            
            
    def remove_card(self, name):
        card = list_karet[ind(name)]
        index = list_karet.index(card)
        self.limit += 1
        if card in self.hand:
            self.hand.remove(card)
        else:
            self.hand_pasiv.remove(card)
        seznam_karet_použité.remove(card)
        recovery(self, card, index)
        is_it_active(self)
        spocitej_body(self)

    def reset(self):
        """resetuje hráče do stavu bez karet a
            obnoví všechny atributy karet"""
        for x in self.hand:
            self.remove_card(x.name)
        for x in self.hand_pasiv:
            self.remove_card(x.name)
        self.limit = 7
        self.max_limit = 7
        self.hand = []
        self.hand_pasiv = []
        self.string_hand = ""
        self.string_hand_pasiv= ""
        self.points = 0
        self.points_effects = 0
        self.points_all = 0
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
        

list_karet = [Card(card['name'], card['body'], card['typ'],
                          card.get('bonus'), card.get('efekt'),
                          card.get('postih'), card.get('efekt2'),
                          card.get('mazani'), card.get('efekt3'),
                          card.get('vymaz_masli'), card.get('vymaz_nemasli'),
                          card.get('odstran'), card.get('efekt4')                           
                          ) for card in seznam_karet]


