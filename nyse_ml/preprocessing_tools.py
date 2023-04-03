import pandas as pd
import numpy as np

def check_for_nan_columns(df):
    """Check for columns with NaN values.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to check for NaN values.

    Returns
    -------
    list
        A list of columns with NaN values.
    """
    return df.columns[df.isna().any()].tolist()

def check_for_inf_columns(df):
    """Check for columns with infinite values.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to check for infinite values.

    Returns
    -------
    list
        A list of columns with infinite values.
    """
    return df.columns[df.isin([np.inf, -np.inf]).any()].tolist()

def drop_nan_columns(df, threshold=0.5):
    """Drop columns with NaN values.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to drop columns from.
    threshold : float, optional
        The threshold of NaN values to drop a column, by default 0.5

    Returns
    -------
    pd.DataFrame
        The DataFrame with columns dropped.
    """
    nan_columns = check_for_nan_columns(df)
    for column in nan_columns:
        if df[column].isna().sum() / len(df) > threshold:
            df.drop(columns=column, inplace=True)
    return df