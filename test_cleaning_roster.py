import random
import sys
import logging
from pandas import read_excel
from datetime import date
from openpyxl import load_workbook

def get_master_data_records_xlsx(sheet_name="test_output"):
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
        sys.exit()

records = get_master_data_records_xlsx()