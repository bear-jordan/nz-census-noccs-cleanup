import re
from datetime import date

from modules.utils.config import HISTORY_FILEPATH


def create_history_filter(data) -> list:
    history = pd.read_csv(HISTORY_FILEPATH)
    filter = data["Response Number"].isin(history["Response Number"])
    add_to_history(data.loc[~filter, "Response Number"])

    return filter


def add_to_history(data) -> None:
    history = pd.read_csv(HISTORY_FILEPATH)
    expression = re.compile(r"\.csv")
    backupFilepath = re.sub(expression, f"-{date.today()}-backup.csv", HISTORY_FILEPATH)
    history.to_csv(backupFilepath, index=False)
    pd.concat([history, data]).to_csv(HISTORY_FILEPATH)