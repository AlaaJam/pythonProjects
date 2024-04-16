# src/data_summary.py

import pandas as pd

def generate_summary(data):
    return data.describe()

def most_frequent_values(data):
    return data.mode()