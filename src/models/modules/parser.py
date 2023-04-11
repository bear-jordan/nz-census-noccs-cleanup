import argparse
from pathlib import Path


def run_parser() -> Path:
    """
    Parse the command-line arguments for the NOCC estimate tool.
    Return the path to the data file specified by the user.
    """
    parser = argparse.ArgumentParser(
        prog="NOCC Estimate Tool",
        description="Use this tool to estimate whether or not the NOCCs needs to be changed. Place the data in the './data/external' folder."
    )
    parser.add_argument("data", help="Copy and paste the name of the data file. This must be in the './data/external/' folder.")
    args = parser.parse_args()
    dataPath = Path("../../data/external/" + args.data)

    if not dataPath.exists():
        raise ValueError("Check the data file name.")

    return dataPath
