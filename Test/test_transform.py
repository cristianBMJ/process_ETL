import pandas as pd
from transform import transform_data_with_pandas


def test_transformed_data_is_dataframe():
    df = transform_data_with_pandas()
    assert isinstance(df, pd.DataFrame)

def test_transformed_data_no_duplicates():
    df = transform_data_with_pandas()
    if df is not None:
        assert not df.duplicated(subset='id').any()

def test_transformed_data_no_missing_values():
    df = transform_data_with_pandas()
    if df is not None:
        assert not df['title'].isnull().any()

def test_transformed_data_title_is_uppercase():
    df = transform_data_with_pandas()
    if df is not None:
        assert all(df['title'].str.isupper())
