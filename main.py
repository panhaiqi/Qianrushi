# from predict import predict
from load_poem import load_poem
from load_music import load_music
from send_gcode import send_gcode
from sys import argv
from skimage import io
from load import load
from image_process import image_process
import numpy as np
# import datetime
# from keras.utils import plot_model

# import datetime
base_path = r'..\\Qianrushi\\'
model = load()
# print(model.summary())
# plot_model(model, to_file='model.png')
lst = [ 'he', 'zhu', 'moon', 'ju', 'lan', 'liu', 'mei', 'mountain']

while (1):
    img = input()
    # starttime = datetime.datetime.now()
    data = image_process(img)

    predict_result = np.argmax(model.predict(data))

    # endtime = datetime.datetime.now()
    # print (endtime - starttime)
    poem_num = load_poem(predict_result)
    #music_path = base_path + 'music' + '\\' + str(predict_result) + '\\' + str(poem_num) + '.mp3'
    music_path = base_path + 'music' + '\\' + str(7) + '\\' + str(3) + '.mp3'
    gcode_path = base_path + 'gcode' + '\\' + str(7) + '\\' + str(3) + '.txt'
    load_music(music_path)
    send_gcode(gcode_path)
    print('[result]:'+str(predict_result))
