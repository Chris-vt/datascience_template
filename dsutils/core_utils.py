from varname import nameof
from numpy import round as np_round

def save_var(var:any,var_name:str, suffix='df')-> None:
    import pickle
    """save variable for later use"""
    with open(f',/02_vars/{suffix}_{var_name}','wb') as f:
        pickle.dump(var,f)

def load_var(var_file:str)-> any:
    import pickle
    """load variable for use"""
    with open(var_file,"rb") as f:
        var=pickle.load(f)
    return var


    