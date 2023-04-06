import pandas as pd
from modules.utils.config import OUTPUT_FILEPATH
from modules.classifier import classify
from modules.regression import logistic_regression
from modules.parser import run_parser
from modules.check import create_history_filter
from modules.reporting import report
from modules.sql.query import run_query, read_query


def writeout(data, filepath):
    ...

def generate_dataset():
    ...

def main():
    toWrite = []
    dataPath = run_parser()
    rawData = pd.read_csv(dataPath)
    data = rawData.loc[~create_history_filter(rawData), :].copy()
    data["CONFIDENCE"] = None
    data = classify(data)
    data = logistic_regression(data)
    data["CONFIDENCE"] = pd.Categorical(data["CONFIDENCE"], categories=["High", "Medium", "Low"])
    data.sort_values(by="CONFIDENCE", ignore_index=True, inplace=True)
    print(data)
    # report(data)
    toWrite.append((OUTPUT_FILEPATH, data))
    # data.to_csv(OUTPUT_FILEPATH, index=False)


if __name__ == "__main__":
    main()