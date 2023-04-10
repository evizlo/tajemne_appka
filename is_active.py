from player import *


def erase_by_priority(user, priority):
    """Deletes the card according to the specified priority"""
    for x in user.hand:
        if x.erase == priority and x.activ == True and x.penalty_condition == True:
            x.erase_cards(user, x.ID, *x.effect3)


def erase(user, count):
    """Gradually deletes according to priorities from one
    to the total number of types of priorities"""
    priority = 1
    while priority != count + 1:
        erase_by_priority(user, f'priority_{priority}')
        cards_mgmt(user)
        priority += 1

def cards_mgmt(user):
    """Moves inactive cards to the users passive hand"""
    for x in user.hand:
        if x.activ == False:
            user.hand.remove(x)
            user.hand_passive.append(x)
        
def passive_if_not(user):
    """Inactive cards that do not have a specific card to pair"""
    for x in user.hand:
        if x.erase_not_if == True and x.penalty_condition == True:
            x.erase_no_suit(user, x.ID, *x.effect3)
    cards_mgmt(user)
    
def passive_if(user):
    """Inactive cards that are blocked by another card"""
    for x in user.hand:
        if x.erase_if == True and x.penalty_condition == True:
            x.erase_if_suit(user, x.ID, *x.effect3)
    cards_mgmt(user)
            
def all_active(user):
    """Moves all cards to the hand"""
    for x in user.hand_passive:
        user.hand.append(x)
        user.hand_passive.remove(x)

def active_true(user):
    """Activates all cards in hand"""
    for x in user.hand:
        x.activ = True

def cards_string(user):
    """converts cards names to strings
       one with active andone with deleted cards"""
    user.string_hand = ""
    string_list = [str(obj) for obj in user.hand]
    separator = ", "
    user.string_hand = separator.join(string_list)
    
    user.string_hand_passive = ""
    string_list2 = [str(obj) for obj in user.hand_passive]
    separator = ", "
    user.string_hand_passive = separator.join(string_list2)
    
def is_it_active(user):
    """It will find out which cards are active and which are passive"""
    all_active(user)
    active_true(user)
    erase(user, 4)
    passive_if_not(user)
    passive_if(user)   
    cards_string(user)






