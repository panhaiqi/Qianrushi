import os
import numpy as np
from skimage import io, transform, img_as_ubyte,color
import threading

NUM_THREAD = 8

def scan_files(directory, prefix=None, postfix='.jpg'):
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(os.path.abspath(directory), special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(os.path.abspath(directory), special_file))
            else:
                files_list.append(os.path.join(os.path.abspath(directory), special_file))
    print(len(files_list))
    return files_list

def image_norm(image, image_size):
    return img_as_ubyte(transform.resize(image, image_size))

def filename_to_label(file):
    lst = ['bird', 'he', 'zhu', 'horse', 'ju', 'lan', 'liu', 'mei', 'mountain']
    name = os.path.basename(file)
    label = np.zeros(len(lst))
    for i in range(len(lst)):
        if lst[i] in name:
            label[i] = 1
            print(lst[i])
    return  label

def get_photo_data(file_list, image_size=(224, 224)):
    data, Label = [], []
    source = file_list
    lock = threading.Lock()
    def work(i):
        file = source.pop(0)
        try:
            img = io.imread(file)
            img = color.gray2rgb(img)
            img = image_norm(img, image_size)
            label = filename_to_label(file)
        except:
            print('Load', file, 'fail')
            return
        if img.shape != (image_size[0], image_size[1], 3):
            return
        lock.acquire()
        data.append(img)
        Label.append(label)
        lock.release()
    try:
        from multiprocessing.pool import ThreadPool
        multi_available = True
    except ImportError:
        print('multiprocessing not available, fall back to single threaded encoding')
        multi_available = False

    if multi_available and NUM_THREAD > 0:
        p = ThreadPool(NUM_THREAD)
        p.map(work, [i for i in range(len(source))])
    else:
        for _ in range(len(source)):
            work(_)
    data = np.array(data)
    Label = np.array(Label)
    assert data.shape[0] == Label.shape[0]
    print(data.shape, Label.shape)
    return data, Label

def load_data(path):
    import random
    if os.path.exists('X.npy') and os.path.exists('Y.npy'):
        X = np.load('X.npy')
        Y = np.load('Y.npy')
    else:
        X, Y = get_photo_data(scan_files(path))
        np.save('X.npy', X)
        np.save('Y.npy', Y)
    Len = X.shape[0]
    index = [i for i in range(Len)]
    random.shuffle(index)
    X = X[index]
    Y = Y[index]
    t_size = int(Len * 0.8)
    x_train = X[:t_size,:,:,:]
    x_test = X[t_size+1:,:,:,:]
    y_train = Y[:t_size,:]
    y_test = Y[t_size+1:,:]

    try:
        os.mkdir('overview')
    except:
        pass
    for i in range(10):
        io.imsave('overview/' + str(i) + '.jpg', X[i,:,:,:])
    return (x_train, y_train), (x_test, y_test)