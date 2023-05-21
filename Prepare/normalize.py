import os
import main as main
from sklearn.preprocessing import StandardScaler


def normalize_options(data):
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------')
    print('--------------------------------Normalize dataset------------------------------')
    print('-------------------------------------------------------------------------------\n')
    print('Methods:')
    print('1. Standard Scaler')
    print('0. Go to home')
    while True:
        try:
            option = int(input('Please enter one option from above: '))
            if option == 0:
                main.custom_options_selector(data)
                break
            elif option == 1:
                data = normalize_standard_scaler(data)
                print('Normalizing using Standard Scaler finished!')
            else:
                print("That's not a valid option!")

        except:
            print("That's not a valid option!")




def normalize_standard_scaler(data):
    # Normalize the dataset
    scaler = StandardScaler()
    # Get only the numerical columns
    numerical_dataset = data[data.columns[:-1]].select_dtypes(include='number')
    # Transform (normalize) the numerical columns
    data[numerical_dataset.columns] = scaler.fit_transform(numerical_dataset)

    return data
