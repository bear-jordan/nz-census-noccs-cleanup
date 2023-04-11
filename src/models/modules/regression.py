import pickle
import pandas as pd

from modules.config import MODEL_FILEPATH, ENCODER_FILEPATH 
from modules.clean import clean


def logistic_regression(data) -> pd.DataFrame:
    """
    Apply the logistic regression model to the cleaned text data in the `data` DataFrame to predict the level of confidence that each response is a match.
    Return the `data` DataFrame with the `CONFIDENCE` column updated with the model predictions.
    """
    X = clean(data)
    model = pickle.load(open(MODEL_FILEPATH, 'rb'))
    predictions = model.predict(X)
    transformer = pickle.load(open(ENCODER_FILEPATH, 'rb'))
    data.loc[data["CONFIDENCE"].apply(lambda x: x is None), "CONFIDENCE"] = ["Medium" if p=="Match" else "Low" for p in transformer.inverse_transform(predictions)]
    data.drop(inplace=True, columns=["AllText", "CleanText"])

    return data
