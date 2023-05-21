import pandas as pd
import numpy as np


def load_dataset():
    # Load CSV file
    return pd.read_csv("./Datasets/online_shoppers_intention.csv")


def count_rows_columns(data):
    # Print the count of rows and columns of dataset
    print('-------------------------------------------------------------------------------')
    print('---------------------------Count of total rows and columns---------------------')
    print('-------------------------------------------------------------------------------\n')
    data_shape = data.shape;
    print('Total rows: ', data_shape[0])
    print('Total columns: ', data_shape[1])
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')


def dataset_details(data):
    # Print the details of the dataset
    print('-------------------------------------------------------------------------------')
    print('--------------------The details of each column of the dataset------------------')
    print('-------------------------------------------------------------------------------\n')
    print(data.describe())
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')


def count_category_columns(data):
    # Count the rows of each Revenue Category (for the training data)
    print('-------------------------------------------------------------------------------')
    print('----Total rows of each category (Before under/oversampling; TRAINING DATA)-----')
    print('-------------------------------------------------------------------------------\n')
    print('The total rows for True (category): ', len(data[data["Revenue"] == True]))
    print('The total rows for False (category): ', len(data[data["Revenue"] == False]))
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

def split(data):
    X = data[data.columns[:-1]].values
    y = data[data.columns[-1]].values
    data = np.hstack((X, np.reshape(y, (-1, 1))))
    return data, X, y