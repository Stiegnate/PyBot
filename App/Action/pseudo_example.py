def left_click(t=0.1):
    '''
    t: the delay time between pressing left click and releasing left click
    '''
    press()
    time_delay()
    release()

def right_click(t=0.1):
    as left_click

def move(pos1, pos2):
    '''
    pos1: initial position of mouse [x1,y1]
    pos2: final position of mouse [x2,y2]
    '''
    pass

def left_click_hold(t):
    '''
    thinking
    '''

def scroll_click():
    '''
    thinking
    '''

def keyboard_type('string',t=0.1):
    '''
    example:
        input:
            keyboard_type('my name')
        output:
            typing the keyboard 'm', 'y', ... and so on with time delay t = 0.1(sec).
    '''
