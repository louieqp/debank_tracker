import requests
import json
import pandas as pd
from datetime import datetime

def getData(wallet_address):
    chains = ['eth', 'bsc', 'matic', 'avax', 'ftm']

    columns = ['Chain','Value','Time']
    data_dict = {}

    for column in columns:
        data_dict[column] = [] 

    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    for chain in chains:
        url = f'https://openapi.debank.com/v1/user/chain_balance?id={wallet_address}&chain_id={chain}'
        response = json.loads(requests.get(url).text)
        chain_val = round(response['usd_value'],2)
        data_dict['Chain'].append(chain.upper())
        data_dict['Value'].append(chain_val)
        data_dict['Time'].append(now)

    print(pd.DataFrame(data_dict))

def read_config():
    with open('config.json', 'r') as f:
        config = json.load(f)

    return config

if __name__ == "__main__":
    config = read_config()
    wallet_address = config['wallet_address']
    getData(wallet_address)