from predict import predict
from load_poem import load_poem
from load_music import load_music
from send_gcode import send_gcode
from sys import argv
base_path = r'..\\Qianrushi\\'

predict_result = predict(argv)
poem_num,add_path = load_poem(predict_result)
music_path = base_path + 'music' + '\\'+ str(predict_result)+'\\'+str(poem_num)+'.mp3'
gcode_path = base_path + 'gcode' + '\\'+ str(picture_class) +'\\'+ str(random_num) + '.txt'
load_music(music_path)
send_gcode(gcode_path)