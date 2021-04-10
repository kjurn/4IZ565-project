from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split


def split(dataset, sample="UNDER", split_size=0.30, strategy="all"):
    # Split target and features
    features = dataset.iloc[:, :-1]
    target = dataset.iloc[:, -1]

    # Split train-test data
    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=split_size,
                                                                                random_state=1)
    # Balance dataset
    if sample.upper() == "UNDER":
        undersample = RandomUnderSampler(sampling_strategy=strategy)
        features_train_under, target_train_under = undersample.fit_resample(features_train, target_train)
        return features_train_under, target_train_under, features_test, target_test

    if sample.upper() == "UPPER":
        oversample = RandomOverSampler(sampling_strategy=strategy)
        features_train_upper, target_train_upper = oversample.fit_resample(features_train, target_train)
        return features_train_upper, target_train_upper, features_test, target_test
