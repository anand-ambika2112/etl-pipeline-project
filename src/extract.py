import pandas as pd

def extract_data(file_path):
    
    df = pd.read_csv(
    file_path,
    encoding='latin1',
    sep='\t',              # 🔥 THIS IS THE FIX
    on_bad_lines='skip'
    
    )
    
    print("Data loaded successfully")
    print("Shape:", df.shape)
    
    return df