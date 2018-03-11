import numpy as np
from datetime import datetime, timedelta
import pandas as pd
import json

# from: https://github.com/vega/ipyvega/blob/vega3/vega3/utils.py
def sanitize(df):
    df = df.copy()

    for col_name, dtype in df.dtypes.iteritems():
        if str(dtype) == 'category':
            # XXXX: work around bug in to_json for categorical types
            # https://github.com/pydata/pandas/issues/10778
            df[col_name] = df[col_name].astype(str)
        elif np.issubdtype(dtype, np.integer):
            # convert integers to objects; np.int is not JSON serializable
            df[col_name] = df[col_name].astype(object)
        elif np.issubdtype(dtype, np.floating):
            # For floats, convert nan->None: np.float is not JSON serializable
            col = df[col_name].astype(object)
            df[col_name] = col.where(col.notnull(), None)
        elif str(dtype).startswith('datetime'):
            # Convert datetimes to strings
            # astype(str) will choose the appropriate resolution
            df[col_name] = df[col_name].astype(str).replace('NaT', '')
    return df

class P3JsonEncoder(json.JSONEncoder):
    def default(self,obj):
        return (obj.strftime("%Y-%m-%d %H:%M:%S") if isinstance(obj, datetime)
        else obj.total_seconds() if isinstance(obj, timedelta)
        else obj.to_dict(orient='records') if isinstance(obj, pd.DataFrame)
        else json.JSONEncoder.default(self, obj))
