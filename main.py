#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Feito por Dennys Augustus / dennysaug@gmail.com


import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException



def main():
    os.system('clear')
    print '######### Robot para publicar anuncio na olx ######### \n\n'
    #usuario = raw_input("Entre com o usuário: ")
    #senha = raw_input("Entre com a senha: ")
    #dia = int(raw_input("Repostar em dia(s): "))

    logins = []
    logins.insert(0, {"login": "seixas.camilla@hotmail.com", "senha": "xxx"})
    logins.insert(1, {"login": "dennysaugustus@hotmail.com", "senha": "xxx"})    
    logins.insert(2, {"login": "dennysaug@gmail.com", "senha": "xxx"})

    postcount = {"dennysaug@gmail.com": 0, "seixas.camilla@hotmail.com": 0, "dennysaugustus@hotmail.com": 0}
    dia = 2

    destino = r"/home/pi/Downloads/olx/anuncios"

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

            deletarPost(browser)

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
                preco = "90"
                cep = "66060460"

                time.sleep(5)

                if not usuario == "seixas.camilla@hotmail.com":
                    browser.find_element_by_id("phone_hidden").click()
                    browser.find_element_by_id("name").clear()
                    browser.find_element_by_id("name").send_keys("Camilla Seixas")

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
                time.sleep(5)
                #browser.find_element_by_name("image").send_keys(destino+"/"+diretorio+"/06.jpg")
                #time.sleep(10)
                
                scroll = browser.find_element_by_class_name('copyright')
                scroll.location_once_scrolled_into_view                               
                             
                browser.find_element_by_name("create").click()
                time.sleep(10)

                print "[*] Publicacao concluida"
                postcount[usuario] += 1
                print "[*] Total de anuncios: " + str(postcount[usuario]) +"\n"
                i += 1
            browser.quit()
            time.sleep(dia * 84600)




        print "######## FIM ########"





def init():
    chromedriver = "/usr/lib/chromium-browser/chromedriver"
    os.environ['webdriver.chrome.driver'] = chromedriver
    browser = webdriver.Chrome(chromedriver)
    browser.delete_all_cookies()
    browser.maximize_window()
    return browser

def deletarPost(browser):
    i = 1
    while True:
        try:
            if not browser.current_url == "https://www3.olx.com.br/account/userads/":
                browser.get("https://www3.olx.com.br/account/userads/")

            post = browser.find_element_by_class_name("description__action")
            deletar = post.find_elements_by_tag_name("a")[1]
            deletar.click()
            time.sleep(6)
            browser.find_element_by_id("reason_3").click()
            time.sleep(2)
            browser.find_element_by_class_name("close-lightbox").click()
            browser.find_element_by_id("level_10").click()
            browser.find_element_by_id("bt_continue").click()
            print "[*] Deletando " + str(i) + " anuncio(s)"
            i += 1
            time.sleep(6)

        except NoSuchElementException:
            print "[*] Nenhum anuncio para deletar"
            break






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
