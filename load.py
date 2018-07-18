#-*-coding:utf-8 * -
from tensorflow.python.keras.models import Model, load_model
from tensorflow.python.keras._impl.keras.applications.mobilenet import relu6,DepthwiseConv2D
# from skimage import img_as_ubyte,transform

# import datetime
# starttime = datetime.datetime.now()
def load():
    model = load_model('mobilenet.hdf5',custom_objects={
                  'relu6': relu6,
        'DepthwiseConv2D': DepthwiseConv2D})
    return model

