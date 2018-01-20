#-*-coding:utf-8 * -
#随机获取一首诗的g代码
from random import randint

def load_poem(picture_class):
    random_num = randint(0,3)
    add_path = 'gcode' + '\\'+ str(picture_class) +'\\'+ str(random_num) + '.txt'
    return random_num,add_path
