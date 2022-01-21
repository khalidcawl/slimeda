import altair as alt
import pandas as pd

def corr_map(df, columns):
    """
    Creates correlation map chart object for specific columns in a data frame

    Parameters
    ----------
    df: pd.DataFrame
        pandas dataframe
    columns: list
        list of columns to create the correlation map for
    path: string [default value of ""]
        the file path indicating where the image is stored
        by default it would store at the current working directory

    Returns
    -------
    Chart

    Examples
    --------
    >>>from slimeda import corr_map
    >>>corr_map(df, ['age', 'income'])
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Check if 'df' has type pd.DataFrame")

    if not isinstance(columns, list):
        raise TypeError("Check if 'columns' has type list")

    if len(columns) < 2:
        raise ValueError(
            "There should be at least two columns given"
        )
    
    for col in columns:
        if col not in df.columns:
            raise ValueError(
                f"Column {col} is not in the dataset 'df'"
            )

    selected_df = df[columns]

    corr_df = (
        selected_df.select_dtypes("number")
        .corr("spearman")
        .stack()
        .reset_index(name="corr")
    )

    if corr_df.empty:
        raise ValueError(
            f"None of {columns} is  numeric"
        )


    corr_df.loc[corr_df["corr"] == 1, "corr"] = 0  # Remove diagonal
    corr_df["abs"] = corr_df["corr"].abs()
    corr_chart = alt.Chart(corr_df).mark_circle().encode(
        x=alt.X("level_0", title=None),
        y=alt.Y("level_1", title=None),
        size="abs",
        color=alt.Color("corr", scale=alt.Scale(scheme="purpleorange", domain=(-1, 1))),
    )
    return corr_chart