import os
import main as main
from sklearn import preprocessing

def encoding_options(data):
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------')
    print('-----------------------------------Encode dataset------------------------------')
    print('-------------------------------------------------------------------------------\n')
    print('Methods:')
    print('1. Label Encoding')
    print('2. One-Hot Encoding')
    print('0. Go to home')
    while True:
        try:
            option = int(input('Please enter one option from above: '))
            if option == 0:
                main.custom_options_selector(data)
                break
            elif option == 1:
                data = label_encoding(data)
                print('Label Encoding finished!')
            elif option == 2:
                data = one_hot_encoding(data)
                print('One-Hot Encoding finished!')
            else:
                print("That's not a valid option!")

        except:
            print("That's not a valid option!")


def label_encoding(data):
    # Encode labels (transform categorical data to numerical ones)
    le = preprocessing.LabelEncoder()
    for column_name in data.columns:
        if data[column_name].dtype == object:
            data[column_name] = le.fit_transform(data[column_name])
    return data


def one_hot_encoding(data):
    # Encode labels (transform categorical data to numerical ones)
    enc = preprocessing.OneHotEncoder()
    for column_name in data.columns:
        if data[column_name].dtype == object:
            data[column_name] = enc.fit_transform(data[column_name])
    return data
