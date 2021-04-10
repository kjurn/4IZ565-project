from matplotlib.pyplot import figure
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier, plot_tree


def create_tree(split):
    features_train = split[0]
    target_train = split[1]
    features_test = split[2]
    target_test = split[3]

    classifier = DecisionTreeClassifier()
    tree_model = classifier.fit(features_train, target_train)
    prediction = tree_model.predict(features_test)
    print("Accuracy:", metrics.accuracy_score(target_test, prediction))
    visualise_tree(tree_model, features_train)


def visualise_tree(tree_model, features_train):
    figure(figsize=(18, 18))
    plot_tree(tree_model, feature_names=features_train.columns,
              class_names=["nezaviněná řidičem", "nepřiměřená rychlost jízdy", "nesprávné předjíždění",
                           "nedání přednosti v jízdě", "nesprávný způsob jízdy", "technická závada vozidla"],
              filled=True)
