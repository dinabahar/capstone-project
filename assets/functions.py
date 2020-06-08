import pandas as pd

def make_lists(df, col):
    """
    col = name of column to convert into a list 
    """
    
    indices = list(df.index)
    for i in indices:
        df.at[i, col] = str(df.loc[i, col][2:-2]).split("', '")
        
    return df[col]