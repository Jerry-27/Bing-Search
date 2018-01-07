from splinter import Browser
from bs4 import BeautifulSoup
from time import sleep
from database import database
from random import randint
import os

base = database(name = 'words',location = 'C:\\Users\\Kelvin\\Documents\\python programming\\Random Databases')


url_signin = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1497478941&rver=6.7.6631.0&wp=MBI&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1&lc=1033&id=264960&CSRFToken=261c7194-3ede-4c1a-bb5f-be0641f7b8c4"
url_search = "https://www.bing.com"


email = 'emaail'
password = 'password'

#Navigate to site
browser = Browser()



def logon(browser,email,password):
    #Visit logon site
    browser.visit(url_signin)
    sleep(10)

    #Enter email information and click next
    browser.find_by_name('loginfmt').first.fill(email)
    sleep(2)
    next_button = browser.find_by_id('idSIButton9')
    next_button.click()
    sleep(2)

    #Enter password information and login
    browser.find_by_name('passwd').first.fill(password)
    sleep(2)
    signin_button = browser.find_by_id('idSIButton9')
    sleep(3)
    signin_button.click()

    return browser

def search_term():
    word = base.get_ranword()
    print("Searching for the word ", word)
    return word

def wait_random():
    number = randint(1,5)
    minutes = number*60

    number = randint((minutes/4),(minutes/2))
    
    wait_time = abs(minutes - number)
    print("Waiting a total of ",(wait_time/60), "minutes.")
    sleep(wait_time)

def search_site():
    searchTerm = search_term()
    
    browser.find_by_id('sb_form_q').first.fill(searchTerm)
    browser.find_by_id('sb_form_go').click()
    wait_random()

logon(browser,email,password)
rand = randint(15,30)
print("Total Number of Searches: ",rand)
for n in range(rand):
    search_site()
    
for window in browser.windows:
    window.close()    
