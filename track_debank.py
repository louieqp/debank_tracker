from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import sched, time
from datetime import date,datetime
import json

def getData(wallet_address):
   
    url = f'https://debank.com/profile/{wallet_address}'
    networks = ['Ethereum','BSC', 'Polygon', 'Fantom', 'Avalanche']

    # Enable JS
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")

    # Get HTML
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(14)
    html = driver.page_source

    # Close browser
    driver.close()

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    total_portfolio = soup.find("div", {'class': 'TotalChainPortfolio_totalChain__1R3Tl'})
    assets = total_portfolio.find_all("span")
        
    with open('data.csv','a') as data:
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        for i,span in enumerate(assets):
            data.write(f'{networks[i]},{span.text[1:].replace(",","")},{now}\n' )
    
def read_config():
    with open('config.json', 'r') as f:
        config = json.load(f)

    return config

if __name__ == "__main__":
    config = read_config()
    wallet_address = config['wallet_address']
    getData(wallet_address)
