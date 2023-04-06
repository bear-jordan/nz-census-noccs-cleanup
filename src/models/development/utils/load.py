from utils.config import FILEPATH
from utils.tpp import run_tpp
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder 
import pickle

def load_data(minNgram, maxNgram):
    # Load the dataset
    df = pd.read_csv(FILEPATH)
    df["Notes"].fillna(' ', inplace=True)
    df["Notes2"].fillna(' ', inplace=True)
    df['AllText'] = df['Notes'].astype(str)+" "+df['Notes2'].astype(str)

    # Preprocess the text
    df = run_tpp(df)
    df = df.loc[:, ["CleanText", "Match"]]
    df.dropna(inplace=True)

    # Split the data into training and testing sets or use k-fold cross-validation
    X = df["CleanText"]
    y = df['Match']

    # Vectorize the text data using N-grams
    vectorizer = CountVectorizer(ngram_range=(minNgram, maxNgram))
    X = vectorizer.fit_transform(X)
    
    # Encode y
    encoder = LabelEncoder()
    y = encoder.fit_transform(y)

    return (X, y)