import pandas as pd
import re

from modules.config import EXPRESSIONS


def test_possible_match(expression: str, notes: str) -> bool:
    """
    Test if a regular expression `expression` matches with the string `notes`.
    Return True if there's a match, False otherwise.
    """
    matches = re.search(expression, notes)
    if matches is None:
        return False
    else:
        return True 


def build_filter(data: pd.DataFrame, matches: list) -> pd.Series:
    """
    Build a filter that selects rows where any of the `matches` strings appear in the "Found.In" column of the `data` DataFrame.
    Return a boolean Series with the same length as `data` that indicates whether each row satisfies the filter or not.
    """
    data["Found.In"] = matches
    one_filter = data.loc[:, "Found.In"].apply(lambda r: "1" in r)
    two_filter = data.loc[:, "Found.In"].apply(lambda r: "2" in r)
    three_filter = data.loc[:, "Found.In"].apply(lambda r: "3" in r)
    four_filter = data.loc[:, "Found.In"].apply(lambda r: "4" in r)
    five_filter = data.loc[:, "Found.In"].apply(lambda r: "5" in r)
    data.drop(columns=["Found.In"], inplace=True)

    return (one_filter | two_filter | three_filter | four_filter | five_filter)


def classify(data: pd.DataFrame) -> pd.DataFrame:
    """
    Classify the rows of the `data` DataFrame based on the regular expressions in the `EXPRESSIONS` dictionary.
    Add a new "CONFIDENCE" column to `data` that indicates whether the row's classification is "High" or not.
    Return the modified `data` DataFrame.
    """
    data["Notes"].fillna("", inplace=True)
    data["Notes2"].fillna("", inplace=True)
    data["Notes"] = data["Notes"].apply(str)
    data["Notes2"] = data["Notes2"].apply(str)
    matches = []
    for _, row in data.iterrows():
        row_match = []
        notes = row["Notes"].lower() + row["Notes2"].lower()
        for key, values in EXPRESSIONS.items():
            if test_possible_match(values["exp"], notes):
                row_match.append(key)
            else:
                row_match.append(None)
        matches.append(row_match)

    filter = build_filter(data, matches)
    data.loc[filter, "CONFIDENCE"] = "High"

    return data
