#-*-coding:utf-8 * -
from keras.models import Model, load_model
#from LoadData import load_data
from keras.applications.mobilenet import relu6,DepthwiseConv2D
from skimage import img_as_ubyte,transform
# import numpy as np
#from sys import argv
import numpy as np
from skimage import color
import datetime

def predict(img):
    data = []

    img = color.gray2rgb(img)
    img = img_as_ubyte(transform.resize(img, (224,224,3)))
    data.append(img)
    data = np.array(data)
    data = data.astype('float32')
    data /= 255.

    model = load_model('mobilenet_add.hdf5',custom_objects={
                  'relu6': relu6,
                  'DepthwiseConv2D': DepthwiseConv2D})
    # endtime1 = datetime.datetime.now()
    starttime = datetime.datetime.now()
    predict_list = model.predict(data)
    endtime2 = datetime.datetime.now()
    # print(endtime1 - starttime)
    print(endtime2 - starttime)
    return np.argmax(predict_list)

