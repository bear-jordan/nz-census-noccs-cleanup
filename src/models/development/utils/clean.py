import pickle
from models.utils.config import VECTORIZER_FILEPATH 
from models.utils.tpp import run_tpp


def clean(data):
    # Load the dataset
    data["Notes"].fillna(' ', inplace=True)
    data["Notes2"].fillna(' ', inplace=True)
    data['AllText'] = data['Notes'].astype(str)+" "+data['Notes2'].astype(str)

    # Preprocess the text
    data = run_tpp(data)

    # Split the data into training and testing sets or use k-fold cross-validation
    X = data.loc[data["CONFIDENCE"].apply(lambda x: x is None), "CleanText"]

    # Vectorize the text data using N-grams
    vectorizer = pickle.load(open(VECTORIZER_FILEPATH, 'rb'))
    X = vectorizer.transform(X)

    return X