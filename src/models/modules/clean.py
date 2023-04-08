import re
import pickle

from modules.utils.config import VECTORIZER_FILEPATH 


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


def preprocess(text):
    text = text.lower() 
    text = text.strip()  
    text = re.sub('\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
    text = re.sub(r'\d','#',text) 
    text = re.sub(r' (one|two|three|four|five|six|seven|eight|nine)',' #',text) 
    text = re.sub(r'\s+',' ',text) 
    
    return text


def run_tpp(data):
    data["CleanText"] = data["AllText"].apply(lambda text: preprocess(str(text)))
    
    return data