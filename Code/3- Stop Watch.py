# template for "Stopwatch: The Game"



#-------------------------------------------------
#-------------------------------------------------

# global state

import simplegui


# define global variables
ticks = 0
total_stops = 0
correct_stops = 0

timer_stopped = True

#-------------------------------------------------
#-------------------------------------------------


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    # one tenth of a second
    d = t % 10
    
    # total seconds
    seconds = t // 10

    a = seconds // 60
    
    bc = seconds % 60
    
    c = bc % 10
    b = bc // 10
    
    
    result = str(a) + ":" + str(b) + str(c) + "." + str(d)
    
    return result
    
#-------------------------------------------------    
#-------------------------------------------------

    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global timer_stopped
    timer.start()
    timer_stopped = False

    
def stop():
    global timer_stopped
    
    if not timer_stopped:
        timer.stop()

        global total_stops, correct_stops

        if ticks % 10 == 0:
            correct_stops += 1

        total_stops += 1
        
        timer_stopped = True
    

def reset():
    global ticks, correct_stops, total_stops, timer_stopped
    ticks = 0
    correct_stops = 0
    total_stops = 0
    timer_stopped = True
    timer.stop()


#-------------------------------------------------    
#-------------------------------------------------


# define event handler for timer with 0.1 sec interval

def increment_ticks():
    global ticks
    ticks += 1


# define draw handler

def draw(canvas):
    canvas.draw_text(format(ticks), [75, 100], 40, "Green")
    canvas.draw_text(str(correct_stops) + "/" + str(total_stops), [270,20], 20, "Red")
  

#-------------------------------------------------    
#-------------------------------------------------
    
    
# create frame

frame = simplegui.create_frame("Stop Watch: The Game", 300, 200)
timer = simplegui.create_timer(100, increment_ticks)

#-------------------------------------------------    
#-------------------------------------------------


# register event handlers

frame.set_draw_handler(draw)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)


#-------------------------------------------------    
#-------------------------------------------------

# start frame

frame.start()


#-------------------------------------------------    
#-------------------------------------------------
