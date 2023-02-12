from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
PATH=ChromeDriverManager().install()

import requests
from bs4 import BeautifulSoup



def extraer_datos(url):
    
    driver=webdriver.Chrome(PATH)
    driver.get(url)
    
    
    data = [e.get_attribute('alt') for e in driver.find_elements(By.TAG_NAME, 'img') if e.get_attribute('alt')!='']
    
    nombre = data[0][6:]
    #posicion = data[1]
    
    if data[2] == 'Top' or data[2] == 'Mid' or data[2] == 'Jungla' or data[2] == 'ADC' or data[2] == 'Support':
        fuerte = data[3:8]
        fuerte_str = ''
        for e in fuerte:
            fuerte_str += e + ' '
        fuerte_str = fuerte_str[:-1]
            
        debil = data[8:13]
        debil_str = ''
        for e in debil:
            debil_str += e + ' '
        debil_str = debil_str[:-1]
        
        hechizos = data[13:15]
        hechizos_str = ''
        for e in hechizos:
            hechizos_str += e + ' '
        hechizos_str = hechizos_str[:-1]
        
        obj_ini = data[15:17]
        obj_ini_str = ''
        for e in obj_ini:
            obj_ini_str += e + ' '
        obj_ini_str = obj_ini_str[:-1]
        
        item_1 = data[17]
        item_2 = data[18]
        item_3 = data[19]
        item_4 = data[20]
        item_5 = data[21]
        item_6 = data[22]
    
    
    else:
        fuerte = data[2:7]
        fuerte_str = ''
        for e in fuerte:
            fuerte_str += e + ' '
        fuerte_str = fuerte_str[:-1]
        
        debil = data[7:12]
        debil_str = ''
        for e in debil:
            debil_str += e + ' '
        debil_str = debil_str[:-1]
        
        hechizos = data[12:14]
        hechizos_str = ''
        for e in hechizos:
            hechizos_str += e + ' '
        hechizos_str = hechizos_str[:-1]
        
        obj_ini = data[14:16]
        obj_ini_str = ''
        for e in obj_ini:
            obj_ini_str += e + ' '
        obj_ini_str = obj_ini_str[:-1]
        
        item_1 = data[16]
        item_2 = data[17]
        item_3 = data[18]
        item_4 = data[19]
        item_5 = data[20]
        item_6 = data[21]
        
    
    
    data_clean = {'campeon':nombre,
                  #'posicion':posicion,
                  'fuerte':fuerte_str,
                  'debil': debil_str,
                  'hechizos':hechizos_str,
                  'obj_ini':obj_ini_str,
                  'item_1':item_1,
                  'item_2':item_2,
                  'item_3':item_3,
                  'item_4':item_4,
                  'item_5':item_5,
                  'item_6':item_6,
                  }
                  
    
    driver.quit()
    
    return data_clean




def extraer_runas(url):
    
    html = requests.get(url).text

    sopa = BeautifulSoup(html, 'html.parser')
    
    runas = sopa.find_all('div', {'class':'hidden lg:block truncate font-semibold'})
    
    lista = [e.text for e in runas]
    
    lista = lista[:7]
    word = ''
    
    for e in lista:
        word += e + ',' + ' '
    word = word[:-1]
    
    nombre = sopa.find('h1', {'class':'text-2xl truncate'}).text[6:]
    
    
    data = {'campeon':nombre,
            'runas':word}
    
    return data