# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import random

random.seed()
FILE_I_END = 7
offset = 63

data_order = [i for i in range(1, FILE_I_END + 1)]
shuffle(data_order)
for count, i in enumerate(data_order):
    try:
        random.seed()
        file_name = 'D:/training_data/hist_data_2/hist_2_taxi_training_data-{}.npy'.format(i)
        # full file info
        train_data = np.load(file_name, allow_pickle=True)
        print(file_name, len(train_data))
        df = pd.DataFrame(train_data)
        print(df.head())
        print(Counter(df[1].apply(str)))
        w = []
        s = []
        a = []
        d = []
        wa = []
        wd = []
        sa = []
        sd = []
        nk = []
        for data in train_data:
            img = data[0]
            choice = data[1]
            if choice == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
                w.append([img, choice])
                shuffle(w)
            elif choice == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
                s.append([img, choice])
                shuffle(s)
            elif choice == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
                a.append([img, choice])
                shuffle(a)
            elif choice == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
                d.append([img, choice])
                shuffle(d)
            elif choice == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
                wa.append([img, choice])
                shuffle(wa)
            elif choice == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
                wd.append([img, choice])
                shuffle(wd)
            elif choice == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
                sa.append([img, choice])
                shuffle(sa)
            elif choice == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
                sd.append([img, choice])
                shuffle(sd)
            elif choice == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
                nk.append([img, choice])
                shuffle(nk)
            else:
                print('no matches')
        w = w[:len(s)][:len(a)][:len(d)][:len(wa)][:len(wd)][:len(sa)][:len(sd)][:len(nk)]
        s = s[:len(w)]
        a = a[:len(w)]
        d = d[:len(w)]
        wa = wa[:len(w)]
        wd = wd[:len(w)]
        sa = sa[:len(w)]
        sd = sd[:len(w)]
        nk = nk[:len(w)]

        final_data = w + s + a + d + wa + wd + sa + sd + nk
        shuffle(final_data)
        np.save('D:/training_data/balanced_hist_taxi_training_data-{}.npy'.format(i+offset), final_data)

    except Exception as e:
        print(str(e))




