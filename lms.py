import numpy as np
import cv2
import random
import argparse
import os
import zipfile
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def logistic_map_key(s): 
    """
    Generate a permutation key using the logistic map based on image dimensions.

    Parameters:
        s : The dimensions of the image.

    Returns:
        An array of indices representing a permutation key, 
    """
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
    '''
    Scramble the image using the generated key.

    Parameters:
        img : An image
        k : The generated key

    Returns:
        Scrambled picture

    '''
    flat = img.reshape((-1, 3))
    return flat[k].reshape(img.shape)

def unscram(scram, k):
    '''
    Unscramble the image using the key

    Parameters:
        scram : A scrambled picture
        k : The key
    
    Returns:
        Unscrambled picture

    '''
    flat = scram.reshape((-1, 3))
    reverse_k = np.empty_like(k)
    reverse_k[k] = np.arange(len(k)) 

    restored = flat[reverse_k]
    return restored.reshape(scram.shape)



def main():
    myparser = argparse.ArgumentParser(description='Image Scrambling')

    mysubparser = myparser.add_subparsers(dest='action', required=True, title='Commands')

    cli_scram = mysubparser.add_parser('scram', help='Scramble the image')
    cli_scram.add_argument('image', help='Path to the image to scramble')
    cli_scram.add_argument('--zip_keys', action='store_true', help='Save all keys into a single zipped .zip file')
    cli_scram.add_argument('--zip_images', action='store_true', help='Save all scrambled images into a single zipped .zip file')


    cli_unscram = mysubparser.add_parser('unscram', help='Unscramble the image')
    cli_unscram.add_argument('image', help='Path to th image to unscramble')
    cli_unscram.add_argument('key', help='The key for unscrambling')

    args = myparser.parse_args()

    scrambled_images_dir = (os.path.join('lms_images', 'scrambled'))
    unscrambled_images_dir = (os.path.join('lms_images', 'unscrambled'))
    keys_dir = (os.path.join('lms_images', 'keys'))
    os.makedirs(scrambled_images_dir, exist_ok=True)
    os.makedirs(unscrambled_images_dir, exist_ok=True)
    os.makedirs(keys_dir, exist_ok=True)


    if args.action == 'scram':
    
        arg_image = os.path.normpath(args.image)
        

        
        if os.path.isfile(args.image):
            arg_image = cv2.imread(args.image)
            arg_key = logistic_map_key(arg_image.shape)
            scrambled_result = scram(arg_image, arg_key)
            cv2.imwrite(os.path.join(scrambled_images_dir, 'scrambled.png'), scrambled_result)
            np.save(os.path.join(keys_dir, 'key'),arg_key )


        elif os.path.isdir(arg_image):
            image_extensions = ('.png', '.jpeg', '.jpg', '.gif',
            '.tif', '.tiff', '.bmp', '.webp',
            '.raw', '.cr2', '.nef', '.heic', '.svg')
            list_of_images_to_scramble = [x for x in os.listdir(arg_image) if x.lower().endswith(image_extensions)]


            for x in range(len(list_of_images_to_scramble)):
                full_path_of_image = os.path.join(arg_image, list_of_images_to_scramble[x])
                image = cv2.imread(full_path_of_image)
                key = logistic_map_key(image.shape)
                scrambled_result = scram(image, key)
                cv2.imwrite(os.path.join(scrambled_images_dir, f'scrambled{x + 1}.png'), scrambled_result)
                np.save(os.path.join(keys_dir, f'key{x + 1}'), key)
        
        
        
            #Zip keys
            if args.zip_keys:
                with zipfile.ZipFile(f'keys{timestamp}.zip', 'w') as zip_file:
                    for key in os.listdir(keys_dir):
                        zip_file.write(os.path.join(keys_dir,key), arcname=key)
                        os.remove(os.path.join(keys_dir,key))
            #End Zip keys
        
            #Zip images
            if args.zip_images:
                with zipfile.ZipFile(f'scrambled_images{timestamp}.zip', 'w') as zip_file:
                    for image in os.listdir(scrambled_images_dir):
                        zip_file.write(os.path.join(scrambled_images_dir, image), arcname=image)
                        os.remove(os.path.join(scrambled_images_dir, image))
            #End Zip images




    elif args.action == 'unscram':
        
        arg_image = cv2.imread(args.image)
        arg_key = np.load(args.key)
        unscrambled_result = unscram(arg_image, arg_key)

        cv2.imwrite(os.path.join(unscrambled_images_dir, 'unscrambled.png'), unscrambled_result)


if __name__ == '__main__':
    main()
        

        