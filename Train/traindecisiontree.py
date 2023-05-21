from sklearn.tree import DecisionTreeClassifier
import dataset as dataset
import directory as directory
import pickle
from datetime import datetime


def train(data):
    train, X_train, y_train = dataset.split(data)
    dt_model = DecisionTreeClassifier()
    print("Please wait while the model is being trained.")
    dt_model.fit(X_train, y_train)
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    directory_path = "Models/DecisionTreeModels/"
    directory.make_directory(directory_path)
    filename = directory_path+"Decision_Tree_Model_" + dt_string + ".sav"
    pickle.dump(dt_model, open(filename, 'wb'))
    print("Decision tree model has been trained!")
