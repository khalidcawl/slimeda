from slimeda.corr_map import corr_map
import numpy as np
import pandas as pd
from vega_datasets import data
import pytest

def test_corr_map_one_col():
    df = data.cars()
    output_chart = corr_map(df, ['Horsepower'])
    assert output_chart
    assert isinstance(output_chart, alt.Chart)
    assert output_chart.mark == 'circle'

def test_corr_map_multi_col():
    df = data.cars()
    output_chart = corr_map(df, ['Horsepower', 'Acceleration'])
    assert output_chart
    assert isinstance(output_chart, alt.Chart)
    assert output_chart.mark == 'circle'

def test_corr_map_all_col():
    df = data.cars()
    output_chart = corr_map(df, df.columns.to_list())
    assert output_chart
    assert isinstance(output_chart, alt.Chart)
    assert output_chart.mark == 'circle'

def test_corr_map_no_column():
    with pytest.raises(ValueError):
        df = data.cars()
        corr_map(df, [])

def test_corr_map_no_num_column():
    with pytest.raises(ValueError):
        df = data.cars()
        corr_map(df, ['Origin', 'Year'])

def test_corr_map_wrong_column():
    with pytest.raises(ValueError):
        df = data.cars()
        corr_map(df, ['abc', 'def'])

def test_wrong_df_type():
    with pytest.raises(TypeError):
        corr_map([1, 2, 3], ['abc', 'def'])

def test_wrong_col_type():
    with pytest.raises(TypeError):
        df = data.cars()
        corr_map(df, 'Horsepower')

