# Thresholding

Thresholding is used to set some image region for a specific value. 

OpenCV has two functions to work with thresholding: `cv2.threshold` e `cv2.adaptiveThreshold`. The first one is used to simple threshold and the second one is used for adaptativa threshold.

- `th, img = threshold(image, lower, higher, flag`

  - cv2.THRESH_BINARY
  - cv2.THRESH_BINARY_INV
  - cv2.THRESH_TRUNC
  - cv2.THRESH_TOZERO
  - cv2.THRESH_TOZERO_INV

- `img = adapdativeThreshold(image, constatnt, flag,h_window,w_window) `

  - Simple trashed set a global threshold for all image. But it may not be good in all conditions where images has diferent lighting conditions in different areas. Adaptative threshold calculate the threshold for small regions of the image.
    - To specify the region to calc threshold, we set `h_windown` e `w_windown` 
    - `constant` is a constat to subtract the mean or wighted mean
    - Flags:
      - `cv2.ADAPTIVE_THRESH_MEAN_C` - threshold value is the mean of neighbourhood area
      - `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` - threshold value is the weighted sum of neighbourhood values where weights are a gaussian window

  ## Otsu's Binarization

  It's necessry a threshold value to use `threshold` function. We can get the optimal threshold value using the Otsu algorithm. This algorithm calcs the threshold value as the mean between two peaks from histogram of a **bimoal imagem** (is a image whose histogram has two peaks).

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
  
      # simple trasheholding
      ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
      ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
      ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
      ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
      ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
  
      blur = cv2.GaussianBlur(img,(5,5),0)
  
      # adaptative trasheholding
      th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
      th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
      
      th2_ = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
      th3_ = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
  
      # Otsu's thresholding
      ret2,th4 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  
      # Otsu's thresholding after Gaussian filtering
      ret3,th5 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  
      s1 = utils.concatV(thresh1, th2)
      s2 = utils.concatV(th2_, th5)
      image = utils.concatH(s1,s2)
      cam.show(image)
  ```





# Reference

<https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html>