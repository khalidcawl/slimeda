import numpy as np
import pandas as pd
from slimeda.histogram import histogram
import pytest
from vega_datasets import data

def test_histogram_single_chart():
    """Tests that a single chart is created for a single column"""

    # create a dummy data frame with four columns for testing
    df = data.cars()
    charts = histogram(df, ["Cylinders"])
    assert charts != None
    assert len(charts) == 1
    assert charts[0] != None
    assert charts[0].data.equals(df)
    assert charts[0].mark == "bar"

def test_histogram_multiple_charts():
    """Tests that multiple charts are created for multiple columns"""

    # create a dummy data frame with four columns for testing
    df = data.cars()
    charts = histogram(df, ["Cylinders", "Miles_per_Gallon", "Horsepower"])
    assert charts != None
    assert len(charts) == 3
    for chart in charts:
        assert chart != None
        assert chart.data.equals(df)
        assert chart.mark == "bar"

def test_histogram_invalid_dataframe():
    """Tests that invalid dataframe throws an error"""
    with pytest.raises(TypeError):
        histogram([1,2,3,4])

def test_histogram_no_columns():
    """Tests that function throws an error when no columns are specified"""
    with pytest.raises(ValueError):
        df = data.cars()
        histogram(df, [])

def test_histogram_wrong_column():
    """Tests that function throws an error when user specifies an incorrect column name"""
    with pytest.raises(ValueError):
        rng = np.random.default_rng()
        df = data.cars()
        histogram(df, ["Fake_column"])
