#pip install pandas
# dataset from https://www.kaggle.com/datasets/dnkumars/cybersecurity-intrusion-detection-dataset
import pandas as pd

df = pd.read_csv('cybersecurity_intrusion_data.csv')

print(df.head())

print(df.columns)