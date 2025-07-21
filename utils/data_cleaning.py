import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')
    return df
