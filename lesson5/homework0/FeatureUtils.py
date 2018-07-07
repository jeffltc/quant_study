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

# Simple Moving Average 
def SMA(data, ndays=50): 
 SMA = pd.Series(data['close'].rolling(ndays).mean(), name = 'SMA') 
 data = data.join(SMA) 
 return data


# Exponentially-weighted Moving Average 
def EWMA(data, ndays=200): 
 EMA = pd.Series(data['close'].ewm(span = ndays, min_periods = ndays - 1), 
 name = 'EWMA_' + str(ndays)) 
 data = data.join(EMA) 
 return data


# Rate of Change (ROC)
def ROC(data,n = 5):
 N = data['close'].diff(n)
 D = data['close'].shift(n)
 ROC = pd.Series(N/D,name='Rate of Change')
 data = data.join(ROC)
 return data 

# Efficiency Ratio
def ER(data,n = 10):
     change = data['close'].diff(n).abs()
     t_change =  data['close'].diff(1).abs()
     volatility = (t_change).rolling(min_periods=10, window=10).sum()
     ER = pd.Series(change/volatility,name='Efficiency Ratio')
     data = data.join(ER)
     return data 

# Commodity Channel Index 
def CCI(data, ndays =20): 
     TP = (data['high'] + data['low'] + data['close']) / 3 
     CCI = pd.Series((TP - pd.rolling_mean(TP, ndays)) / (0.015 * pd.rolling_std(TP, ndays)),
     name = 'CCI') 
     data = data.join(CCI) 
     return data

#On Balance Volumn
def OBV(data, ndays = 1): 
    OBV = [data['volume'][0]]
    
    for i in range(1,len(data)):
        if data['close'].iloc[i] < data['close'].iloc[i-1]:
            current_OBV = OBV[i-1] - data['volume'].iloc[i]
        elif data['close'].iloc[i] == data['close'].iloc[i-1]:
            current_OBV = OBV[i-1]
        elif data['close'].iloc[i] > data['close'].iloc[i-1]:
            current_OBV = OBV[i-1] + data['volume'].iloc[i]
        OBV.append(current_OBV)
    
    OBV = pd.Series(OBV, name = 'On Balance Volumn') 
    data = data.join(OBV) 
    return data

# PP
def PP(data,n = 1):
    P = (data['high'] + data['low'] + data['close'])/3
    S1 = P*2 - data['high']
    S2 = P - (data['high'] - data['low'])
    R1 = P*2 - data['low']
    R2 = P + (data['high'] - data['low'])
    PP = pd.DataFrame({'P':P,'S1':S1,'S2':S2,'R1':R1,'R2':R2})
    data = data.join(PP)
    return data

# ATR
def ATR(data,n =1):
    TR_lst = [data.iloc[0]['high']-data.iloc[0]['low']]
    for i in range(1,len(data)):
        current_high = data.iloc[i]['high']
        current_low = data.iloc[i]['low']
        previous_close = data.iloc[i-1]['close']
        TR1 = current_high - current_low
        TR2 = current_high - previous_close
        TR3 = current_low - previous_close
        TR = max(TR1,TR2,TR3)
        TR_lst.append(TR)
    
    ATR = []
    
    for i in range(0,14):
        ATR.append(TR_lst[i])
    
    ATR.append(sum(ATR)/len(ATR))
        
    for i in range(15,len(TR_lst)):
        ATR.append((ATR[i-1]*13 + TR_lst[i])/14)
    ATR = pd.Series(ATR, name = 'Actual True Range') 
    data = data.join(ATR) 
    return data
