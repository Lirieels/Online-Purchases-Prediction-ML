from sklearn.tree import DecisionTreeClassifier
import dataset as dataset
import pickle
from datetime import datetime


def train(data):
    train, X_train, y_train = dataset.split(data)
    dt_model = DecisionTreeClassifier()
    dt_model.fit(X_train, y_train)
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    filename = "Decision_Tree_Model_" + dt_string + ".sav"
    pickle.dump(dt_model, open(filename, 'wb'))
    print("Decision tree model has been trained!")
