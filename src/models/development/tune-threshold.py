import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score
from utils.load import load_data
import matplotlib.pyplot as plt

X, y = load_data()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

# Train a logistic regression model on the training set
model = LogisticRegression(C=0.01, penalty='l2', solver="saga", class_weight="balanced")
model.fit(X_train, y_train)

# Predict probabilities for the validation set
y_pred_prob = model.predict_proba(X_test)[:, 1]

# Vary the threshold value and compute precision for each threshold value
thresholds = np.linspace(0, 1, 101)
precisions = []
for threshold in thresholds:
    y_pred = (y_pred_prob >= threshold).astype(int)
    precision = precision_score(y_test, y_pred, average="weighted", zero_division=1)
    precisions.append(precision)

# Plot the precision values against the threshold values
plt.plot(thresholds, precisions)
plt.xlabel('Threshold')
plt.ylabel('Precision')
plt.title('Precision vs. Threshold')
# plt.show()

# Choose the threshold value that results in the highest precision value
best_threshold = thresholds[np.argmax(precisions)]
print(best_threshold)
print(precisions[np.argmax(precisions)])