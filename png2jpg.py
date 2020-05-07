from glob import glob                                                           
import cv2
import os
pngs = glob('/Users/apple1/Desktop/MLiS_2/training_one/images/train/*.png')

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)
    os.remove(j)
