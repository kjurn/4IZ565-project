from collections import Counter

from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


def split(dataset, sample="UNDER"):
    # Split target and features
    features = dataset.iloc[:, :-1]
    target = dataset.iloc[:, -1]

    # Split train-test data
    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.30)

    # Balance dataset
    if sample.upper() == "UNDER":
        undersample = RandomUnderSampler(sampling_strategy="not majority")
        features_train_under, target_train_under = undersample.fit_resample(features_train, target_train)
        print(features_train_under)
        print(target_train_under.value_counts())
        return features_train_under, target_train_under, target_train, target_test

    if sample.upper() == "UPPER":
        oversample = RandomOverSampler(sampling_strategy="not minority")
        features_train_upper, target_train_upper = oversample.fit_resample(features_train, target_train)
        print(features_train_upper)
        print(target_train_upper.value_counts())
        return features_train_upper, target_train_upper, target_train, target_test


    # smote = SMOTE(sampling_strategy=0.1)
    # vectorizer = CountVectorizer(lowercase=False)
    # vectorizer.fit(features_train.values.ravel())
    # features_train = vectorizer.transform(features_train.values.ravel())
    # features_test = vectorizer.transform(features_test.values.ravel())
    # features_train = features_train.toarray()
    # features_test = features_train.toarray()
    # X_train_SMOTE, y_train_SMOTE = smote.fit_resample(features_train, target_train)
    # print(Counter(y_train_SMOTE))
