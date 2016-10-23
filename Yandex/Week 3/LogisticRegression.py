
#!/usr/bin/python3

import math
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier


np.set_printoptions(suppress=True)
data = pd.read_csv('D:\\Dropbox\\Study\\Programming\\Coursera\\Machine-Learning\\Yandex\\Week 3\\data\\data-logistic.csv', names=None, header=None)

data = data.as_matrix().astype(float)

X = data[:, 1:]
y = data[:, 0]


# # print(X)
# lr = LogisticRegression(C=10)
# clf_l2_LR = lr.fit(X, y,sample_weight= [0,0])
# coef_l2_LR = clf_l2_LR.score(X,y)

# print(coef_l2_LR)
# #0.487804878049

sg = SGDClassifier(penalty=None, loss="log", alpha=1/(10*X.shape[0]), n_iter=10000) #, class_weight={1:0}
sg.fit(X, y)





#l2 = 0.487804878049