import imageio
import os
import matplotlib.pyplot as plt
import numpy as np

def loadImages(dirName, class_mode='emotion'):
    '''
    # This function loads images from any directory
    # :param str dirName: is address of the directory (string)
    # :param str class_mode: is the classification mode (emotion or recognition) (string)
    '''
    assert class_mode in ['emotion', 'recognition'], "Class mode should be either 'emotion' or 'recognition'."
    data = []
    label = []
    for root, dirs, files in os.walk(dirName):
        for file in files:
            #face = scipy.misc.imread(os.path.join(root, file)) # Load image from a path
            face = imageio.imread(os.path.join(root, file))
            face = face.reshape(256 * 256, ).tolist()          # Flatten image. Note: size of any image is 256,256
            data.append(face)
            if class_mode == 'recognition':
                label.append(file.split('.')[0])
            if class_mode == 'emotion':
                label.append(file.split('.')[1][:2])
    return np.asarray(data) , label
