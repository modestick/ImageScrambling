import numpy as np
import cv2
import random

def logistic_map_key(s):
    h, w = s[0], s[1]
    all_pixels = h * w
    x = random.uniform(0.11 , 0.99)
    skip = 1111
    r = 4

    for _ in range(skip):
        x = r * x * (1 - x)

    array = []
    for _ in range(all_pixels):
        x = r * x * (1 - x)
        array.append(x)

    return np.argsort(array)

def scram(img, k):
    flat = img.reshape((-1, 3))
    return flat[k].reshape(img.shape)

def unscram(scram, k):
    flat = scram.reshape((-1, 3))
    reverse_k = np.empty_like(k)
    reverse_k[k] = np.arange(len(k)) 

    restored = flat[reverse_k]
    return restored.reshape(scram.shape)

pic = cv2.imread("myPicture.jpg")
if pic is None:
    print("Image is not found")
    quit()

lmkey = logistic_map_key(pic.shape)
s = scram(pic, lmkey)
us = unscram(s, lmkey) 

cv2.imwrite("scrambled.jpg", s)
cv2.imwrite("unscrambled.jpg", us)
