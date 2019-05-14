# Geometric Transformation

- Scaling - `resize(image,(width, height), fx, fy, insterpolation)`
  - Final widht
  - FInal height
  - fx - x scale factor
  - fy - y scale factor
  - interpolation algorithm: `cv2.INTER_AREA,` `cv2.INTER_CUBIC ` e `cv2.INTER_LINEAR` (default)
- Translation - `cv2.warpAffine(image, M, (cols, rows))`
  - M - transformation matrix
  - cols and rows is the number of columns and rows
- Rotation -` cv2.warpAffine(image, M, (cols, rows))`
  - M - transformation matrix
  - `cv2.getRotationMatrix2D((cols, rows), angle, scale)` - this function cals the transformation matrix based on trigonometric operations define for this transformation
-  Twist -` cv2.warpAffine(image, M, (cols, rows))
  - `getAffineTransform(pts1, pts2)`
    - `pts1` define point to change
    - `pts2` define where `pts1` will be after transformation
- Perspective - `warpPerspective(ima, M, (cols, rows))`
  - `getPerspectiveTransform(pts1,pts2)` 

```
from camera import Camera
import utils
import cv2
import numpy as np

rootdir="imgs"
cam = Camera('Camera')

while cv2.waitKey(1) != 27:
    frame = cam.capture()
    img = utils.resize(utils.rgb2gray(frame),0.5)
    
    # filter gaussiano
    img_ = cv2.GaussianBlur(img,(5,5),0)

    rows,cols = img.shape
    # deslocamento
    M1 = np.float32([[1,0,100],[0,1,50]])
    dst1 = cv2.warpAffine(img,M1,(cols,rows))

    # rotate
    M2 = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst2 = cv2.warpAffine(img,M2,(cols,rows))
    
    # torcao
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M3 = cv2.getAffineTransform(pts1,pts2)
    dst3 = cv2.warpAffine(img,M3,(cols,rows))

    # perpectiva
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    M4 = cv2.getPerspectiveTransform(pts1,pts2)
    dst4 = cv2.warpPerspective(img,M4,(cols,rows))

    image = utils.concatH(img,dst4)
    cam.show(image)
```

