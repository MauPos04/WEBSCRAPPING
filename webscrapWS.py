from selenium import webdriver
from selenium.webdriver.chrome.service import Service
path = '/Users/user/Downloads/chromedriver-win64/chromedriver.exe'
import pandas as pd
import time


service = Service(executable_path=path)

driver = webdriver.Chrome(service=service)
def obtain_data_missing(year):

    web = f'https://web.archive.org/web/20230911171621/https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    driver.get(web)

    matches = driver.find_elements(by='xpath', value = '//tr[@itemprop="name"]')

    home = []
    score = []
    away = []

    for match in matches:
        ##El punto en value indica que estamos usando otro elemento en este caso el elemento match
        home.append(match.find_element(by='xpath', value='./th[1]').text) ## el home
        score.append(match.find_element(by='xpath', value='./th[2]').text) ## el score
        away.append(match.find_element(by='xpath', value='./th[3]').text) ## el visitante

    dict_football = {'home' : home, 'score' :score , 'away': away}

    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    time.sleep(2)

    
    return df_football

years = [1930, 1934, 1938,  1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

fifa = [obtain_data_missing(year) for year in years] ## lista de comprension


driver.quit()
df_fifa = pd.concat(fifa, ignore_index=True)

df_fifa.to_csv('fifa_worldcup_missing_data.csv', index=False)
