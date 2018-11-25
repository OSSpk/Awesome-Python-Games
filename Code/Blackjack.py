# Mini-project #6 - Blackjack

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

import simplegui
import random

#---------------------------------------------------------------

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    


# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message = ""
display_hole_card = False
game_stop = True

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



#---------------------------------------------------------------
#---------------------------------------------------------------

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
#---------------------------------------------------------------
        
        
# define hand class
class Hand:
    def __init__(self):
        self.cards_list = []

    def __str__(self):
        ans = "Hand contains "
        for x in self.cards_list:
            ans += str(x) + " "
            
        return ans

    def add_card(self, card):
        self.cards_list.append(card)	

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        
        value = 0
        has_rank = False
        
        for x in self.cards_list:
            r = x.get_rank()
            
            if r == RANKS[0]:
                has_rank = True
                
            value += VALUES[r]

        if has_rank and (value+10 <= 21):
            value += 10
        
        return value
    
    
    def draw(self, canvas, pos):
        for x in self.cards_list:
            x.draw(canvas, pos)
            pos[0] += 100

#---------------------------------------------------------------
            
                
# define deck class 
class Deck:
    def __init__(self):       
        self.cards_list = [Card(s,r) for s in SUITS for r in RANKS]
        
    def shuffle(self):
        random.shuffle(self.cards_list) 

    def deal_card(self):
        return self.cards_list.pop(-1)
    
    def __str__(self):
        ans = "Deck contains "
        for x in self.cards_list:
            ans += str(x) + " "
            
        return ans
        
#---------------------------------------------------------------
#---------------------------------------------------------------
    
    
#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, player_hand
    global dealer_hand, message, display_hole_card, game_stop, score
    
    if game_stop == False:
        outcome = "You lose."
        score -= 1
        message = "New deal?"
        display_hole_card = True
        game_stop = True
                
    else:
        game_deck = Deck()
        game_deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        for i in range(2):
            player_hand.add_card( game_deck.deal_card() )
            dealer_hand.add_card( game_deck.deal_card() )    

        in_play = True
        display_hole_card = False
        outcome = ""
        message = "Hit or Stand?"

        game_stop = False

#---------------------------------------------------------------
   
def hit():

    global outcome, score, message, display_hole_card, game_stop
        
    if game_stop == False:
        
        # if the hand is in play, hit the player    
        if in_play:
            if player_hand.get_value() <= 21:
                player_hand.add_card(game_deck.deal_card())

            if player_hand.get_value() > 21:
                outcome = "You went bust and lose."
                message = "New deal?"
                score -= 1
                display_hole_card = True
                game_stop = True
        else:
            dealer_hand.add_card(game_deck.deal_card())
#---------------------------------------------------------------
        
def stand():

    global in_play, outcome, score, message, display_hole_card, game_stop
    
    if game_stop == False:

        message = "New deal?"
        in_play = False

        display_hole_card = True

        # repeatedly hit dealer until his hand has value 17 or more
        while (dealer_hand.get_value() < 17):
            hit()

        if dealer_hand.get_value () > 21:
            outcome = "You won."
            score += 1

        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                outcome = "You lose."
                score -= 1        

            else:
                outcome = "You won."
                score += 1

        game_stop = True
#---------------------------------------------------------------
#---------------------------------------------------------------

                                                                                              
# draw handler    
def draw(canvas):
   
    canvas.draw_text("Blackjack", [100, 100], 50,  "Red")
    canvas.draw_text("Score: " + str(score), [400, 100], 40,  "yellow")
    
    canvas.draw_text("Dealer", [40, 200], 40,  "Black")      
    canvas.draw_text("Player", [40, 400], 40,  "Black")                                       

    canvas.draw_text(outcome, [250, 200], 35,  "Black")                                       
    canvas.draw_text(message, [300, 400], 40,  "Black")                                       
    
    player_hand.draw(canvas, [50, 440])
    dealer_hand.draw(canvas, [50, 230])
    
    if display_hole_card == False:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE
                          , [50 + CARD_CENTER[0], 230 + CARD_CENTER[1]], CARD_BACK_SIZE)
     
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
#-----------------------------------------------------------------

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
#-----------------------------------------------------------------

# defining global objects
game_deck = Deck()
player_hand = Hand()
dealer_hand = Hand()
#-----------------------------------------------------------------
                                 
# get things rolling
deal()
frame.start()
