from datetime import date
import re


HISTORY_FILEPATH = "../../data/interm/history.csv"
OUTPUT_FILEPATH = f"../../data/processed/{date.today().strftime('%y-%m-%d')}-results.csv"
MODEL_FILEPATH = "./models/utils/models/logistic-regression.sav"
VECTORIZER_FILEPATH = "./models/utils/models/vectorizer.sav"
ENCODER_FILEPATH = "./models/utils/models/encoder.sav"
TARGET = "Number of Individual Forms Received"
FILEPATH = "../../data/external/noccs-testing.csv"
EXPRESSION_1 = re.compile(r"confirm(ed|s)?( with the \w+)?( only)?( there are| that| that there are| there were)?( only)?( occupancy of)? x?(?P<number>\d+|one|two|three|four|five|six|seven|eight|nine)")
EXPRESSION_2 = re.compile(r"(confirmed) (only )?x?(?P<number>[0-9]+|one|two|three|four|five|six|seven|eight|nine) (occupant|people|participants|ppl|residents)?")
EXPRESSION_4 = re.compile(r"(only )?x?(?P<number>[0-9]+|one|two|three|four|five|six|seven|eight|nine) (occupant|people|participants|ppl|residents)? (here )?(in dwelling|at dwelling|on census|on March|liv)")
EXPRESSION_5 = re.compile(r"23 (confirmed )?only x?(?P<number>[0-9]+|one|two|three|four|five|six|seven|eight|nine)")
EXPRESSION_6 = re.compile(r"(confirmed )?only x?(?P<number>[0-9]+|one|two|three|four|five|six|seven|eight|nine) (people )?not")
EXPRESSION_7 = re.compile(r"away on census")
EXPRESSIONS = {
    "1": {"exp": EXPRESSION_1, "score": 1},
    "2": {"exp": EXPRESSION_2, "score": 5},
    "4": {"exp": EXPRESSION_4, "score": 1},
    "5": {"exp": EXPRESSION_5, "score": 1},
    "6": {"exp": EXPRESSION_6, "score": 1},
    "7": {"exp": EXPRESSION_7, "score": 1}
}