from camera import Camera
import utils
import cv2
import numpy as np

rootdir="imgs"
cam = Camera('Camera')

while cv2.waitKey(1) != 27:
    frame = cam.capture()
    img = utils.resize(utils.rgb2gray(frame),0.3)
    img_ = cv2.bilateralFilter(img,9,75,75)
    th = cv2.adaptiveThreshold(img_,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    kernel = np.ones((3,3), np.uint8)
    
    dilation = cv2.dilate(th, kernel, iterations = 1)
    
    erosion = cv2.erode(dilation, kernel, iterations = 1)

    opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)

    closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)
   
    im1 = utils.concatV(img, th)
    im2 = utils.concatV(erosion, dilation)
    im3 = utils.concatV(closing, opening)
    image = utils.concatH(im1, utils.concatH(im2,im3))
    cam.show(image)