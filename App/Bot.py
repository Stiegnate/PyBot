import sys
if sys.platform == 'win32':
    from .Action.win import Mouse
elif sys.platform == '':
    pass
elif sys.platform == '':
    pass

class Bot:
    def __init__():
        pass
    
    def event(self, check, action):
        if check:
            action()