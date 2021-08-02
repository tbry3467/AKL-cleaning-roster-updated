import random
import sys
import logging
import os
from pandas import read_excel
from datetime import date
from openpyxl import load_workbook

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))


module_folder = os.path.dirname(os.path.abspath(__file__))

def get_master_data_records_xlsx(path=f"{module_folder}/test_output.xlsx", sheet_name="output.xlsx"):
    """
    Reads records from the master data excel file.
    Must be an [.xlsx]

    Args:
        path ([type], optional): Path to the file. Defaults to f"{module_folder}/master.xlsx".
        sheet_name (str, optional): Name of the sheet in the file. Defaults to "master".

    Returns:
        [list[dict]]: List of dictionaries with the columns as the keys
    """
    # Get excel results into a dataframe
    try:
        data_frame = read_excel(sheet_name=sheet_name, dtype=str)
    except Exception:
        logging.error(f"Excel file may be corrupted! Exiting app to avoid damage.")
        #sys.exit()

records = get_master_data_records_xlsx()

print ("hey")