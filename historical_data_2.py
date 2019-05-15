# historical_data.py

import numpy as np
import cv2


FILE_I_END = 1
FILE_I_START = 0

data_order = [i for i in range(FILE_I_START + 1, FILE_I_END + 1)]
for count, i in enumerate(data_order):
    file_name = r'D:\training_data\raw_data\training_data-{}.npy'.format(i)
    train_data = np.load(file_name, allow_pickle=True)
    column_last = train_data[:][:-1]
    train_data = np.delete(train_data, 0, 0)
    column_2nd_last = column_last[:][:-1]
    train_data = np.delete(train_data, 0, 0)
    column_last = np.delete(column_last, 0, 0)
    column_3rd_last = column_2nd_last[:][:-1]
    train_data = np.delete(train_data, 0, 0)
    column_last = np.delete(column_last, 0, 0)
    column_2nd_last = np.delete(column_2nd_last, 0, 0)
    #                            Source Var:   image, input
    #                      -----------------------------------
    #                            train_data: data[0], data[1]
    #                           column_last: data[2], data[3]
    #                       column_2nd_last: data[4], data[5]
    #                       column_3rd_last: data[6], data[7]
    merged_data = np.hstack((train_data, column_last, column_2nd_last, column_3rd_last))
    final_data = []

    for data in merged_data:
        print(data)
        img1 = data[0]
        img2 = data[2]
        img3 = data[4]
        img4 = data[6]
        last_input = data[3]
        _2nd_last_input = data[5]
        _3rd_last_input = data[7]
        current_input = data[1]
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
        cv2.putText(img2, str(last), (10,10), font, 1, (0, 0, 255), 3, cv2.LINE_AA)
        _2nd_last = []
        if _2nd_last_input == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
            _2nd_last = 'W'
        elif _2nd_last_input == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
            _2nd_last = 'SS'
        elif _2nd_last_input == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
            _2nd_last = 'AAA'
        elif _2nd_last_input == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
            _2nd_last = 'DDDD'
        elif _2nd_last_input == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
            _2nd_last = 'WAWAWA'
        elif _2nd_last_input == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
            _2nd_last = 'WDWDWDWD'
        elif _2nd_last_input == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
            _2nd_last = 'SASASASASA'
        elif _2nd_last_input == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
            _2nd_last = 'SDSDSDSDSDSD'
        elif _2nd_last_input == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
            _2nd_last = 'NKNKNKNKNKNKNK'
        cv2.putText(img3, str(_2nd_last), (10, 10), font, 1, (0, 0, 255), 3, cv2.LINE_AA)
        _3rd_last = []
        if _3rd_last_input == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
            _3rd_last = 'W'
        elif _3rd_last_input == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
            _3rd_last = 'SS'
        elif _3rd_last_input == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
            _3rd_last = 'AAA'
        elif _3rd_last_input == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
            _3rd_last = 'DDDD'
        elif _3rd_last_input == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
            _3rd_last = 'WAWAWA'
        elif _3rd_last_input == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
            _3rd_last = 'WDWDWDWD'
        elif _3rd_last_input == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
            _3rd_last = 'SASASASASA'
        elif _3rd_last_input == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
            _3rd_last = 'SDSDSDSDSDSD'
        elif _3rd_last_input == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
            _3rd_last = 'NKNKNKNKNKNKNK'
        cv2.putText(img4, str(_3rd_last), (10, 10), font, 1, (0, 0, 255), 3, cv2.LINE_AA)
        vis0 = np.concatenate((img1, img2), axis=1)
        vis1 = np.concatenate((img3, img4), axis=1)
        final_vis = np.concatenate((vis0, vis1), axis=0)
        final_vis = cv2.resize(final_vis, (480, 270))

        final_data.append([final_vis, current_input])

    print("Saving")
    np.save(r'D:\training_data\hist_data_2\hist_2_training_data-{}.npy'.format(i), final_data)
