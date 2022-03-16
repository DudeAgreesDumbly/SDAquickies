import pandas as pd
import os

def process_files(ext):
    ''' The process files function will look at the current directory and 
    retreive all the file names and then given the argument ext as the characters
    after the period will proceed to read them into a dataframe and return that
    dataframe.
    
    Inputs: the file extension after the period
    Outputs: Dataframe containing all information from files with matched file extension
    '''
    num_past_period = len(ext)
    path = os.getcwd()
    files = os.listdir(path)
    files_to_read = [f for f in files if f[-num_past_period:] == ext]
    df = pd.DataFrame()
    if files_to_read:
        for f in files_to_read:
            data = pd.read_excel(f)
            df = df.append(data)
    else:
        raise Exception('No files were found ending in %s.' % ext)
    return df