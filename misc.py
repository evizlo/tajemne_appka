from is_active import *
from cards_stats_2 import cards_stats_2
from cards_stats import cards_stats
from hrac import *
import copy

def recovery(user, card, index):
    """Restores the returned card's attributes"""
    new_list = copy.deepcopy(cards_stats_2)

    if card.effect2 != None:
        card.effekt2 = new_list[index]['efekt2']

    if card.effect3 != None:
        card.effect3 = new_list[index]['efekt3']


    card.activ = True
    card.penalty_condition = True

def recovery_hand(user):
    """Restores the attributes of all cards in the hand"""
    from hrac import cards_list
    from hrac import ind
    for x in user.hand:
        card = cards_list[ind(x.name)]
        index = cards_list.index(card)
        recovery(user, card, index)
        

def points_count(user):
    from is_active import active_true, all_active, is_it_active
    """It first finds out which cards are not active
       and then counts the points"""
    user.points_effects = 0
    user.points = 0
    user.points_all = 0

    all_active(user); active_true(user)
    recovery_hand(user)
    penalty_off_all(user)
    penalty_delete(user)
    is_it_active(user)      
        
        
    for x in user.hand:
        user.points += x.value 
        if x.bonus == 'post':
            x.sequence(user)
        if x.bonus == 'bkt':
            x.card_bonus(user, x.ID, *x.effect)
        if x.penalty == 'bkt' and x.penalty_condition == True:
            x.card_bonus(user, x.ID, *x.effect2)
        if x.bonus == 'ret':
            x.max_value(user, *x.effect)
        if x.bonus == 'mt':
            x.max_same_suit(user)
        if x.bonus == 'pl':
            x.plus_limit(user)
        if x.bonus == 'lc':
            x.odd_value(user)
        if x.bonus == 'nt':
            x.different_suits(user)
    user.points_all = (user.points + user.points_effects)

def penalty_delete(user):
    """remove penalties according to various requirements"""
    for x in user.hand:
        if x.delete == 'odstr':
            x.penalty_off(user, x.effect4)
        if x.delete == 'slovo':
            x.erase_suit(user, x.effect4)
        if x.delete == 'exclusive':
            x.erase_suit_ex(user, x.effect4)

def penalty_off_all(user):
    """Sets all penalty contition to False, must be first"""
    if any('11-Ochranná runa' == x.ID for x in user.hand):
        for x in user.hand:
            x.penalty_condition = False







            







        
    

    
