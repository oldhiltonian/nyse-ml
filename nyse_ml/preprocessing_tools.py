import pandas as pd
import numpy as np

def check_for_invalid_data(df, *args):
    """
    Checks for invalid data in the dataframe.
    
    Checks to see if any of the columns in the dataframe contain invalid data types
    pass by the args parameter. If the column contains invalid data, the column name
    is appended to a list and returned.
    """
    if not args:
        args = [np.inf, -np.inf, np.nan]
    invalid_columns = []
    for col in df.columns:
        for value in df[col]:
            if type(value) in args:
                invalid_columns.append(col)
    return invalid_columns