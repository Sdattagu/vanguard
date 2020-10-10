import numpy as np
import cv2

def func_other():
    image = cv2.imread('test.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    lower_yellow = (28, 220, 254)
    upper_yellow = (30, 250, 255)
    lower_red = (0, 250, 200)
    upper_red = (10, 255, 255)

    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Find contours
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Extract contours depending on OpenCV version
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # Iterate through contours and filter by the number of vertices
    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
        if len(approx) > 3:
            (x, y), radius = cv2.minEnclosingCircle(c)
            center = (int(x), int(y))
            radius = int(radius)
            print('Contour: centre {},{}, radius {}'.format(x, y, radius))
            cv2.drawContours(result, [c], -1, (36, 255, 12), -1)

    cv2.imshow('mask', mask)
    cv2.imshow('original', result)
    cv2.imwrite('mask.png', mask)
    cv2.imwrite('original.png', result)
    cv2.waitKey()