import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Drop rows where 'name' column has missing values
    cleaned_students = students.dropna(subset=['name'])
    return cleaned_students