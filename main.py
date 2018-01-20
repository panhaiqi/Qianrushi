from predict import predict
from load_poem import load_poem
from load_music import load_music
from send_gcode import send_gcode
from sys import argv
from skimage import io
base_path = r'..\\Qianrushi\\'
img = io.imread(argv[1])
predict_result = predict(img)
poem_num = load_poem(predict_result)
music_path = base_path + 'music' + '\\'+ str(predict_result)+'\\'+str(poem_num)+'.mp3'
synthesis_path = base_path + 'synthesis' + '\\'+ str(predict_result)+'\\'+str(poem_num)+'.mp3'
gcode_path = base_path + 'gcode' + '\\'+ str(predict_result) +'\\'+ str(poem_num) + '.txt'
load_music(music_path)
load_music(synthesis_path)
send_gcode(gcode_path)