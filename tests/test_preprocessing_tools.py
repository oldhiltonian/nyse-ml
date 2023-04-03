import numpy as np
import pandas as pd
import unittest
from unittest.mock import Mock, patch
from nyse_ml.preprocessing_tools import check_for_nan_columns, check_for_inf_columns, check_for_invalid_columns

def test_check_for_nan_columns():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, np.nan, 6]})
    assert check_for_nan_columns(df) == ['b']

def test_check_for_inf_columns():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, np.inf, 6]})
    assert check_for_inf_columns(df) == ['b']


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)