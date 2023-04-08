import pandas as pd
import re

from modules.utils.config import EXPRESSIONS


def test_possible_match(expression, notes) -> bool:
    matches = re.search(expression, notes)
    if matches is None:
        return False
    else:
        return True 


def build_filter(data, matches):
    data["Found.In"] = matches
    oneFilter = data.loc[:, "Found.In"].apply(lambda r: "1" in r)
    twoFilter = data.loc[:, "Found.In"].apply(lambda r: "2" in r)
    fourFilter = data.loc[:, "Found.In"].apply(lambda r: "4" in r)
    fiveFilter = data.loc[:, "Found.In"].apply(lambda r: "5" in r)
    sixFilter = data.loc[:, "Found.In"].apply(lambda r: "6" in r)
    sevenFilter = data.loc[:, "Found.In"].apply(lambda r: "7" in r)
    data.drop(columns=["Found.In"], inplace=True)

    return (oneFilter | twoFilter | fourFilter | fiveFilter | sixFilter | sevenFilter)



def classify(data):
    data["Notes"].fillna("", inplace=True)
    data["Notes2"].fillna("", inplace=True)
    data["Notes"] = data["Notes"].apply(str)
    data["Notes2"] = data["Notes2"].apply(str)
    matches = list() 
    for _, row in data.iterrows():
        rowMatch = list()
        notes = row["Notes"].lower() + row["Notes2"].lower()
        for key, values in EXPRESSIONS.items():
            if test_possible_match(values["exp"], notes):
                rowMatch.append(key)
            else:
                rowMatch.append(None)
        matches.append(rowMatch)

    filter = build_filter(data, matches)
    data.loc[filter, "CONFIDENCE"] = "High"

    return data
