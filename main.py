from bayes_forest import *
import time

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def classification():
    filename = "car.data"
    data = read_data(filename)
    train_data, test_data = split_data(data)    # Split the data into training and testing sets
    x_train, y_train = encoding(train_data)
    x_test, y_test = encoding(test_data)
    random_forest = RandomForest(100, NaiveBayes)  # Create a random forest with 100 trees of naive bayes classifications
    random_forest.fit(x_train, y_train)
    y_pred = random_forest.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

def classification2():
    filename_obesity = "ObesityDataSet.csv"
    filename_app_data = "data_to_classification.csv"
    data_obesity = read_data(filename_obesity, 16)
    data_to_classification = read_data(filename_app_data,16)
    train_data_obesity, test_data_obesity = split_data(data_obesity)
    x_train_obesity, y_train_obesity = encoding(train_data_obesity)
    x_test_obesity, y_test_obesity = encoding(test_data_obesity)

    x_to_predict, y_to_predict = encoding(data_to_classification)

    random_forest = RandomForest(30,NaiveBayes)  # Create a random forest with 100 trees of naive bayes classifications
    random_forest.fit(x_train_obesity, y_train_obesity)
    y_pred2 = random_forest.predict(x_test_obesity)
    y_predicted = random_forest.predict(x_to_predict)
    accuracy = accuracy_score(y_test_obesity, y_pred2)
    print(f"Accuracy2: {accuracy}")

def classification3():
    filename_cancer = "breast-cancer.data"
    filename_app_data = "breast_data_to_classification.data"
    data_cancer = read_data(filename_cancer, 0)
    data_to_classification = read_data(filename_app_data,0)
    train_data_cancer, test_data_cancer = split_data(data_cancer)
    x_train_cancer, y_train_cancer = encoding(train_data_cancer)
    x_test_cancer, y_test_cancer = encoding(test_data_cancer)

    x_to_predict, y_to_predict = encoding(data_to_classification)

    random_forest = RandomForest(30,NaiveBayes)  # Create a random forest with 100 trees of naive bayes classifications
    random_forest.fit(x_train_cancer, y_train_cancer)
    y_pred2 = random_forest.predict(x_test_cancer)
    y_predicted = random_forest.predict(x_to_predict)
    accuracy = accuracy_score(y_test_cancer, y_pred2)
    print(f"Accuracy3: {accuracy}")
    print(y_predicted)

if __name__ == '__main__':

    classification()
    #classification2()
    classification3()

    displayText()

