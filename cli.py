import pandas as pd
from DataPrepKit import read_csv, read_excel, read_json, data_summary, most_frequent_values, remove_missing_values, impute_missing_values, one_hot_encoding, label_encoding

data_path = input("Enter the path of the data file: ")

if data_path.endswith('.csv'):
    data = read_csv(data_path)
elif data_path.endswith('.xlsx'):
    data = read_excel(data_path)
elif data_path.endswith('.json'):
    data = read_json(data_path)
else:
    print("Unsupported file format")

summary = data_summary(data)
print("Summary Statistics:")
print(summary)


data_without_missing = remove_missing_values(data)
print("Data without missing values:")
print(data_without_missing.head())


data_imputed_mean = impute_missing_values(data)
print("Data with missing values imputed using mean:")
print(data_imputed_mean.head())


data_encoded = one_hot_encoding(data, columns=['categorical_column'])
print("Data after one-hot encoding:")
print(data_encoded.head())


data_labeled = label_encoding(data, columns=['categorical_column'])
print("Data after label encoding:")
print(data_labeled.head())
