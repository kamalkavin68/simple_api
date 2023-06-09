import pandas as pd

def read_data():
    df = pd.read_csv("./HINDALCO.csv").to_dict("records")
    return df