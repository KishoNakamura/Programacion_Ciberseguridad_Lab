from selenium import webdriver
import time
import os

def OpenChrome(nombre):
    PATH = "C:/WebDriver/chromedriver.exe"

    driver = webdriver.Chrome(PATH)
    driver.get("https://www.google.com")

    time.sleep(2)

    srch_tag = driver.find_element_by_name("q")
    srch_tag.send_keys(nombre)
    srch_btn = driver.find_element_by_name("btnK")
    srch_btn.submit()

    time.sleep(2)

    with open("Recursos/Urls.txt", "a") as file:
        for elemnt in driver.find_elements_by_xpath('//div[@class="tF2Cxc"]'):
            link = elemnt.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href')
            file.write(link + "\n")
    
    time.sleep(2)

    srch_tag2 = driver.find_element_by_name("q")
    srch_tag2.clear()
    srch_tag2.send_keys(nombre + " wegow")
    srch_tag2.submit()

    with open("Recursos/Urls.txt", "a") as file2:
        cont = 0
        for elemnt2 in driver.find_elements_by_xpath('//div[@class="tF2Cxc"]'):
            if cont >= 3:
                pass
            else:
                link = elemnt2.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href')
                file2.write(link + "\n")
            cont += 1

    time.sleep(2)

    srch_tag3 = driver.find_element_by_name("q")
    srch_tag3.clear()
    srch_tag3.send_keys(nombre + " noticias")
    srch_tag3.submit()
    
    with open("Recursos/Noticias.txt", "w", encoding="utf-8") as news:
        for elemnt3 in driver.find_elements_by_xpath('//div[@class="tF2Cxc"]'):
            title = elemnt3.find_element_by_xpath('.//h3').text
            link_news = elemnt3.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href')
            detail = elemnt3.find_element_by_xpath('.//span[@class="aCOpRe"]').text
            news.write(title + " | " + link_news + " | " + detail + "\n")
    
    time.sleep(2)
    driver.quit()