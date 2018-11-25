# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import simplegui


#------------------------------------------
# declaring global variables
secret_number = 0
num_range = 100
remaining_guesses = 0

#------------------------------------------
# helper function to start and restart the game

def new_game():
    print "----------------------------------------"
    print "----------------------------------------"
    
    print "New game. Range is from 0 to", num_range
    
    global secret_number, remaining_guesses
    
    secret_number = random.randrange(0, num_range)

    remaining_guesses = int( math.ceil(math.log(num_range, 2)) )
    
    print "Total Guesses:", remaining_guesses
    
    
#------------------------------------------
# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 

    global num_range
    num_range = 100
    new_game()
    
  
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global num_range
    num_range = 1000
    new_game()
    

def reset():
    new_game()
    
    
def input_guess(guess):
    
    global remaining_guesses
    
    guess = int(guess)
    
    print "Guess was", guess
    
    if guess < secret_number:
        print "Higher!"
    elif guess > secret_number:
        print "Lower!"
    else:
        print "Correct!"
        new_game()
        return
    
    remaining_guesses -= 1
    print ""
    print "Number of remaining guesses is :", remaining_guesses
    
    if remaining_guesses == 0:
        print "You ran out of guesses :(  The secret number was", secret_number
        new_game()

#------------------------------------------
        
# create frame

frame = simplegui.create_frame("Guess the Number", 200, 200)

#------------------------------------------

# register event handlers for control elements and start frame

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

frame.add_button("New Game", reset, 200)

#------------------------------------------
# call new_game 
new_game()

#------------------------------------------
# starting the frame
frame.start()
#------------------------------------------




# always remember to check your completed program against the grading rubric
