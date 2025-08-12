import pandas as pd
from datetime import datetime

def convert_excel_to_csv(input_file, output_file):
    df = pd.read_excel(input_file)
    df.to_csv(output_file, index=False, sep=",", quoting=1)

    print(f"Converted {input_file} to {output_file} successfully.")
    
# def add_quotes(val):
#     if isinstance(val, pd.Timestamp):
#         return val.strftime("%m/%d/%Y")
#     elif isinstance(val, str):
#         if "." in val:
#             return val
#         return val
#     return val


if __name__ == "__main__":
    input_file = 'app/data/input/people_data.xlsx'
    output_file = 'app/data/output/people_data.csv'
    convert_excel_to_csv(input_file, output_file)
    print(f"Conversion completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")