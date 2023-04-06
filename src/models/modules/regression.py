import pickle
from modules.utils.config import MODEL_FILEPATH, ENCODER_FILEPATH 
from modules.utils.clean import clean

def logistic_regression(data):
    X = clean(data)
    model = pickle.load(open(MODEL_FILEPATH, 'rb'))
    predictions = model.predict(X)
    transformer = pickle.load(open(ENCODER_FILEPATH, 'rb'))
    data.loc[data["CONFIDENCE"].apply(lambda x: x is None), "CONFIDENCE"] = ["Medium" if p=="Match" else "Low" for p in transformer.inverse_transform(predictions)]
    data.drop(inplace=True, columns=["AllText", "CleanText"])

    return data