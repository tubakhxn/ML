import numpy as np
import pandas as pd
import matplotlib . pyplot as plt
import seaborn as sns
import random

df = pd.read.csv ( 'iris. csv' )
df = df.drop('Id' , axis=1)
df = df.rename ( columns={ 'Species': 'Lable' })

def train_test_split(df, test_size):
    indices= df.index.tolist()
    test_indices=random.sample(population=indices, k=test_size)
    test_df= df.loc(test_indices)
    train_df= df.drop(test_indices)
    return train_df, test_df

def classify_data(data):
    label_column = data [:, -1]
    unique_classes, counts_unique_classes= np.unique(label_column, return_counts=True)
    index=counts_unique_classes.argmax()
    classification=unique_classes[index]
    return classification

label_column=data[:,-1]


