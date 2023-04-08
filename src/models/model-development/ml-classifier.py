import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, make_scorer

from modules.config import FILEPATH
from modules.clean import run_tpp
from modules.load import load_data


def tune(X, y):
    cv = StratifiedKFold(n_splits=10, shuffle=True)

    # Define the models and hyperparameters to search
    models = [
        ('NB', MultinomialNB(), {'alpha': [0.01, 0.1, 1.0]}),
        ('LR', LogisticRegression(penalty='l2', solver="saga", class_weight="balanced", max_iter=10000), {'C': [0.01, 0.1, 1.0]}),
        ('RF', RandomForestClassifier(), {'n_estimators': [100, 500, 1000],
            'min_samples_leaf': [.05, .1]}),
        ('SVM', SVC(kernel='linear'), {'C': [0.01, 0.1, 1.0]}),
    ]

    # Evaluate multiple models using cross-validation and grid search
    for name, model, params in models:
        scorer = make_scorer(precision_score, average='weighted')
        clf = GridSearchCV(model, params, cv=cv, scoring=scorer)
        clf.fit(X, y)
        return f"{name}: Best parameters - {clf.best_params_}, Best score - {clf.best_score_}"

def main():
    for maxRange in range(1, 10):
        for minRange in range(maxRange):
            X, y = load_data(minRange, maxRange)
            result = tune(X, y)
            with open("./results.txt", "w+") as file:
                title = f" ngram({minRange}, {maxRange}) ".center(20, "=")
                file.writelines([title, result])

if __name__ == "__main__":
    main()