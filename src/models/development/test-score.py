from utils.config import *
from utils.score import *
import pandas as pd
from utils.match import *

def gen_confusion(data):
    for key in EXPRESSIONS.keys():
        print(f" {key} ".center(30, "="), "\n", score_expression(EXPRESSIONS[key]["exp"], data), "\n\n")

def main():
    data = pd.read_csv(FILEPATH)
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

    gen_confusion(data)
    data["Found.In"] = matches

    oneFilter = data.loc[:, "Found.In"].apply(lambda r: "1" in r)
    twoFilter = data.loc[:, "Found.In"].apply(lambda r: "2" in r)
    threeFilter = data.loc[:, "Found.In"].apply(lambda r: "3" in r)
    fourFilter = data.loc[:, "Found.In"].apply(lambda r: "4" in r)
    fiveFilter = data.loc[:, "Found.In"].apply(lambda r: "5" in r)
    sixFilter = data.loc[:, "Found.In"].apply(lambda r: "6" in r)
    sevenFilter = data.loc[:, "Found.In"].apply(lambda r: "7" in r)
    filteredData = data.loc[~(oneFilter | twoFilter | threeFilter | fourFilter | fiveFilter | sixFilter | sevenFilter), :]
    # filteredData.to_csv("./to-do-v4.csv", index=False)
    print(len(filteredData))


if __name__ == "__main__":
    main()