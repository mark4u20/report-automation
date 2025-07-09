import pandas as pd
import json
import argparse
import os

from utils.pivot import generate_pivot_table
from utils.charts import create_chart
from utils.excel_io import add_timestamp_to_file

parser = argparse.ArgumentParser(description="Sales Analysis Automation Script")
parser.add_argument('--config', type=str, required=True, help='Path to config.json')
args = parser.parse_args()

# ─── 2. Load paths from config.json ────────────────────────────────────────────
with open(args.config, 'r') as f:
    config = json.load(f)

input_path = config['input_path']
output_path = config['output_path']
output_filename_config = config['output_filename']
reports = config['reports']
output_file_name = add_timestamp_to_file(output_path + output_filename_config)

files = os.listdir(input_path)

combined_df = pd.DataFrame()

for file in files:
    sheets = pd.ExcelFile(input_path + file).sheet_names
    for sheet in sheets:
        df = pd.read_excel(input_path + file, sheet)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

result_array =[]

for report in reports:
    dict_temp={}
    pivot = generate_pivot_table(combined_df,report)
    dict_temp['report_config']=report
    dict_temp['dataframe']=pivot
    result_array.append(dict_temp)


create_chart(output_file_name, result_array)
