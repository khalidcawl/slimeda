from ast import keyword
from slimeda.miss_counts import miss_counts
import pandas as pd
import pytest

@pytest.fixture
def df_branches():
    return pd.DataFrame([['Monica',"missing","missing"],['David',12,],['Jay',1,]], 
                           columns=['Name','Age',"Hobby"])


def test_miss_counts():
    """Unit test with 3 edge cases."""
    df1 = pd.DataFrame([['Jessica',10,"cook"],['Tom',12,"swim"],['Clarke',1,"Football"]], 
                           columns=['Name','Age',"Hobby"])
    df2 = pd.DataFrame([['Alex',10,"missing"],["Marry",19],['Clarke',1,4]], 
                           columns=['Name','Age',"Hobby"]) 
    df3 = pd.DataFrame(columns=['Name','Age',"Hobby"])                     
    result1 = miss_counts(df1)
    result2 = miss_counts(df2,keyword="missing")
    result3 = miss_counts(df3,keyword="missing")
    assert result1 == "Congratulations! There is no null value in this dataframe", "df without NaNs counted incorrectly!"
    assert result2["Counts"][0] == 2, "Missing value counted incorrectly!"
    assert result3 == "Congratulations! There is no null value in this dataframe", "df without rows counted incorrectly!"

@pytest.mark.parametrize(
    "obj",
    [3.141,"test.txt",[1,2,3]]
)
def test_miss_counts_df_input(obj):
    """Test for the input of df."""
    with pytest.raises(TypeError):
        miss_counts(obj)

def test_miss_counts_keyword_input(df_branches):
    """Test for the input of keyword."""
    with pytest.raises(TypeError):
        miss_counts(df_branches,keyword=[1,2,3])

def test_miss_counts_sparse(df_branches):
    """Test for the sparse parameter."""
    result4 = miss_counts(df_branches,keyword="missing",sparse=True)
    result5 = miss_counts(df_branches,keyword="missing",sparse=False)
    assert len(result4) == 3, "df_branches's result should have 3 rows with sparse = True."
    assert len(result5) == 2, "df_branches's result should have 2 rows with sparse = False."

def test_miss_counts_ascending(df_branches):
    """Test for the ascending parameter."""
    result6 = miss_counts(df_branches,keyword="missing",ascending=True)
    result7 = miss_counts(df_branches,keyword="missing",ascending=False)
    assert result6.iloc[0,0] == 1, "Sort incorrect with ascending = True."
    assert result7.iloc[0,0] == 3, "Sort incorrect with ascending = False."