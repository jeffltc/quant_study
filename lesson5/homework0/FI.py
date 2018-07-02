################# Force Index ########################################################

# Load the necessary packages and modules
import pandas as pd
import tushare as ts

# Force Index 
def ForceIndex(data, ndays): 
 FI = pd.Series(data['close'].diff(ndays) * data['volume'], name = 'ForceIndex') 
 data = data.join(FI) 
 return data


# Retrieve the Apple data from Tushare:
data = ts.get_k_data('600000',start='2010-01-01', end='2016-01-01')
data = pd.DataFrame(data)

# Compute the Force Index for Apple 
n = 1
AAPL_ForceIndex = ForceIndex(data,n)
print(AAPL_ForceIndex)