# OpenCV

Library to work with image processing

## Changing colorspace

There are several system of color. Each system of color define a color space. Each color space represent the image with 3 componentes. 

- RGB - Red Green and Blue
- HSV - Matiz Saturation and Value
- HSB - Matiz Saturation and Brightness
- HSI - Matiz Saturation and Intensity
- HSL - Matiz Saturation and Luminosity

`cvtColor(frame, flag)` `inRange(frame, lower, higher)`

```
while cv2.waitKey(1) != 27:
    frame = cam.capture()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cam.show(res)
```

