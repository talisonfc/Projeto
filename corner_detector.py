from camera import Camera
import utils
import cv2
import numpy as np

window = cv2.namedWindow('imgs')

frame = cv2.imread("Dataset/forms.jpg")
img = utils.resize(utils.rgb2gray(frame),0.2)

coners = cv2.goodFeaturesToTrack(img, 25, 0.01, 10)
coners = np.int0(coners)


N = len(coners)
for i in coners:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, (0,255,0), -1)

while cv2.waitKey(1) != 27:
    cv2.imshow(window, img)

'''
rootdir="imgs"
cam = Camera('Camera')

while cv2.waitKey(1) != 27:
    frame = cam.capture()
    img = utils.resize(utils.rgb2gray(frame),1)
    img_ = cv2.bilateralFilter(img,9,75,75)
    
    coners = cv2.goodFeaturesToTrack(img, 25, 0.01, 10)
    coners = np.int0(coners)


    N = len(coners)
    for i in coners:
        x,y = i.ravel()
        cv2.circle(img, (x,y), 3, 255, -1)

    cam.show(imgS)
'''