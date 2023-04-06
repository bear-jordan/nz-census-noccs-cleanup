def report(data):
    highAccuracy = round(data.loc[(data["CONFIDENCE"]=="High")&(data["Match"]=="Match")].shape[0]/data.loc[data["CONFIDENCE"]=="High"].shape[0], 2)*100
    mediumAccuracy = round(data.loc[(data["CONFIDENCE"]=="Medium")&(data["Match"]=="Match")].shape[0]/data.loc[data["CONFIDENCE"]=="Medium"].shape[0], 2)*100
    lowAccuracy = round(data.loc[(data["CONFIDENCE"]=="Low")&(data["Match"]=="No Match")].shape[0]/data.loc[data["CONFIDENCE"]=="Low"].shape[0], 2)*100

    print(" Accuracy ".center(25, "="))
    print(f"High Confidence: {highAccuracy}% are correctly classified as needing change")
    print(f"Medium Confidence: {mediumAccuracy}% are correctly classified as needing change")
    print(f"Low Confidence: {lowAccuracy}% are correctly classified as not needing change")
