import pandas as pd
import requests

def fundamentus () :

    url = 'http://fundamentus.com.br/resultado.php'

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

    r = requests.get(url,headers=header)

    return pd.read_html(r.text,  decimal=',', thousands='.')[0]

df = fundamentus()

#save file
df.to_csv("B3.csv")
