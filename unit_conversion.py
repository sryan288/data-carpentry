""" Functions to convert units """

def convert_pr_units(clim):
    """ Function to convert precipitation units to mm/day
    
    Args:
        clim (dataset) : precipiation variable
        
    Output:
        clim (dataset) : converted variable and attributes
    """
    clim.data = clim.data * 86400
    clim.attrs['units'] = 'mm/day'
    return clim