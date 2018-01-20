#-*-coding:utf-8 * -
from keras.models import Model, load_model
from LoadData import load_data
from keras.applications.mobilenet import relu6,DepthwiseConv2D
from skimage import img_as_ubyte,transform
import numpy as np
from sys import argv
import numpy as np

def predict(argv[0]):
    data = []
    data.append(img_as_ubyte(transform.resize(argv, (224,224,3))))
    data = data.astype('float32')
    data /= 255.

    model = load_model('mobilenet_add.hdf5',custom_objects={
                  'relu6': relu6,
                  'DepthwiseConv2D': DepthwiseConv2D})

    predict_list = model.predict(data)

    return np.argmax(predict_list)

