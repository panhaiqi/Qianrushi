#-*-coding:utf-8 * -
from keras.models import Model, load_model

from keras.applications.mobilenet import relu6,DepthwiseConv2D
from skimage import img_as_ubyte,transform

# import datetime
# starttime = datetime.datetime.now()
def load():
    model = load_model('mobilenet_add.hdf5',custom_objects={
                  'relu6': relu6,
                  'DepthwiseConv2D': DepthwiseConv2D})
    return model

