#-*-coding:utf-8 * -
from keras.models import Model, load_model
#from LoadData import load_data
from keras.applications.mobilenet import relu6,DepthwiseConv2D
from skimage import img_as_ubyte,transform
import numpy as np
#from sys import argv
import numpy as np
from skimage import color

def predict(img):
    lst = ['鸟', '荷', '竹', '马', '菊', '兰', '柳', '梅', '山']
    data = []
    #img = color.gray2rgb(argv)
    #data = []
    #data.append(img_as_ubyte(transform.resize(argv, (224,224,3))))
    #img = io.imread(argv[1])
    img = color.gray2rgb(img)
    img = img_as_ubyte(transform.resize(img, (224,224,3)))
    data.append(img)
    data = np.array(data)
    data = data.astype('float32')
    data /= 255.

    model = load_model('mobilenet_add.hdf5',custom_objects={
                  'relu6': relu6,
                  'DepthwiseConv2D': DepthwiseConv2D})

    predict_list = model.predict(data)
    print(lst[np.argmax(predict_list)].encode('utf-8').decode('utf-8'))
    return np.argmax(predict_list)

