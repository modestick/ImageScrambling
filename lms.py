import numpy as np
import cv2
import random
import argparse


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


myparser = argparse.ArgumentParser(description='Image Scrambling')

mysubparser = myparser.add_subparsers(dest='action', required=True, title='Commands')

cli_scram = mysubparser.add_parser('scram', help='Scramble the image')
cli_scram.add_argument('image', help='Path to the image to scramble')

cli_unscram = mysubparser.add_parser('unscram', help='Unscramble the image')
cli_unscram.add_argument('image', help='Path to th image to unscramble')
cli_unscram.add_argument('key', help='The key for unscrambling')

args = myparser.parse_args()


if args.action == 'scram':
   
    arg_image = cv2.imread(args.image)
    arg_key = logistic_map_key(arg_image.shape)
    scrambled_result = scram(arg_image, arg_key)

    cv2.imwrite('scrambled.png', scrambled_result)
    np.save('key.npy',arg_key )

elif args.action == 'unscram':
    
    arg_image = cv2.imread(args.image)
    arg_key = np.load(args.key)
    unscrambled_result = unscram(arg_image, arg_key)

    cv2.imwrite('unscrambled.png', unscrambled_result)
    

    