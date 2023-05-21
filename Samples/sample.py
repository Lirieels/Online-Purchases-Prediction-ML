import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
def use_sample():
    # Set up the pandas table (for terminal printing)
    desired_width = 2000
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', 20)

    # Load CSV file
    online_shoppers_intention = pd.read_csv(r"./Datasets/online_shoppers_intention.csv")

    # Print the count of rows and columns of dataset
    print('-------------------------------------------------------------------------------')
    print('---------Count of total rows and columns (before removing zero rows)-----------')
    print('-------------------------------------------------------------------------------\n')
    online_shoppers_intention_shape = online_shoppers_intention.shape;
    print('Total rows: ', online_shoppers_intention_shape[0])
    print('Total columns: ', online_shoppers_intention_shape[1])
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

    # remove rows where the specified columns have values of 0
    for index, row in online_shoppers_intention.iterrows():
        if (row['Administrative'] == 0 and row['Administrative_Duration'] == 0 and row['Informational'] == 0 and
                row['Informational_Duration'] == 0 and row['ProductRelated'] == 0 and row['ProductRelated_Duration'] == 0
                and row['BounceRates'] == 0 and row['ExitRates'] == 0 and row['PageValues'] == 0):
            online_shoppers_intention.drop(index, inplace=True)

    # Print the count of rows and columns of dataset
    print('-------------------------------------------------------------------------------')
    print('----------Count of total rows and columns (after removing zero rows)-----------')
    print('-------------------------------------------------------------------------------\n')
    online_shoppers_intention_shape = online_shoppers_intention.shape;
    print('Total rows: ', online_shoppers_intention_shape[0])
    print('Total columns: ', online_shoppers_intention_shape[1])
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

    # Print the details of the dataset
    print('-------------------------------------------------------------------------------')
    print('--------------------The details of each column of the dataset------------------')
    print('-------------------------------------------------------------------------------\n')
    print(online_shoppers_intention.describe())
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

    # Split the dataset into training, validation and testing data
    train, valid, test = np.split(online_shoppers_intention.sample(frac=1),
                                  [int(0.6 * len(online_shoppers_intention)), int(0.8 * len(online_shoppers_intention))])

    print('-------------------------------------------------------------------------------')
    print('-------------------------------------Lengths-----------------------------------')
    print('-------------------------------------------------------------------------------\n')
    print('Length of the training data: ', len(train))
    print('Length of the validation data: ', len(valid))
    print('Length of the testing data: ', len(test))
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

    # Count the rows of each Revenue Category (for the training data)
    print('-------------------------------------------------------------------------------')
    print('----Total rows of each category (Before under/oversampling; TRAINING DATA)-----')
    print('-------------------------------------------------------------------------------\n')
    print('The total rows for True (category): ', len(train[train["Revenue"] == True]))
    print('The total rows for False (category): ', len(train[train["Revenue"] == False]))
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')


    def normailze_oversample(dataframe, oversample=False):



        # Normalize the dataset
        scaler = StandardScaler()
        # Get only the numerical columns
        numerical_dataset = dataframe[dataframe.columns[:-1]].select_dtypes(include='number')
        # Transform (normalize) the numerical columns
        dataframe[numerical_dataset.columns] = scaler.fit_transform(numerical_dataset)

        # Encode labels (transform categorical data to numerical ones)
        le = preprocessing.LabelEncoder()
        for column_name in dataframe.columns:
            if dataframe[column_name].dtype == object:
                dataframe[column_name] = le.fit_transform(dataframe[column_name])

        # Split the dataset into X and y
        X = dataframe[dataframe.columns[:-1]].values
        y = dataframe[dataframe.columns[-1]].values

        # Under/over sample the dataset
        if oversample:
            ros = RandomOverSampler()
            X, y = ros.fit_resample(X, y)

        # Stack the array
        data = np.hstack((X, np.reshape(y, (-1, 1))))
        return data, X, y


    train, X_train, y_train = normailze_oversample(train, True)
    test, X_test, y_test = normailze_oversample(test, False)

    # Count the rows of each Revenue Category (for the training data)
    print('-------------------------------------------------------------------------------')
    print('-----Total rows of each category (After under/oversampling; TRAINING DATA)-----')
    print('-------------------------------------------------------------------------------\n')
    print('The total rows for True (category): ', sum(y_train == 1))
    print('The total rows for False (category): ', sum(y_train == 1))
    print('\n-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')


    # Building model using Decision Tree Algorithm
    print('-------------------------------------------------------------------------------')
    print('------------------------Using Decision Tree Algorithm--------------------------')
    print('-------------------------------------------------------------------------------\n')
    dt_model = DecisionTreeClassifier()
    dt_model.fit(X_train, y_train)
    y_pred = dt_model.predict(X_test)
    score = accuracy_score(y_pred, y_test)
    print('Accuracy score: ', score, '\n')
    print('CLASSIFICATION REPORT')
    print(classification_report(y_test, y_pred))
    print('-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

    # Building model K-Nearest Neighbors Algorithm (1 neighbor)
    print('-------------------------------------------------------------------------------')
    print('---------------Using K-Nearest Neighbors Algorithm (1 neighbor)----------------')
    print('-------------------------------------------------------------------------------\n')
    knn_model = KNeighborsClassifier(n_neighbors=1)
    knn_model.fit(X_train,y_train);
    y_pred = knn_model.predict(X_test)
    score = accuracy_score(y_pred, y_test)
    print('Accuracy score: ', score, '\n')
    print('CLASSIFICATION REPORT')
    print(classification_report(y_test, y_pred))
    print('-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')


    # Building model K-Nearest Neighbors Algorithm (5 neighbors)
    print('-------------------------------------------------------------------------------')
    print('---------------Using K-Nearest Neighbors Algorithm (5 neighbors)---------------')
    print('-------------------------------------------------------------------------------\n')
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train,y_train);
    y_pred = knn_model.predict(X_test)
    score = accuracy_score(y_pred, y_test)
    print('Accuracy score: ', score, '\n')
    print('CLASSIFICATION REPORT')
    print(classification_report(y_test, y_pred))
    print('-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')


    # Building model Random Forest Algorithm (1000 decision trees, 42 random state)
    print('-------------------------------------------------------------------------------')
    print('----Using Random Forest Algorithm (50 decision trees, 60 random state----------')
    print('-------------------------------------------------------------------------------\n')
    rf_model = RandomForestRegressor(n_estimators = 50, random_state = 60)
    rf_model.fit(X_train, y_train);
    y_pred = rf_model.predict(X_test)
    # Extract the predicted class labels
    y_pred = np.where(y_pred > 0.5, 1, 0)
    score = accuracy_score(y_pred, y_test)
    print('Accuracy score: ', score, '\n')
    print('CLASSIFICATION REPORT')
    print(classification_report(y_test, y_pred))
    print('-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

    # Building model Random Forest Algorithm (1000 decision trees, 42 random state)
    print('-------------------------------------------------------------------------------')
    print('----Using Random Forest Algorithm (1000 decision trees, 42 random state)-------')
    print('-------------------------------------------------------------------------------\n')
    rf_model = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    rf_model.fit(X_train, y_train);
    y_pred = rf_model.predict(X_test)
    # Extract the predicted class labels
    y_pred = np.where(y_pred > 0.5, 1, 0)
    score = accuracy_score(y_pred, y_test)
    print('Accuracy score: ', score, '\n')
    print('CLASSIFICATION REPORT')
    print(classification_report(y_test, y_pred))
    print('-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

    # Building model Native Bayes Algorithm
    print('-------------------------------------------------------------------------------')
    print('--------------------Using Gaussian Native Bayes Algorithm----------------------')
    print('-------------------------------------------------------------------------------\n')
    gnb_model = GaussianNB()
    gnb_model.fit(X_train, y_train);
    y_pred = gnb_model.predict(X_test)
    score = accuracy_score(y_pred, y_test)
    print('Accuracy score: ', score, '\n')
    print('CLASSIFICATION REPORT')
    print(classification_report(y_test, y_pred))
    print('-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')

    # Building model Linear Regression Algorithm
    print('-------------------------------------------------------------------------------')
    print('--------------------Using Linear Regression Algorithm----------------------')
    print('-------------------------------------------------------------------------------\n')
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train);
    y_pred = lr_model.predict(X_test)
    # Extract the predicted class labels
    y_pred = np.where(y_pred > 0.5, 1, 0)
    score = accuracy_score(y_pred, y_test)
    print('Accuracy score: ', score, '\n')
    print('CLASSIFICATION REPORT')
    print(classification_report(y_test, y_pred))
    print('-------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------\n')



