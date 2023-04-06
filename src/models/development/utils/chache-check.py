import re
from datetime import date
import pandas as pd

FILEPATH = ""

def create_filter(data) -> list:
    history = pd.read_csv(FILEPATH)
    filter = data["Response.Number"].isin(history)

    return filter

def add_to_history(data) -> None:
    history = pd.read_csv(FILEPATH)
    expression = re.compile(r"\.csv")
    backupFilepath = re.sub(expression, FILEPATH, f"-{date.today()}-backup.csv")
    history.to_csv(backupFilepath, index=False)
    history.concat(data)
    history.to_csv(FILEPATH)