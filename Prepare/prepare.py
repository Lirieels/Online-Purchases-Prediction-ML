import os
import main as main
import dataset as dataset
import normalize as normalize


def prepare_options(data):
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------')
    print('----------------------------------Prepare dataset------------------------------')
    print('-------------------------------------------------------------------------------\n')
    print('Algorithms:')
    print('1. Remove zero rows')
    print('2. Normalize')
    print('0. Go to home')
    while True:
        try:
            option = int(input('Please enter one option from above: '))
            if (option == 1 or option == 2 or option == 0):
                break
            print("That's not a valid option!")
        except:
            print("That's not a valid option!")

    if option == 0:
        main.options_selector(data)
    elif option == 1:
        dataset.count_rows_columns(data)
        data = remove_zero_rows(data)
        dataset.count_rows_columns(data)
    elif option == 2:
        normalize.normalize_options(data)

def remove_zero_rows(data):
    # remove rows where the specified columns have values of 0
    for index, row in data.iterrows():
        if (row['Administrative'] == 0 and row['Administrative_Duration'] == 0 and row['Informational'] == 0 and
                row['Informational_Duration'] == 0 and row['ProductRelated'] == 0 and row[
                    'ProductRelated_Duration'] == 0
                and row['BounceRates'] == 0 and row['ExitRates'] == 0 and row['PageValues'] == 0):
            data.drop(index, inplace=True)

    return data
