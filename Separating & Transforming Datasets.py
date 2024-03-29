# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:47:20 2019

@author: M7md_Karam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
x = dataset.iloc [: , :-1].values
y = dataset.iloc[:, 3].values
#iloc separates values


#syket learn
from sklearn.preprocessing import Imputer
imputer = Imputer (missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[: , 1:3])
x[: , 1:3] = imputer.transform (x[: , 1:3])

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[: , 0] = labelencoder_x.fit_transform(x[: , 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
