import requests
import pandas as pd
import time
from datetime import datetime
from csv import writer

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
index_data_url = "https://www.nseindia.com/api/allIndices"
headers = {
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,mr;q=0.6",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
session = requests.Session()

def OC_dataframe(expiry_date):
    data = session.get(url, headers=headers).json()['records']['data']
    ocdata = []
    this_moment = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    for i in data:
        for j,k in i.items():
            if j == 'CE' or j == 'PE':
                info = k
                info["instrumentType"]=j
                ocdata.append(info)
    df = pd.DataFrame(ocdata)
    ex_df = df.loc[(df["expiryDate"] == expiry_date)]
    return ex_df

def indices_curr_strike(url,index):
    index_data = session.get(url, headers=headers).json()['data']
    index_data_df = pd.DataFrame(index_data)
    df_nifty = index_data_df.loc[index_data_df['index']== index]['last']
    current_value = df_nifty.iat[0]
    int_value = current_value.astype(int)
    rounded = round(int_value/50)*50
    return rounded

def mota_PCR(dtframe):
    strike = indices_curr_strike(index_data_url,'NIFTY 50')
    #calculate expiry date Option chain data only
    df1 = dtframe.loc[(dtframe['strikePrice'] > strike-400) & (dtframe['strikePrice'] < strike+400)]
    df_call = df1.loc[df1["instrumentType"] == 'CE']
    df_put = df1.loc[df1["instrumentType"] == 'PE']
    c = df_call["changeinOpenInterest"].sum()
    p = df_put["changeinOpenInterest"].sum()
    #Calculate PCR ratio
    PCR_rate = round(p/c,3)
    return PCR_rate

def current_strike_PCR(dtfame):
    strike = indices_curr_strike(index_data_url,'NIFTY 50')
    curr_st_df = dtfame.loc[(dtfame['strikePrice'] == strike)]
    df_call = curr_st_df.loc[curr_st_df["instrumentType"] == 'CE']
    df_put = curr_st_df.loc[curr_st_df["instrumentType"] == 'PE']

    c = df_call["changeinOpenInterest"].sum()
    p = df_put["changeinOpenInterest"].sum()
    #Calculate PCR ratio
    Cur_PCR_rate = round(p/c,3)
    return Cur_PCR_rate

def write_to_csv(expiry_date, list_data):
    with open(f"Data/N_PCR_{expiry_date}.csv", 'a', newline = '') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list_data)
        f_object.close()

def Indicator(expi_date):
    df = OC_dataframe(expi_date)
    # Find current live strike price of option chian.
    cr_strike = indices_curr_strike(index_data_url,'NIFTY 50')
    # Overall PCR rate of Opion chain data.
    mota_PCR_rate = mota_PCR(df)
    # Current strike PCR ratio.
    cur_PCR_rate = current_strike_PCR(df)
    print(f"Current Strike is {cr_strike} --> PCR =", cur_PCR_rate)
    # calculate present time
    this_moment = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    if mota_PCR_rate >= 1:
        todo = 'Buy'
        list_data = [this_moment,mota_PCR_rate,todo]
        write_to_csv(expi_date,list_data)
        print(this_moment,"-->",mota_PCR_rate," --> 'Buy' -> Buy Call Option.")
    elif mota_PCR_rate <= 0.9:
        todo = 'Sell'
        list_data = [this_moment,mota_PCR_rate,todo]
        write_to_csv(expi_date,list_data)
        print(this_moment,"-->",mota_PCR_rate," --> 'Sell' -> Buy PUT Option.")
    else:
        todo = 'Sideways'
        list_data = [this_moment,mota_PCR_rate,todo]
        write_to_csv(expi_date,list_data)
        print(this_moment,"-->",mota_PCR_rate," --> Don't trade, Market is Sideways.")

if __name__ == "__main__":
    while True:
        try:
            Indicator("12-Oct-2023")
            time.sleep(300)
        except:
            print("connection lost")