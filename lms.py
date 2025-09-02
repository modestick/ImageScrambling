import numpy as np
import cv2
import random
import sys


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



if sys.argv[1] == 'scram':
    arg_pic = cv2.imread(sys.argv[2])
    if arg_pic is None:
        print("Image is not found")
        quit()

    arg_pic_key = logistic_map_key(arg_pic.shape)
    np.save("key.npy", arg_pic_key)

    arg_pic_scramble = scram(arg_pic, arg_pic_key)
    cv2.imwrite("scrambled.png", arg_pic_scramble)


elif sys.argv[1] == 'unscram':
    arg_key = np.load(sys.argv[2])
    arg_pic = cv2.imread(sys.argv[3])

    arg_pic_unscramble = unscram(arg_pic, arg_key)
    cv2.imwrite("unscrambled.png", arg_pic_unscramble)
