from __future__ import print_function,division,unicode_literals
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.naive_bayes import MultinomialNB ,BernoulliNB
from sklearn.metrics import accuracy_score

#data path and file name
path = 'ex6DataPrepared/'
train_data_fn = 'train-features.txt'
test_data_fn = 'test-features.txt'
train_label_fn = 'train-labels.txt'
test_label_fn = 'test-labels.txt'

