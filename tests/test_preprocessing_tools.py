import numpy as np
import pandas as pd
import unittest
from unittest.mock import Mock, patch
from nyse_ml.preprocessing_tools import check_for_invalid_data

def test_check_for_invalid_data():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [np.inf, 2, 3]})
    assert check_for_invalid_data(df) == ['col2']


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)