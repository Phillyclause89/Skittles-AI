import numpy as np
from grabscreen import grab_screen
import cv2
import time
import os
import pandas as pd
#from tqdm import tqdm
from collections import deque
from models import inception_v3 as googlenet
from random import shuffle

FILE_I_END = 1

WIDTH = 960
HEIGHT = 270
LR = 1e-3
EPOCHS = 1

MODEL_NAME = 'pygta5-{}-{}-{}-epochs-1-hist_data.model'.format(LR, 'googlenet',EPOCHS)
PREV_MODEL = 'pygta5-{}-{}-{}-epochs-1-hist_data.model'.format(LR, 'googlenet',EPOCHS)

LOAD_MODEL = False

wl = 0
sl = 0
al = 0
dl = 0

wal = 0
wdl = 0
sal = 0
sdl = 0
nkl = 0

w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
nk = [0, 0, 0, 0, 0, 0, 0, 0, 1]

model = googlenet(WIDTH, HEIGHT, 3, LR, output=9, model_name=MODEL_NAME)

if LOAD_MODEL:
    model.load(PREV_MODEL)
    print('We have loaded a previous model!!!!')

# iterates through the training files


for e in range(EPOCHS):
    # data_order = [i for i in range(1,FILE_I_END+1)]
    data_order = [i for i in range(1, FILE_I_END + 1)]
    shuffle(data_order)
    for count, i in enumerate(data_order):

        try:
            file_name = 'training_data/hist_data/hist_training_data-{}.npy'.format(i)
            # full file info
            train_data = np.load(file_name, allow_pickle=True)
            print(file_name, len(train_data))

            ##            # [   [    [FRAMES], CHOICE   ]    ]
            ##            train_data = []
            ##            current_frames = deque(maxlen=HM_FRAMES)
            ##
            ##            for ds in data:
            ##                screen, choice = ds
            ##                gray_screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
            ##
            ##
            ##                current_frames.append(gray_screen)
            ##                if len(current_frames) == HM_FRAMES:
            ##                    train_data.append([list(current_frames),choice])

            # #
            # always validating unique data: 
            # shuffle(train_data)
            train = train_data[:-2500]
            test = train_data[-2500:]

            X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3)
            Y = [i[1] for i in train]


            test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
            test_y = [i[1] for i in test]

            model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
                      snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

            if count % 10 == 0:
                print('SAVING MODEL!')
                model.save(MODEL_NAME)

        except Exception as e:
            print(str(e))

#

# cd C:\Users\Philip\PycharmProjects\PythonPlays\venv\Lib\site-packages
# python -m tensorboard.main --logdir=foo:C:\Users\Philip\PycharmProjects\pygta5\log
