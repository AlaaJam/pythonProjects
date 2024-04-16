import pandas as pd

def remove_missing_values(data):
    return data.dropna()

def impute_missing_values(data, strategy='mean'):
    if strategy == 'mean':
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'mode':
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Invalid imputation strategy. Supported strategies--> 'mean', 'median', 'mode'")