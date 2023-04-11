import pandas as pd
import re

def score(notes, expression, type):
    matches = notes.apply(lambda row: re.search(expression, row))
    
    matchCount = sum([1 for match in matches if match is not None])
    if type=="positive":
        return matchCount
    elif type=="negative":
        return len(notes)-matchCount

def score_true_positive(expression, data) -> int:
    data = data.loc[data["Match"] == "Match"]

    return score(data["Notes"]+data["Notes2"], expression, "positive")

def score_true_negative(expression, data) -> int:
    data = data.loc[data["Match"] == "No Match"]

    return score(data["Notes"]+data["Notes2"], expression, "negative")

def score_false_positive(expression, data) -> int:
    data = data.loc[data["Match"] == "No Match"]

    return score(data["Notes"]+data["Notes2"], expression, "positive")

def score_false_negative(expression, data) -> int:
    data = data.loc[data["Match"] == "Match"]

    return score(data["Notes"]+data["Notes2"], expression, "negative")

def score_expression(expression, data):
    truePositives = score_true_positive(expression, data)
    trueNegatives = score_true_negative(expression, data)
    falsePositives = score_false_positive(expression, data)
    falseNegaives = score_false_negative(expression, data)

    return pd.DataFrame({"type": ["Positive", "Negative"], "True": [truePositives, trueNegatives], "False": [falsePositives, falseNegaives]})
