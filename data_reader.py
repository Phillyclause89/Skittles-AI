import numpy as np
import pandas as pd
from collections import Counter

FILE_I_START = 1
FILE_I_END = 2
d = Counter()
data_order = [i for i in range(FILE_I_START, FILE_I_END + 1)]

for count, i in enumerate(data_order):
    try:
        file_name = r'D:\training_data\raw_data\taxi_training_data-{}.npy'.format(i)
        # full file info
        train_data = np.load(file_name, allow_pickle=True)
        print(file_name, len(train_data))
        df = pd.DataFrame(train_data)
        print(df.head())
        c = Counter(df[1].apply(str))
        d.update(c)
        print(c)
        # print(df[0].apply(str))
    except Exception as e:
        print(str(e))

print("Totals across all files read:", d)
