#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Feito por Dennys Augustus / dennysaug@gmail.com


import os
import time
import glob
from selenium import webdriver



def main():
    os.system('clear')
    print '######### Robot para publicar anuncio na olx ######### \n\n'
    #usuario = raw_input("Entre com o usuário: ")
    #senha = raw_input("Entre com a senha: ")
    #dia = int(raw_input("Repostar em dia(s): "))

    logins = []
    logins.insert(0, {"login": "dennysaug@gmail.com", "senha": "xxx"})


    postcount = {"dennysaug@gmail.com": 0}
    dia = 2

    destino = r"/home/dennys/PycharmProjects/olx/anuncios"

    os.system('clear')

    i = 0


    if True:
        while True:
            browser = init()
            browser.get("https://pa.olx.com.br")
            print "[*] Efetuando login"

            index = i % 3
            usuario = logins[index]['login']
            senha = logins[index]['senha']
            print "[*] Conta: " +usuario

            browser.get("https://www3.olx.com.br/account/form_login/")
            browser.find_element_by_id("login_email").send_keys(usuario)
            browser.find_element_by_id("login_password").send_keys(senha)
            browser.find_element_by_id("bt_submit_login").click()
            time.sleep(10)

            anuncios = os.listdir(destino)
            for diretorio in anuncios:
                print "[*] Publicando anuncio: " + diretorio
                browser.get("http://www2.olx.com.br/ai")

                config = open(destino+"/"+diretorio+"/config.txt", "r").read()
                texto = open(destino+"/"+diretorio+"/texto.txt", "r").read()

                #print config
                #print texto

                print "[*] Preenchendo os campos"

                categoria = "8000" #"Moda e beleza"
                subcategoria = "8060" #""Bolsas, malas e mochilas"
                novoUsado = "Novo"
                titulo = "Bolsas Feminina (Promoção)"
                preco = ""
                cep = "66060460"

                time.sleep(5)

                if not usuario == "xxxxxxx@hotmail.com":
                    browser.find_element_by_id("phone_hidden").click()
                    browser.find_element_by_id("name").clear()
                    browser.find_element_by_id("name").send_keys("xxxxx")

                browser.find_element_by_id(categoria).click()
                time.sleep(2)
                browser.find_element_by_id(subcategoria).click()
                time.sleep(5)
                browser.find_element_by_id("condition").send_keys(novoUsado)
                time.sleep(2)
                browser.find_element_by_id("subject").send_keys(titulo.decode("utf-8"))
                browser.find_element_by_id("body").send_keys(texto.decode("utf-8"))
                browser.find_element_by_id("price").send_keys(preco)
                browser.find_element_by_id("zipcode").send_keys(cep)



                print "[*] Upload das fotos"
                browser.find_element_by_name("image").send_keys(destino+"/"+diretorio+"/01.jpg")
                time.sleep(2)
                browser.find_element_by_name("image").send_keys(destino+"/"+diretorio+"/02.jpg")
                time.sleep(2)
                browser.find_element_by_name("image").send_keys(destino+"/"+diretorio+"/03.jpg")
                time.sleep(2)
                browser.find_element_by_name("image").send_keys(destino+"/"+diretorio+"/04.jpg")
                time.sleep(2)
                browser.find_element_by_name("image").send_keys(destino+"/"+diretorio+"/05.jpg")
                #time.sleep(2)
                #browser.find_element_by_name("image").send_keys(destino+"/"+diretorio+"/06.jpg")
                #time.sleep(10)



                #browser.find_element_by_id("submit_create_now").click()
                time.sleep(10)

                print "[*] Publicacao concluida\n"
                postcount[usuario] += 1
                print "[*] Total de anuncios: " + str(postcount[usuario])
                i += 1
            browser.quit()
            time.sleep(dia * 15)




        print "######## FIM ########"





def init():
    chromedriver = "/usr/lib/chromium-browser/chromedriver"
    os.environ['webdriver.chrome.driver'] = chromedriver
    browser = webdriver.Chrome(chromedriver)
    browser.delete_all_cookies()
    browser.maximize_window()
    return browser


if __name__ == '__main__':
    main()


"""
import os
from selenium import webdriver
chromedriver = "/usr/lib/chromium-browser/chromedriver"
os.environ['webdriver.chrome.driver'] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.delete_all_cookies()
browser.maximize_window()
browser.get("https://www3.olx.com.br/account/form_login/")
"""