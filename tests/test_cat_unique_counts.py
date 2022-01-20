from slimeda.cat_unique_counts import cat_unique_counts

import pandas as pd
import numpy as np
import pytest

def df_sample():
    """Sample dataset"""
    # generate random date
    days = np.arange(0, 30)
    start_date = np.datetime64('2021-01-16')
    date_col = start_date + np.random.choice(days, 10 ) 

    # generate random numbers
    numbers_col = np.random.randint(0, 100, 4)

    # generate random strings
    animal = ['rhino', 'cat', 'bufaloo', 'iguana']
    animal_col = np.random.choice(animal, 10 , p=[0.5, 0.1, 0.1, 0.3])

    # generate random string date type
    str_date  = ['2021-01-01', '2021-01-05', '2021-01-25', '2021-01-15']
    str_date_col = np.random.choice(str_date, 10 , p=[0.5, 0.1, 0.1, 0.3])

    df = pd.DataFrame(data = [date_col, numbers_col, animal_col, str_date_col])

    df1 = pd.DataFrame(data = [['Jessica',10,"cook"],
                        ['Tom',12,"swim"],
                        ['Clarke',1,"football"]], 
                        columns=['Name','Age',"Hobby"])

    df2 = pd.DataFrame(data = [['Alex', 10, '3'],
                                ["Marry", 19, '1'],
                                ['Clarke', 1, '4']], 
                           columns=['Name','Age', "Rate"])

    df3 = pd.DataFrame( columns=['Name','Age', "Rate"])

    return (df.T,df1, df2, df3)

def test_cat_unique_counts():
    """Unit test for unique counts of values in categorical features."""

    df1 = df_sample()[1]
    df2 = df_sample()[2]
    df3 = df_sample()[3]

    result1 = list(cat_unique_counts(df1).iloc[:, 0])
    result2 = list(cat_unique_counts(df2).iloc[:, 0])
    result3 = cat_unique_counts(df3)

    assert result1 == ['Name', 'Hobby']
    assert result2 == ['Name']
    assert result3 == None
    
# bad input
@pytest.mark.parametrize(
    "input", 
    [
        pd.Series(data= {'a': 1, 'b': 2, 'c': 3}, index=['x', 'y', 'z']),
        np.array([[1, 2], [3, 4]]),
        "folorunsho is a girl",
        [3, 5, 9, 11],
        9,
        df_sample()
    ]
)
def test_cat_unique_counts_bad_input(bad_input):
    """Accepts parameters and raise errors when parameter is of wrong instance"""
    with pytest.raises(TypeError):
        cat_unique_counts(input)



