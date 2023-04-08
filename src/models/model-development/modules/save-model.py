import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

X, y = load_data()


# Train a logistic regression model on the training set
model = LogisticRegression(C=0.01, penalty='l2', solver="saga", class_weight="balanced")
model.fit(X, y)
pickle.dump(model, open("./logistic-regression.sav", "wb"))