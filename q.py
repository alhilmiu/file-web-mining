import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np

dataframe = pd.read_excel('mainbasket_vsmsatufitur.xlsx')

dataframe.to_csv('baru.csv')
