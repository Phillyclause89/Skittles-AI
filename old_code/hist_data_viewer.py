import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

FILE_I_END = 1

data_order = [i for i in range(1, FILE_I_END + 1)]
for count, i in enumerate(data_order):
    try:
        file_name = 'training_data/hist_data/hist_training_data-{}.npy'.format(i)
        train_data = np.load(file_name, allow_pickle=True)
        for data in train_data:
            img = data[0]
            choice = data[1]
            last_img = data[2]
            last_choice = data[3]
            if choice == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
                choice_img = 'key_images/w.png'
            elif choice == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
                choice_img = 'key_images/s.png'
            elif choice == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
                choice_img = 'key_images/a.png'
            elif choice == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
                choice_img = 'key_images/d.png'
            elif choice == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
                choice_img = 'key_images/aw.png'
            elif choice == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
                choice_img = 'key_images/dw.png'
            elif choice == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
                choice_img = 'key_images/as.png'
            elif choice == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
                choice_img = 'key_images/ds.png'
            elif choice == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
                choice_img = 'key_images/nk.png'
            else:
                print('no matches')
            img2 = cv2.imread(choice_img)
            img2 = cv2.resize(img2, (250, 270))
            images_1_2_h = np.concatenate((img, img2), axis=1)
            cv2.imshow('current_event', images_1_2_h)

            if last_choice == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
                last_choice_img = 'key_images/w.png'
            elif last_choice == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
                last_choice_img = 'key_images/s.png'
            elif last_choice == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
                last_choice_img = 'key_images/a.png'
            elif last_choice == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
                last_choice_img = 'key_images/d.png'
            elif last_choice == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
                last_choice_img = 'key_images/aw.png'
            elif last_choice == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
                last_choice_img = 'key_images/dw.png'
            elif last_choice == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
                last_choice_img = 'key_images/as.png'
            elif last_choice == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
                last_choice_img = 'key_images/ds.png'
            elif last_choice == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
                last_choice_img = 'key_images/nk.png'
            else:
                print('no matches')
            img3 = cv2.imread(last_choice_img)
            img3 = cv2.resize(img3, (250, 270))
            images_3_4_h = np.concatenate((last_img, img3), axis=1)
            cv2.imshow('last_event', images_3_4_h)

            print(last_choice)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    except Exception as e:
        print(str(e))
