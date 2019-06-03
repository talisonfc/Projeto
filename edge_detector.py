import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import utils

window = cv2.namedWindow('imgs')

frame = cv2.imread("Dataset/forms.jpg")
img = utils.resize(utils.rgb2gray(frame),0.2)

edges = cv2.Canny(img, 100,200)

while cv2.waitKey(1) != 27:
    cv2.imshow(window, edges)