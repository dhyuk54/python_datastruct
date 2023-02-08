import numpy as np
import pandas as pd


def get_df():
    data = [
        {"col1": 10, "col2": 20, "col3": "dummy"},
        {"col1": 11, "col2": 221, "col3": "dummy"},
        {"col1": 11, "col2": np.nan, "col3": "dummy"},
        {"col1": 13, "col2": 23, "col3": "dummy"},
        {"col1": 14, "col2": 24, "col3": "dummy"},
        {"col1": 14, "col2": 25, "col3": "dummy"},
        {"col1": 14, "col2": np.nan, "col3": "dummy"},
    ]
    return pd.DataFrame(data=data)

def main():
    df = get_df()
    print(df)
    """
       col1   col2   col3
    0    10   20.0  dummy
    1    11  221.0  dummy
    2    11    NaN  dummy
    3    13   23.0  dummy
    4    14   24.0  dummy
    5    14   25.0  dummy
    6    14    NaN  dummy
    """
    data = df.groupby('col1').indices
    print(data)
    """
    {10: array([0]), 11: array([1, 2]), 13: array([3]), 14: array([4, 5, 6])}
    """
    for col1_data, index in data.items():
        last_rowData_isNotNone = df.loc[max(index):max(index), 'col2'].notna()
        if (len(index) > 1) and last_rowData_isNotNone.bool:
            df.loc[max(index):max(index), 'col2'] = int(df.loc[min(index):min(index), 'col2'])
            df.loc[min(index):min(index), 'col2'] = None
    df.dropna(how='all',inplace=True,subset='col2')
    print(df)
    """
       col1   col2   col3
    0    10   20.0  dummy
    2    11  221.0  dummy
    3    13   23.0  dummy
    5    14   25.0  dummy
    6    14   24.0  dummy
    """
if __name__ == "__main__":
    main()