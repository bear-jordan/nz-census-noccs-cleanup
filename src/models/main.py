import pandas as pd

from modules.utils.config import OUTPUT_FILEPATH
from modules.classifier import classify
from modules.regression import logistic_regression
from modules.parser import run_parser
from modules.check import create_history_filter


def main():
    dataPath = run_parser()
    rawData = pd.read_csv(dataPath)
    data = rawData.loc[~create_history_filter(rawData), :].copy()
    data["CONFIDENCE"] = None
    data = classify(data)
    data = logistic_regression(data)
    data["CONFIDENCE"] = pd.Categorical(data["CONFIDENCE"], categories=["High", "Medium", "Low"])
    data.sort_values(by="CONFIDENCE", ignore_index=True, inplace=True)
    # data.to_csv(OUTPUT_FILEPATH, index=False)


if __name__ == "__main__":
    main()