# historical_data.py

import numpy as np
import pandas as pd
from collections import Counter


FILE_I_END = 1

data_order = [i for i in range(1, FILE_I_END + 1)]
for count, i in enumerate(data_order):
    try:
        file_name = 'training_data/raw_data/training_data-{}.npy'.format(i)
        train_data = np.load(file_name, allow_pickle=True)
        column_last = train_data[:][:-1]
        train_data = np.delete(train_data, 0, 0)
        # print(len(train_data))
        # print("-------------------------------------")
        # print(len(column_last))
        merged_data = np.hstack((train_data, column_last))
        np.save('training_data/hist_data/hist_training_data-{}.npy'.format(i), merged_data)

    except Exception as e:
        print(str(e))




