# historical_data.py

import numpy as np
import cv2


FILE_I_END = 1

data_order = [i for i in range(1, FILE_I_END + 1)]
for count, i in enumerate(data_order):
    file_name = 'training_data/raw_data/training_data-{}.npy'.format(i)
    train_data = np.load(file_name, allow_pickle=True)
    column_last = train_data[:][:-1]
    train_data = np.delete(train_data, 0, 0)
    merged_data = np.hstack((train_data, column_last))
    final_data = []

    for data in merged_data:
        print(data)
        img1 = data[0]
        img2 = data[2]
        last_input = data[3]
        current_input = data[1]
        vis = np.concatenate((img1, img2), axis=1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        last = []
        if last_input == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
            last = 'W'
        elif last_input == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
            last = 'SS'
        elif last_input == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
            last = 'AAA'
        elif last_input == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
            last = 'DDDD'
        elif last_input == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
            last = 'WAWAWA'
        elif last_input == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
            last = 'WDWDWDWD'
        elif last_input == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
            last = 'SASASASASA'
        elif last_input == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
            last = 'SDSDSDSDSDSD'
        elif last_input == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
            last = 'NKNKNKNKNKNKNK'
        cv2.putText(vis, str(last), (10,10), font, 1, (255, 0, 0), 3, cv2.LINE_AA)
        final_data.append([vis, current_input])

    print("Saving")
    np.save('training_data/hist_data/hist_training_data-{}.npy'.format(i), final_data)
