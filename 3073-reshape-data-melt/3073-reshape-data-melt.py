import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # Melt the DataFrame
    melted_df = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return melted_df