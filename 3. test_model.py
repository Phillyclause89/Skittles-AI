from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
from models import inception_v3 as googlenet
from getkeys import key_check
from collections import deque, Counter
import random
from statistics import mode, mean
import numpy as np

GAME_WIDTH = 1920
GAME_HEIGHT = 1080

WIDTH = 480
HEIGHT = 270
LR = 1e-3
EPOCHS = 4

w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
nk = [0, 0, 0, 0, 0, 0, 0, 0, 1]


def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(S)


def left():
    ReleaseKey(W)
    PressKey(A)
    ReleaseKey(S)
    ReleaseKey(D)
    # ReleaseKey(S)


def right():
    ReleaseKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)


def reverse():
    PressKey(S)
    ReleaseKey(A)
    ReleaseKey(W)
    ReleaseKey(D)


def forward_left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(S)


def forward_right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)


def reverse_left():
    PressKey(S)
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)


def reverse_right():
    PressKey(S)
    PressKey(D)
    ReleaseKey(W)
    ReleaseKey(A)


def no_keys():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)


model = googlenet(WIDTH, HEIGHT, 3, LR, output=9)
MODEL_NAME = 'pygta5-{}-{}-{}-epochs-17-balanced_data.model'.format(LR, 'googlenet', EPOCHS)
model.load(MODEL_NAME)

print('We have loaded a previous model!!!!')


def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    paused = False
    mode_choice = 0

    while (True):

        if not paused:
            screen = grab_screen(region=(0, 40, GAME_WIDTH, GAME_HEIGHT + 40))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            screen = cv2.resize(screen, (WIDTH, HEIGHT))

            prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 3)])[0]
            prediction = np.array(prediction) #* np.array([1.12, 1, 1, 1, 1, 1, 1, 1, 0.2])
            print(prediction)
            # div = 4
            # wplus = prediction[0] + (prediction[4] / div) + (prediction[5] / div)
            # print(wplus)
            # splus = prediction[1] + (prediction[6] / div) + (prediction[7] / div)
            # print(splus)
            # aplus = prediction[2] + (prediction[6] / div) + (prediction[4] / div)
            # print(aplus)
            # dplus = prediction[3] + (prediction[5] / div) + (prediction[7] / div)
            # print(dplus)
            # waplus = prediction[4] + (prediction[0] / div) + (prediction[2] / div)
            # print(waplus)
            # wdplus = prediction[5] + (prediction[0] / div) + (prediction[3] / div)
            # print(wdplus)
            # saplus = prediction[6] + (prediction[2] / div) + (prediction[1] / div)
            # print(saplus)
            # sdplus = prediction[7] + (prediction[1] / div) + (prediction[3] / div)
            # print(sdplus)
            #
            # mode_choice_v2 = np.argmax([wplus, splus, aplus, dplus, waplus, wdplus, saplus, sdplus])
            # print(mode_choice_v2)

            mode_choice = np.argmax(prediction)
            print(mode_choice)

            if mode_choice == 0:
                straight()
                choice_picked = 'straight'
                print(choice_picked)

            elif mode_choice == 1:
                reverse()
                choice_picked = 'reverse'
                print(choice_picked)

            elif mode_choice == 2:
                left()
                choice_picked = 'left'
                print(choice_picked)

            elif mode_choice == 3:
                right()
                choice_picked = 'right'
                print(choice_picked)

            elif mode_choice == 4:
                forward_left()
                choice_picked = 'forward+left'
                print(choice_picked)

            elif mode_choice == 5:
                forward_right()
                choice_picked = 'forward+right'
                print(choice_picked)

            elif mode_choice == 6:
                reverse_left()
                choice_picked = 'reverse+left'
                print(choice_picked)

            elif mode_choice == 7:
                reverse_right()
                choice_picked = 'reverse+right'
                print(choice_picked)

            elif mode_choice == 8:
                no_keys()
                choice_picked = 'nokeys'
                print(choice_picked)

        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
                print("Unpaused")
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)
                print("Paused")


main()
