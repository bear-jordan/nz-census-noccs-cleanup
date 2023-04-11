import pandas as pd

from modules.config import OUTPUT_FILEPATH
from modules.classifier import classify
from modules.regression import logistic_regression
from modules.parser import run_parser
from modules.history import create_history_filter


def main() -> None:
    """
    Run the main pipeline for the NOCC estimate tool.
    Parse the command-line arguments to get the path to the data file.
    Load the data, filter out any rows that have already been processed, and classify the remaining responses as high, medium, or low confidence.
    Apply the logistic regression model to the cleaned text data to predict the level of confidence for each response.
    Sort the responses by confidence level and print the results to the console.
    Optionally, save the results to a CSV file.
    """
    dataPath = run_parser()
    rawData = pd.read_csv(dataPath)
    data = rawData.loc[~create_history_filter(rawData), :].copy()
    data["CONFIDENCE"] = None
    data = classify(data)
    data = logistic_regression(data)
    data["CONFIDENCE"] = pd.Categorical(data["CONFIDENCE"], categories=["High", "Medium", "Low"])
    data.sort_values(by="CONFIDENCE", ignore_index=True, inplace=True)
    print(data)
    # data.to_csv(OUTPUT_FILEPATH, index=False)


if __name__ == "__main__":
    main()
