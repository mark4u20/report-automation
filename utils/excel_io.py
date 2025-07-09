import pandas as pd
import json
from datetime import datetime

def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def read_excel_file(file_path, sheet_name=None):
    return pd.read_excel(file_path, sheet_name=sheet_name)

def write_dataframe_to_excel(writer, df, sheet_name, startrow=0, header=True):
    df.to_excel(writer, sheet_name=sheet_name, startrow=startrow, index=False, header=header)

# Insert timestamp before extension
def add_timestamp_to_file(filename):
    name_parts = filename.split(".")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{name_parts[0]}_{timestamp}.{name_parts[1]}"