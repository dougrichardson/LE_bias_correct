import xarray as xr

# =================
# Data wrangling
# =================
def get_model_path(model):
    """
    Return the path to the historical simulations
    """
    if model == "ACCESS-ESM1-5":
        return "/g/data/fs38/publications/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/"
    else:
        raise ValueError("Incorrect model")
        
def get_model_grid(model):
    """
    Return the string for the model grid
    """
    if model == "ACCESS-ESM1-5":
        return "gn"
    else:
        raise ValueError("Incorrect model")
        
def sel_Aus(ds, lat_name="lat", lon_name="lon"):
    """
    Select Australian region.
    """
    return ds.sel({lon_name: slice(110, 155), lat_name: slice(-45, -10)})