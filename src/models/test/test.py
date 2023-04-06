import pytest
from utils.score import *
import pandas as pd

@pytest.fixture
def data():
    return pd.DataFrame({
        "Match": ["Match", "Match", "Match", "No Match", "No Match", "No Match","No Match","No Match","No Match","No Match"],
        "Notes": ["true", "false", "false", "true", "true", "true", "false", "false", "false", "false"],
        "Notes2": ["", "", "", "", "", "", "", "", "", ""],
    })

@pytest.fixture
def regex():
    return re.compile(r"true")

def test_true_positive(data, regex):
    assert score_true_positive(regex, data) == 1

def test_false_negative(data, regex):
    assert score_false_negative(regex, data) == 2

def test_false_positive(data, regex):
    assert score_false_positive(regex, data) == 3

def test_true_negative(data, regex):
    assert score_true_negative(regex, data) == 4