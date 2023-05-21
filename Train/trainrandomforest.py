from sklearn.ensemble import RandomForestRegressor
import dataset as dataset
import directory as directory
import pickle
from datetime import datetime


def train(data):
    n_estimators = int(input('Please enter the number of estimators: '))
    random_state = int(input('Please enter the random state: '))
    train, X_train, y_train = dataset.split(data)
    rf_model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
    print("Please wait while the model is being trained.")
    rf_model.fit(X_train, y_train)
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    directory_path = "Models/RandomForestModels/"
    directory.make_directory(directory_path)
    filename = directory_path + "Random_Forest_Model_" + dt_string + ".sav"
    pickle.dump(rf_model, open(filename, 'wb'))
    print("Random Forest model has been trained!")
