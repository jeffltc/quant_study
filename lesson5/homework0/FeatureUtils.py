################# FeatureUtils ########################################################


################# Force Index ########################################################

# Load the necessary packages and modules
import pandas as pd
import tushare as ts

# Force Index 
def ForceIndex(data, ndays): 
 FI = pd.Series(data['close'].diff(ndays) * data['volume'], name = 'ForceIndex') 
 data = data.join(FI) 
 return data

'''
