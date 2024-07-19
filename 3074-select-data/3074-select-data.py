import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame to get the row with student_id = 101
    filtered_df = students[students['student_id'] == 101]
    # Select only the 'name' and 'age' columns
    result = filtered_df[['name', 'age']]
    return result
