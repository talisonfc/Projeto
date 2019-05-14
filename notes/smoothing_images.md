# Smoothing images

- Blur images with vaiuos low pass filters
- Apply custom-made filters to images (2D convolution)

## 2D Convolution

As for one dimensional signals, images also can be filtered with low-pass-filter (PPF) and high-pass-filter (HPF). LPF helps to remove noise, or bluring the image. HPS helps in find adges in a image.

OpenCV provides `cv2.filter2D(...)` to convolve a kernel with an image. As an example, we will try a average filter on a image. A 5x5 average filter kernel can be defined as follows:

$K=\frac{1}{25}
\left[\begin{array}[] 
11 & 1 & 1 & 1 & 1 \\ 
1 & 1 & 1 & 1 & 1 \\ 
1 & 1 & 1 & 1 & 1 \\ 
1 & 1 & 1 & 1 & 1 \\ 
1 & 1 & 1 & 1 & 1\end{array}\right]$

## Image Blurring 

- Averaging - `cv2.blur()` `cv2.boxFilter()`
  - $K = \frac{1}{n*m}M_{mxn}$

- Gaussian Filter - `cv2.GaussianBlur(img, window), desvio)`
- Median Filter - `cv2.mediaBlur(img, median)`
- [Bilateral Filter](<http://people.csail.mit.edu/sparis/bf_course/>) - `cv2.bilateralFilter(...)`



```python
from camera import Camera
import utils
import cv2
import numpy as np

rootdir="imgs"
cam = Camera('Camera')

while cv2.waitKey(1) != 27:
    frame = cam.capture()
    img = utils.resize(utils.rgb2gray(frame),0.5)
    th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    
    # average filter
    kernel = np.ones((5,5), np.float32)/25
    img_1 = cv2.filter2D(img, -1, kernel)
    th1 = cv2.adaptiveThreshold(img_1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    # blur - tjaes the average of all the pixels under kernel are and replace the central element with this average
    img_2 = cv2.blur(img, (5,5))
    th2 = cv2.adaptiveThreshold(img_2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    #filter gaussiano
    img_3 = cv2.GaussianBlur(img,(5,5),0)
    th3 = cv2.adaptiveThreshold(img_3,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    # bilateral filtering
    img_4 = cv2.bilateralFilter(img,9,75,75)
    th4 = cv2.adaptiveThreshold(img_4,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    im = utils.concatV(img, th) # average
    im1 = utils.concatV(img_1, th1) # blur
    im2 = utils.concatV(img_2, th2) # FPB with average
    im3 = utils.concatV(img_3, th3) # FPB with goussiana
    im4 = utils.concatV(img_4, th4) # FPB with goussiana
    # image = utils.concatH(utils.concatH(im, im1),utils.concatH(im2, im4))
    image = utils.concatH(im, im4)
    cam.show(image)
```



### References

<https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html>