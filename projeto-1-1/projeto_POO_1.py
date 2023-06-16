from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
<<<<<<< HEAD
import pandas as pd
import py7zr
import getpass
=======
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
import shutil
import os
>>>>>>> 8883c6cde77a995bad33862d2e6b21a232953244

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
<<<<<<< HEAD
options.add_experimental_option("prefs", {
    "download.default_directory": "C:\\Projeto_Alta\\projeto-1-1"  # Substitua pelo caminho da pasta desejada
})

print('É importante esse arquivo tenha o seguinte caminho: C:\Projeto_Alta\projeto-1-1')
email = input('digite o email do usuario: ')
password = getpass.getpass("digite a sua senha: ")
=======


>>>>>>> 8883c6cde77a995bad33862d2e6b21a232953244

driver = webdriver.Chrome(options=options)
url_login = 'https://estudante.estacio.br/login'
url_tema = 'https://estudante.estacio.br/disciplinas'


<<<<<<< HEAD
=======
email = input('digite o email do usuario: ')
password = input("digite a sua senha: ")


>>>>>>> 8883c6cde77a995bad33862d2e6b21a232953244
class Extrai:
    def __init__(self, email, password, driver):
        self.email = email
        self.password = password
        self.driver = driver


<<<<<<< HEAD
=======

>>>>>>> 8883c6cde77a995bad33862d2e6b21a232953244
    def login(self):

     self.driver.get(url_login)
     sleep(10)

     button_entrar = self.driver.find_element(By.XPATH, '//*[@id="section-login"]/div/div/div/section/div[1]/button')
     button_entrar.click()

     sleep(10)

     login = self.driver.find_element(By.NAME, 'loginfmt')
     login.send_keys(self.email)
     button_avancar_email = self.driver.find_element(By.ID, 'idSIButton9')
     button_avancar_email.click()
<<<<<<< HEAD
     sleep(5)
     senha = self.driver.find_element(By.NAME, 'passwd')
     senha.send_keys(self.password)
     sleep(5)
=======
     sleep(2)
     senha = self.driver.find_element(By.NAME, 'passwd')
     senha.send_keys(self.password)
     sleep(2)
>>>>>>> 8883c6cde77a995bad33862d2e6b21a232953244

     button_avancar_senha = self.driver.find_element(By.ID, 'idSIButton9')
     button_avancar_senha.click()

     button_nao = self.driver.find_element(By.ID, 'idBtn_Back')
     button_nao.submit()

     sleep(10)



    def estudante_tema(self):
     self.driver.get(url_tema)
     sleep(10)
     disc = self.driver.find_element(By.XPATH, '//*[@id="card-entrega-ARA0066"]')
     disc.click()
     sleep(5)

     tema = self.driver.find_element(By.XPATH, '//*[@id="temas-lista-topicos"]/li[5]/a/div')
     tema.click()
     sleep(5)

     pag = driver.find_element(By.XPATH, '//*[@id="segunda-tab"]').click()
     sleep(2)

     download = driver.find_element(By.XPATH, '//*[@id="acessar-conteudo-complementar-arquivo-64615eb275e90c00266b9ff9"]').click()
     sleep(250)

<<<<<<< HEAD
     self.driver.quit()



    def  extrai_dados(self):
      with py7zr.SevenZipFile('C:\\Projeto_Alta\\projeto-1-1\\5m-Sales-Records.7z', mode='r') as z: z.extractall()
      csv = pd.read_csv('C:\\Projeto_1\\Projeto_Alta-1-1\\5m Sales Records.csv')
      csv = csv.fillna(value=0)
      csv['Order Date'] = pd.to_datetime(csv['Order Date'])
      csv['Ship Date'] = pd.to_datetime(csv['Order Date'])
      csv['Order ID'] = csv['Order ID'].astype(int)
      csv['Units Sold'] = csv['Units Sold'].astype(int)
      linhas = 25000
      arquivos = int(len(csv) / linhas) + 1
      lista_dt = [csv[i:i+linhas] for i in range(0,len(csv), linhas)]
    #   lista_dt[0].to_excel('C:\\Projeto_1\\projeto-1-1\\1m_Sales_Records.xlsx')
      for i, csv_temp in enumerate(lista_dt):
       csv_temp.to_excel(f'C:\\Projeto_Alta\\projeto-1-1\\5m_Sales_Records{i+1}.xlsx',index=False)
=======





    def  extrai_dados():
       print()








>>>>>>> 8883c6cde77a995bad33862d2e6b21a232953244


extrai = Extrai(email, password, driver)

extrai.login()
extrai.estudante_tema()
<<<<<<< HEAD
extrai.extrai_dados()
=======
>>>>>>> 8883c6cde77a995bad33862d2e6b21a232953244



