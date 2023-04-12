import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
from typing import List
from zlib import crc32


def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio* 2**32

def split_data_with_id_hash(data, test_ratio):
    ids = data.index.to_series()
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

def stratified_clf_cv_accuracy(model, 
                         X_train: np.ndarray, 
                         y_train: np.ndarray,
                         n_splits: int=3, 
                         shuffle: bool=False, 
                         random_state: int=None) -> np.ndarray:
    
    return_ = []
    skfolds = StratifiedKFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
    for train_index, val_index in skfolds.split(X_train, y_train):
        clone_model = clone(model)
        X_train_folds = X_train[train_index]
        y_train_folds = y_train[train_index]
        X_val_fold = X_train[val_index]
        y_val_fold = y_train[val_index]
        clone_model.fit(X_train_folds, y_train_folds)
        y_pred = clone_model.predict(X_val_fold)
        n_correct = sum(y_pred == y_val_fold)
        return_.append(n_correct/len(y_pred))
    return np.array(return_)

