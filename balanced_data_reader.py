import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

FILE_I_END = 1

data_order = [i for i in range(1, FILE_I_END + 1)]
shuffle(data_order)
for count, i in enumerate(data_order):
    try:
        file_name = 'training_data/raw_data/training_data-{}.npy'.format(i)
        # full file info
        train_data = np.load(file_name, allow_pickle=True)
        print(file_name, len(train_data))
        df = pd.DataFrame(train_data)
        print(df.head())
        print(Counter(df[1].apply(str)))
        print(df[0].apply(str))
    except Exception as e:
        print(str(e))