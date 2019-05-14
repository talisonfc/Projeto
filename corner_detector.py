from camera import Camera
import utils
import cv2
import numpy as np

rootdir="imgs"
cam = Camera('Camera')

while cv2.waitKey(1) != 27:
    frame = cam.capture()
    img = utils.resize(utils.rgb2gray(frame),1)
    img_ = cv2.bilateralFilter(img,9,75,75)
    th = cv2.adaptiveThreshold(img_,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    coners = cv2.goodFeaturesToTrack(img, 25, 0.01, 10)
    coners = np.int0(coners)


    N = len(coners)
    for i in coners:
        x,y = i.ravel()
        cv2.circle(img, (x,y), 3, 255, -1)

    cam.show(img)