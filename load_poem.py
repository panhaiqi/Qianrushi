#-*-coding:utf-8 * -
#随机获取一首诗
from random import randint
# global random_num

def load_poem(picture_class):
    random_num = 0
    if ((picture_class == 3) or (picture_class == 5)):
        random_num = randint(0,2)
    else:
        random_num = randint(0,3)
    # if ((picture_class == 0) or (picture_class == 1) or (picture_class == 2)):
    #     random_num = randint(0,6)
    # elif ((picture_class == 3) or (picture_class == 4) or (picture_class == 5)):
    #     random_num = randint(0,5)
    # elif (picture_class == 6):
    #     random_num = randint(0,4)
    # elif (picture_class == 7):
    #     random_num = randint(0,7)
    #add_path = 'gcode' + '\\'+ str(picture_class) +'\\'+ str(random_num) + '.txt'
    return random_num
