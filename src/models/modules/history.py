import re
from datetime import date
import pandas as pd

from modules.config import HISTORY_FILEPATH


def create_history_filter(data: pd.DataFrame) -> pd.Series:
    """
    Create a boolean mask indicating whether each row in the `data` DataFrame corresponds to a response number that has already been processed and saved in the history file.
    If a response number in `data` is not found in the history file, add it to the history file.
    Return the boolean mask.
    """
    history = pd.read_csv(HISTORY_FILEPATH)
    filter_ = data["Response Number"].isin(history["Response Number"])
    add_to_history(data.loc[~filter_, "Response Number"])

    return filter_


def add_to_history(data: pd.DataFrame) -> None:
    """
    Add the response numbers in the `data` DataFrame to the history file.
    Create a backup of the history file before appending the new data.
    """
    history = pd.read_csv(HISTORY_FILEPATH)
    expression = re.compile(r"\.csv")
    backupFilepath = re.sub(expression, f"-{date.today()}-backup.csv", HISTORY_FILEPATH)
    # history.to_csv(backupFilepath, index=False)
    # pd.concat([history, data]).to_csv(HISTORY_FILEPATH, index=False)
