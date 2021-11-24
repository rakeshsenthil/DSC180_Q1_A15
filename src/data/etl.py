import numpy as no

def get_data(x_dir, y_dir):
    '''
    Retrieve data for year/location/group from the internet
    and return data (or write data to file, if `outpath` is
    not `None`).
    '''
    
    x = np.load(x_dir)
    y = np.load(y_dir)
    
    return x, y