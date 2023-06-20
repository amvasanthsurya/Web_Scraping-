import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url='https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
soup = bs(response.content, 'html.parser')

rows = soup.find('table', {'id':'example2'}).find('tbody').find_all('tr')

contries_list = []

for row in rows:
    dic={}

    dic['Country']=row.find_all('td')[1].text
    dic['Popuation 2023']=row.find_all('td')[2].text
    dic['Yearly Change']=row.find_all('td')[3].text
    dic['Net Change'] = row.find_all('td')[4].text
    dic['Density'] = row.find_all('td')[5].text
    dic['Land Area'] = row.find_all('td')[6].text
    dic['Migrants'] = row.find_all('td')[7].text
    dic['Fert. Rate'] = row.find_all('td')[8].text
    dic['Med. Age'] = row.find_all('td')[9].text
    dic['Urban Pop%'] = row.find_all('td')[10].text
    dic['World Share'] = row.find_all('td')[11].text

    contries_list.append(dic)

df = pd.DataFrame(contries_list)
df.to_excel('Countries_data.xlsx', index=False)
df.to_csv('Countries_data.csv', index=False)

