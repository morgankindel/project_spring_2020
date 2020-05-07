

#import required packages 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('./Sample_images/1.jpg')
cv2.imshow("Binary Image",bw_img)

cv2.waitKey(0)
cv2.destroyAllWindows()