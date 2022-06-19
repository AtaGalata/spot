from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os, time
#GEREKLİ YER BAŞ
ad = input("Adınızı Giriniz : ")
sifre = input("Olmasını İstediğiniz Sifreyi Giriniz : ")
dt_gün = "07"
dt_yıl = "1975"
dt_gün = "07"
chromePath ="chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromePath)
act=ActionChains(driver)
#GEREKLİ YER SON

#FAKE MAİL ALMA BAŞ
driver.get('https://tempail.com/tr/')
time.sleep(5)
driver.find_element_by_xpath('/html/body/section[1]/div[2]/div/div[4]/a[1]').click()
time.sleep(4)
#FAKE MAİL ALMA SON

#SPOTİFY BAŞ
driver.get('https://open.spotify.com/')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="onetrust-close-btn-container"]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]').click()
time.sleep(3)

#KAYIT BAŞ
driver.find_element_by_xpath('//*[@id="email"]').click()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
driver.find_element_by_xpath('//*[@id="confirm"]').click()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
driver.find_element_by_xpath('//*[@id="password"]').send_keys(sifre)
driver.find_element_by_xpath('//*[@id="displayname"]').send_keys(ad)

driver.find_element_by_xpath('//*[@id="day"]').send_keys(dt_gün)
driver.find_element_by_xpath('//*[@id="month"]').click()
driver.find_element_by_xpath('//*[@id="month"]/option[8]').click()
driver.find_element_by_xpath('//*[@id="year"]').send_keys(dt_yıl)


driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/form/div[7]/div/label').click()
driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/form/fieldset/div/div[3]/label/span[1]').click()
onay=input("\n\n\nonay gerekiyor lütfen siteden robot doğrulamasına basınız sonra 1 yazıp enterlayınız : ")
driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/form/div[9]/div/button').click()
time.sleep(10)
#KAYIT SON

#PRE ALMA BAŞ

driver.get("https://www.spotify.com/tr/purchase/offer/default-new-family-master-trial-1m/?country=TR")
time.sleep(10)
console.log("\n\n\n\n\nKart Bilgilerinizi Girip 1 Yazıp Enterlayınız : ")

#PRE ALMA SON

