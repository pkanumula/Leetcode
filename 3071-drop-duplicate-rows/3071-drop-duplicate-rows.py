import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicate rows based on the 'email' column, keeping only the first occurrence
    return customers.drop_duplicates(subset='email', keep='first')
