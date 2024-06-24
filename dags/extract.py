import requests
import pandas as pd
from sqlalchemy import create_engine

baseurl = "https://rest.coinapi.io/v1/"

endpoint = "trades/latest/"

params = {
    "include_id": "false",
    "limit": "300",
    "filter_symbol_id": ""
}

headers = {
    'Accept': 'text/plain',
    'X-CoinAPI-Key': '561c1140-f31c-4b1a-952f-4c67a60857bd'
}

url = baseurl + endpoint

response = requests.get(url, headers=headers, params=params)
response.status_code

data = response.json()

df = pd.DataFrame(data)


conn = create_engine('postgresql://j_adolfo12_coderhouse:5W9Nsos3e4@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database')

df.to_sql('trades', con=conn, if_exists='append', chunksize=100, index=False)