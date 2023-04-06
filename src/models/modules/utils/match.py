import pandas as pd
import re

def test_possible_match(expression, notes) -> bool:
    matches = re.search(expression, notes)
    if matches is None:
        return False
    else:
        return True 

def test_exact_match(expression, notes, target) -> bool:
    matches = re.search(expression, notes)
    if matches is None:
        return False
    else:
        return True if target == matches.group("number") else False