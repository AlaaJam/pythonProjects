# def main():
#     print("This is the CLI")
import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path)

def read_excel(file_path):
    return pd.read_excel(file_path)

def read_json(file_path):
    return pd.read_json(file_path)


def data_summary(data):
    return data.describe()

def most_frequent_values(data):
    return data.mode()


def remove_missing_values(data):
    return data.dropna()

def impute_missing_values(data, strategy='mean'):
    if strategy == 'mean':
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'mode':
        return data.fillna(data.mode().iloc[0])

def one_hot_encoding(data, columns):
    return pd.get_dummies(data, columns=columns)

def label_encoding(data, columns):
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    for col in columns:
        data[col] = encoder.fit_transform(data[col])
    return data




