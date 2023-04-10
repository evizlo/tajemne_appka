from cards_stats import cards_stats
from cards_stats import suits_list
from is_active import *
from misc import *
from PyQt5.QtCore import QObject, pyqtSignal
used_cards = []
cards_list = []



class Card():

    instance = 0


    def __init__(self, name, value, suit, bonus, effect, penalty, effect2,
                 erase, effect3, erase_if, erase_not_if, delete,
                 effect4, activ = True, penalty_condition = True):
        self.name = name
        self.value = value
        self.suit  = suit
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

    def card_bonus(self, user, ID, bonus_suit, bonus_card, condition,
                    cards = [], suits = []):
        """Calculates bonuses and penalties on cards,
        which have plus and minus some value"""

        suits_in_hand  = set([x.suit for x in user.hand])
        card_names_in_hand = [x.name for x in user.hand]



        if condition == 'plus':
            #bonus for a specific card, cards, type or both
            if suits in suits_in_hand or suits == 'bez':
                if set(cards).issubset(card_names_in_hand):
                   user.points_effects += (bonus_suit + bonus_card)                  
                else:
                    user.points_effects += bonus_suit

        if condition == 'plus_every':
            #for each specific type plus with a bonus if he also has a specific card
            for x in user.hand:
                if x.suit == suits:
                    if set(cards).issubset(card_names_in_hand):
                        user.points_effects += (bonus_suit + bonus_card)
                    else:
                        user.bodova_hodnota_efekty += bonus_suit
                                        

        if condition == 'nope':
            #verifies that it does not have the given suit
            if any(suits) not in card_names_in_hand:
                user.points_effects += bonus_suit
            

        if condition == 'any_card':
            #verifies that it has at least one card that is needed
            for x in card_names_in_hand:
                if any(x == element for element in cards):
                    user.points_effects += bonus_card
                    break

        if condition == 'any_suit':
            #verifies whether you have at least one suit of what is needed
            for x in suits_in_hand:
                if any(x == element for element in suits):
                    user.points_effects += bonus_suit
                    break
                    
        if condition == "every":
            #for each additional same suit and/or specific card
            for x in user.hand:
                if x.suit in suits and x.ID != ID:
                    user.points_effects += bonus_suit
            if set(cards).issubset(card_names_in_hand):
                user.points_effects += bonus_card
                
        if condition == 'sum':
            #adds the values ​​of the cards
            for x in user.hand:
                if x.suit == suits:
                    user.points_effects += x.points

        if condition == 'more_special':
            #a specific card together with another, other specific cards
            condition1 = set(cards[0])
            condition2 = set(cards[1])
            if condition1.issubset(card_names_in_hand):
                if any(x in card_names_in_hand for x in condition2):
                    user.points_effects += bonus_card

        if condition == 'less_special':
            #one of the specific cards
            condition1 = set(cards[0])
            condition2 = set(cards[1])
            if condition1.issubset(card_names_in_hand):
                user.points_effects += bonus_card[0]
            else:
                if any(x in card_names_in_hand for x in condition2):
                    user.points_effects += bonus_card[1]

    def max_same_suit(self, user):
        """Counts the number of cards of the same suit"""
        max_count = 0
        index = 9
        while index > -1:
            suit = suits_list[index]
            count = sum(1 for card in user.hand if card.suit == suit)
            if count > max_count:
                max_count = count
            index -= 1
        if max_count > 4:
            user.points_effects += 100
        elif max_count > 3:
            user.points_effects += 40
        elif max_count > 2:
            user.points_effects += 10

    def max_value(self, user, condition, suits):
        """Adds the largest base point value of a card from a selection of card types"""

        if condition == 'přidej':
            points = [] 
            for x in user.hand:
                if x.suit in suits:
                    points.append(x.value)                  
            user.points_effects += max(points)

    def sequence(self, user):
        """Calculates the highest sequence of basic card values"""
        max_count = 1
        current_count = 1
        sorted_cards = sorted(user.hand, key=lambda card: card.value)
        for i in range(1, len(sorted_cards)):
            if sorted_cards[i].value == sorted_cards[i-1].value + 1:
                current_count += 1
                max_count = max(max_count, current_count)
            elif sorted_cards[i].value == sorted_cards[i-1].value:
                current_count += 0
                max_count = max(max_count, current_count)
            else:
                current_count = 1
        points = {8 : 150, 7 : 150, 6 : 100, 5 : 60, 4 : 30, 3: 10}
        if max_count > 2:
            user.points_effects += points[max_count]

    def odd_value(self, user):
        """Calculates the odd base values ​​of the cards"""
        not_even = True
        all_points = -3
        for x in user.hand:
            if x.value % 2 == 1:
                all_points += 3
            else:
                not_even = False
        if not_even == True:
            user.points_effects += 50
        else:
            user.points_effects += all_points

    def different_suits(self, user):
        """Find out if all suits of cards in the hand are different"""
        if len([x.suit for x in user.hand]) == len(set([x.suit for x in user.hand])):
            user.points_effects += 50

    def plus_limit(self, user):
        """Increases the player's hand limit by one"""
        if user.max_limit == 7: 
            user.limit += 1
            user.max_limit += 1

    def erase_cards(self, user, ID, cards = [], suits = []):
        """Erases specific suits, except for specific cards"""
        for x in user.hnad:
            if x.suit in suits and x.ID != ID and x.name not in cards:
                x.activ = False

    def erase_no_suit(self, user, ID, cards = [], suits = []):
        """deleted if you don't have at least one card of the desired suit"""
        suits_in_hand = set([x.suit for x in user.hand])
        if any(x in suits_in_hand for x in suits[0]):
            for x in user.hand:
                if x.ID == ID:
                    x.activ = True
        else:
            for x in user.hand:
                if x.ID == ID:
                    x.activ = False

    def erase_if_suit(self, user, ID, cards = [], suits = []):   
        """deleted if you have at least one card of the specified suit"""
        suits_in_hand = set([x.suit for x in user.hand])
        if any(x in suits_in_hand for x in suits[1]):
            for x in user.hnad:
                if x.ID == ID:
                    x.activ = False


    def erase_suit(self, user, suit):
        """clears a specific card suit from card penalties"""
        for x in user.hand:
            if x.effect2 != None: 
                if suit in x.effect2[4] and x.name != "Požár":
                    x.effect2[4].remove(suit)
            if x.effect3 != None:
                if x.name == "Bojová vzducholoď":
                    pass
                else:
                    if suit in x.effect3[1] and x.name != "Požár":
                        x.effect3[1].remove(suit)

    def erase_suit_ex(self, user, suit):
        """clears a specific card suit from card penaltis
            from the specified cards"""
        for x in user.hand:
            if x.suit == suit[0]:
                if x.effect2 != None: 
                    if suit in x.effect2[4] and x.name != "Požár":
                        x.effect2[4].remove(suit[1])
                if x.effect3 != None:
                    if suit in x.effect3[1] and x.name != "Požár":
                        x.effect3[1].remove(suit[1])

    def penalty_off(self, user, suit):
        """Sets penalty condition to False on all cards """
        for x in user.hand:
            if x.suit == suit:
                x.penalty_condition = False



