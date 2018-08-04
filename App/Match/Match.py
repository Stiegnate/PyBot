import cv2
import numpy as np
from PIL import Image

class Match:
    def __init__(self, *args, **kwargs):
        self.true_or_false = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None

    def _OpenCV(self, np_img_big, np_img_small, accuracy=0.98):
        np_img_small_x, np_img_small_y = np_img_small.shape[1], np_img_small.shape[0]
        result = cv2.matchTemplate(np_img_big, np_img_small,cv2.TM_CCOEFF_NORMED)
        index = np.unravel_index(result.argmax(),result.shape)
        if len(np.where(result>accuracy)[0])!=0:
            x0 = index[1]
            y0 = index[0]
            x1 = index[1] + np_img_small_x
            y1 = index[0] + np_img_small_y
            return True, (x0, y0, x1, y1)
        else:
            return False, (x0, y0, x1, y1)        

    def find(self, np_img_big, np_img_small, method = 'OpenCV', mode = 'Default'):
        if method == 'OpenCV':
            self.true_or_false, (self.x0, self.y0, self.x1, self.y1) = self._OpenCV(np_img_big, np_img_small)
        
        if mode == 'Default':
            return self.true_or_false, (self.x0, self.y0, self.x1, self.y1)
        elif mode == 'pos2':
            return (self.x0, self.y0)
        elif mode == 'pos2_random':
            x_random = int(np.random.random_sample() * (self.x1 - self.x0) + self.x0)
            y_random = int(np.random.random_sample() * (self.y1 - self.y0) + self.y0)
            return (x_random, y_random) 
        elif mode == 'pos4':
            return (self.x0, self.y0, self.x1, self.y1)



            

