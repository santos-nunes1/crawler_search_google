from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from pytz import timezone
import logging
import platform
import time

global driver
global modo_chrome


def seta_funcoes_chrome(modo_chrome):

    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument("--no-sandbox")
    chrome_opt.add_argument("ignore-certificate-errors")
    chrome_opt.add_argument("--start-fullscreen")
    chrome_opt.add_argument('--disable-logging')

    if modo_chrome.upper() == "OFF":
        chrome_opt.add_argument("--headless")


    return chrome_opt



def executa_crawler(execucoes=50, modo_chrome="off"):

    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=seta_funcoes_chrome(modo_chrome))

    mensagens = [
        "https://www.google.com/search?q=Bolsonaro+pedofilo",
        "https://www.google.com/search?q=Bolsonaro+orcamento+secreto",
        "https://www.google.com/search?q=Bolsonaro+preco+gasolina",
        "https://www.google.com/search?q=Bolsonaro+nao+comprou+vacina",
        "https://www.google.com/search?q=Bolsonaro+salario+minimo+2023",
        "https://www.google.com/search?q=Bolsonaro+corte+educacao+saude",
        "https://www.google.com/search?q=Bolsonaro+51+imoveis",
        "https://www.google.com/search?q=Bolsonaro+desmatamento"
    ]

    count = 0
    for k in range(execucoes):
        for i in mensagens:
            count = count + 1
            print (count)
            print(i)
            driver.get(i)
            time.sleep(2)
    driver.close()

executa_crawler(1, "on")