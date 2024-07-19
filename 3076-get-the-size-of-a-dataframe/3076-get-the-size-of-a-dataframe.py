import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Get the shape of the DataFrame
    shape = players.shape
    # Return the number of rows and columns as a list
    return [shape[0], shape[1]]
