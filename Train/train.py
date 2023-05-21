import os
import main as main
import traindecisiontree as train_decision_tree
import trainknearestneighbors as train_k_nearest_neighbors
import traingaussiannativebayes as train_gaussian_native_bayes
import trainrandomforest as train_random_forest
import trainlinearregression as train_linear_regression


def train_options(data):
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------')
    print('----------------------------------Train models---------------------------------')
    print('-------------------------------------------------------------------------------\n')
    print('Algorithms:')
    print('1. K-Nearest Neighbors')
    print('2. Decision Tree')
    print('3. Random Forest Tree')
    print('4. Gaussian Native Bayes')
    print('5. Linear Regression')
    print('0. Go to home')
    while True:
        try:
            option = int(input('Please enter one option from above: '))
            if option == 0:
                main.custom_options_selector(data)
            if option == 1:
                train_k_nearest_neighbors.train(data)
            elif option == 2:
                train_decision_tree.train(data)
            elif option == 3:
                train_random_forest.train(data)
            elif option == 4:
                train_gaussian_native_bayes.train(data)
            elif option == 5:
                train_linear_regression.train(data)
        except Exception as e:
            print("That's not a valid option!" + str(e))
