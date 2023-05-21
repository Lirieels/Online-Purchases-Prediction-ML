import os
import main as main
import decisiontreemodel as decision_tree_model
import linearregressionmodel as linear_regression_model
import knearestneighborsmodel as k_nearest_neighbors_model
import gaussiannativebayesmodel as gaussian_native_bayes_model
import randomforestmodel as random_forest_model


def load_models(data):
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------')
    print('-----------------------------------Load models---------------------------------')
    print('-------------------------------------------------------------------------------\n')

    while True:
        try:
            print('Models:')
            print('1. K-Nearest Neighbors')
            print('2. Decision Tree')
            print('3. Random Forest Tree')
            print('4. Gaussian Native Bayes')
            print('5. Linear Regression')
            print('0. Go to home')
            option = int(input('Please enter one option from above: '))
            if option == 0:
                main.options_selector(data)
            elif option == 1:
                k_nearest_neighbors_model.get_models(data)
            elif option == 2:
                decision_tree_model.get_models(data)
            elif option == 3:
                random_forest_model.get_models(data)
            elif option == 4:
                gaussian_native_bayes_model.get_models(data)
            elif option == 5:
                linear_regression_model.get_models(data)
        except Exception as e:
            print("That's not a valid option!" + str(e))
