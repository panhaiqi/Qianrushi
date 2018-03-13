import numpy as np
from skimage import color,io
from skimage import img_as_ubyte,transform

def image_process(img):
    data = []
    img = io.imread(img)
    base_path = r'..\\Qianrushi\\'
    img = color.gray2rgb(img)
    img = img_as_ubyte(transform.resize(img, (224, 224, 3)))
    data.append(img)
    data = np.array(data)
    data = data.astype('float32')
    data /= 255.
    return data