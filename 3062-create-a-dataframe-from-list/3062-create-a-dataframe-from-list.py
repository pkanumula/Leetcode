import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Define the column names
    columns = ['student_id', 'age']
    
    # Create the DataFrame from the 2D list
    df = pd.DataFrame(student_data, columns=columns)
    
    return df
    