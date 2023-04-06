import re

def preprocess(text):
    text = text.lower() 
    text = text.strip()  
    text = re.sub('\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
    text = re.sub(r'\d','#',text) 
    text = re.sub(r' (one|two|three|four|five|six|seven|eight|nine)',' #',text) 
    text = re.sub(r'\s+',' ',text) 
    
    return text

def process_row(row):
    row = str(row)
    row = preprocess(row)
    
    return row

def run_tpp(data):
    data["CleanText"] = data["AllText"].apply(lambda x: process_row(x))
    
    return data