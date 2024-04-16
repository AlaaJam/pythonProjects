import pandas as pd

def one_hot_encoding(data, columns):
    return pd.get_dummies(data, columns=columns)

def label_encoding(data, column):
    labels = data[column].astype('category').cat.codes
    return labels