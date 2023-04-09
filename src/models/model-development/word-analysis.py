from collections import Counter
from modules.config import *
import pandas as pd

def main():
    data = pd.read_csv(FILEPATH)
    data["Notes"] = data["Notes"].apply(str)
    data["Notes2"] = data["Notes2"].apply(str)
    matchCounter = Counter() 
    noMatchCounter = Counter() 
    for _, row in data.iterrows():
        notes = row["Notes"].lower() + row["Notes2"].lower()
        if row["Match"] == "Match":
            matchCounter.update(notes.split())
        else:
            noMatchCounter.update(notes.split())
    
    print((matchCounter-noMatchCounter).most_common(20))

if __name__=="__main__":
    main()