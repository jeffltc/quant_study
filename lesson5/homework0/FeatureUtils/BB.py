################ Bollinger Bands #############################

# Load the necessary packages and modules
import pandas as pd
import tushare as ts

# Compute the Bollinger Bands 
def BBANDS(data, ndays = 50):

    MA = pd.Series(data['close'].rolling(ndays).mean()) 
    SD = pd.Series(data['close'].rolling(ndays).std())

    b1 = MA + (2 * SD)
    B1 = pd.Series(b1, name = 'Upper BollingerBand') 
    data = data.join(B1) 
 
    b2 = MA - (2 * SD)
    B2 = pd.Series(b2, name = 'Lower BollingerBand') 
    data = data.join(B2) 
 
    return data
 
# Retrieve the Nifty data from Yahoo finance:
data = ts.get_k_data('600000',start='2010-01-01', end='2016-01-01')
data = pd.DataFrame(data)

# Compute the Bollinger Bands for NIFTY using the 50-day Moving average
n = 50
NIFTY_BBANDS = BBANDS(data, n)
print(NIFTY_BBANDS)