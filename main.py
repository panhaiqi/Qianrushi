from predict import predict
from load_poem import load_poem
from load_music import load_music
from send_gcode import send_gcode
from sys import argv
from skimage import io
from load import load
from image_process import image_process
import numpy as np
# import datetime
base_path = r'..\\Qianrushi\\'
model = load()
while (1):
    img = input()

    data = image_process(img)

    predict_result = np.argmax(model.predict(data))

    poem_num = load_poem(predict_result)
    music_path = base_path + 'music' + '\\' + str(predict_result) + '\\' + str(poem_num) + '.ogg'
    synthesis_path = base_path + 'synthesis' + '\\' + str(predict_result) + '\\' + str(poem_num) + '.wav'
    gcode_path = base_path + 'gcode' + '\\' + str(predict_result) + '\\' + str(poem_num) + '.txt'
    load_music(music_path, synthesis_path)
    send_gcode(gcode_path)
