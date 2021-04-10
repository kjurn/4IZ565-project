from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


def create_tree(split):
    features_train = split[0]
    target_train = split[1]
    features_test = split[2]
    target_test = split[3]

    print(features_train)
    print(features_test)

    classifier = DecisionTreeClassifier()
    classifier.fit(features_train, target_train)
    prediction = classifier.predict(features_test)
    print("Accuracy:", metrics.accuracy_score(target_test, prediction))
    return prediction
