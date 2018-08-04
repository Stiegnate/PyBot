import time

def printing_run_function_info(func):
    def printing(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)
        t1 = time.time()
        print('run function [%s]: %s(s)' % (func.__name__, str(t1-t0)))
        return
    return printing

def App_Action_win32_Mouse_0():
    import App.Action.win32.Mouse as bot
    b = bot.Mouse(300, 300)
    b.move()
    b.right_click()

def App_Action_win32_Mouse_1():
    import App.Action.win32.Mouse as bot
    bot.Mouse().right_click()

def App_Action_win32_Screenshot():
    import App.Action.win32.ScreenShot as ScreenShot
    import numpy as np
    from PIL import Image

    #ScreenShot.ScreenShot().save()

    # show screenshot in python Image library
    img = ScreenShot.ScreenShot().get_img()
    img.show()

@printing_run_function_info
def App_Match_Match_0():
    import App.Match.Match as Match
    import numpy as np
    from PIL import Image
    
    img_big = Image.open('temp.bmp')  
    img_small = Image.open('ref.bmp')

    img_big = np.asarray(img_big)
    img_small = np.asarray(img_small)

    print(Match.Match().find(img_big, img_small))
    print(Match.Match().find(img_big, img_small, mode = 'pos2_random'))

def App_Bot():
    import App.Bot as bot
    import App.Action.win as action
    a = action.Mouse()
    bot.Bot.event(True, a.move(300,300))

if __name__ == '__main__':
    App_Match_Match_0()