class Player(QObject):

    players = 0
    points_all_changed = pyqtSignal(int)
    limit_change = pyqtSignal(int)
    max_limit_change = pyqtSignal(int)
    cards_hand_change = pyqtSignal(int)
    string_hand_change = pyqtSignal(str)
    string_hand_passive_change = pyqtSignal(str)
    
    
    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.limit = 7
        self.max_limit = 7
        self.hand = []
        self.hand_passive = []
        self.string_hand = ""
        self.string_hand_passive = ""
        self.points = 0
        self.points_effects = 0
        self.points_all = 0
        Player.players += 1
        self.cards_hand = len(self.hand) + len(self.hand_passive)

    @property
    def string_hand_passive(self):
        return self._string_hand

    @string_hand_passive.setter
    def string_hand_passive(self, value):
        self._string_hand_passive = value
        self.string_hand_passive_change.emit(value)

        

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
        self.points_all_changed.emit(value)

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
        new = cards_list[ind(name)]
        if new in used_cards or self.limit == 0:        
            print("Nelze přidat")
        else:
            self.limit -= 1 ##sníží o jedna
            used_cards.append(new) ##hodí novou kartu do použitých
            
            self.hand.append(new)## hodí novou kartu na ruku
 
            points_count(self)
            points_count(self)
            
            
            
    def remove_card(self, name):
        card = cards_list[ind(name)]
        index = cards_list.index(card)
        self.limit += 1
        if card in self.hand:
            self.hand.remove(card)
        else:
            self.hand_passive.remove(card)
        used_cards.remove(card)
        recovery(self, card, index)
        is_it_active(self)
        points_count(self)

    def reset(self):
        """Restarts the player to the default state"""
        for x in self.hand:
            self.remove_card(x.name)
        for x in self.hand_passive:
            self.remove_card(x.name)
        self.limit = 7
        self.max_limit = 7
        self.hand = []
        self.hand_passive = []
        self.string_hand = ""
        self.string_hand_passive= ""
        self.points = 0
        self.points_effects = 0
        self.points_all = 0
        used_cards.clear()

def ind(name):
    """returns the index of the object in card_list
    according to the "name" attribute"""
    from hrac import cards_list
    cont = True
    index = 0
    while cont == True:
        if cards_list[index].name.lower() != name.lower():
            index +=1
        else:
            cont = False
    return index
        

cards_list = [Card(card['name'], card['body'], card['typ'],
                          card.get('bonus'), card.get('efekt'),
                          card.get('postih'), card.get('efekt2'),
                          card.get('mazani'), card.get('efekt3'),
                          card.get('vymaz_masli'), card.get('vymaz_nemasli'),
                          card.get('odstran'), card.get('efekt4')                           
                          ) for card in cards_stats]


