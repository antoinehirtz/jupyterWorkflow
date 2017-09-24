import os
from urllib.request import urlretrieve

import pandas as pd

FERMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FERMONT_URL,
                     force_download=False):
    """Download and cache the Fremont data

    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : Bool (optional)
        if True, force redownload of data

    Returns
    -------
    data : pandas.DataFrame
        The Fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date',parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
