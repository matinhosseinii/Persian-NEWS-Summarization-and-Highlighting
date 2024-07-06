from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

path = 'chromedriver-win64/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Set headless mode

def get_isna_titles():
    website = 'https://www.isna.ir/archive'
    driver = webdriver.Chrome(service=Service(path), options=chrome_options)
    driver.maximize_window()
    driver.get(website)
    choose_news_class_button = driver.find_elements(By.XPATH, '//span[@class="select2-selection__rendered"]')[4]
    choose_news_class_button.click()
    select_news_class_button = driver.find_element(By.XPATH, '//li[text()="اختصاصی خبر"]')
    select_news_class_button.click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()

    titles_div = soup.find('div',class_= 'items')
    h3 = titles_div.find_all('h3')
    titles = {}
    for title in h3:
        a = title.find('a', href=True)
        url = f'https://www.isna.ir/{a["href"]}'
        heading = title.find('a').text
        titles[heading] = url

    return titles

def get_irna_titles():
    website = 'https://www.irna.ir/archive'
    driver = webdriver.Chrome(service=Service(path), options=chrome_options)
    driver.maximize_window()
    driver.get(website)
    choose_news_class_button = driver.find_elements(By.XPATH, '//span[@class="select2-selection__rendered"]')[4]
    choose_news_class_button.click()
    select_news_class_button = driver.find_element(By.XPATH, '//li[text()="خبر"]')
    select_news_class_button.click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()

    titles_div = soup.find('div',class_= "col-12 col-sm-8 main-content")
    h3 = titles_div.find_all('h3')
    titles = {}
    for title in h3:
        a = title.find('a', href=True)
        url = f'https://www.irna.ir/{a["href"]}'
        heading = title.find('a').text
        titles[heading] = url

    return titles

def get_mehr_titles():
    website = 'https://www.mehrnews.com/archive'
    driver = webdriver.Chrome(service=Service(path), options=chrome_options)
    driver.maximize_window()
    driver.get(website)
    choose_news_class_button = driver.find_elements(By.XPATH, '//span[@class="select2-selection__rendered"]')[4]
    choose_news_class_button.click()
    select_news_class_button = driver.find_element(By.XPATH, '//li[text()="خبر"]')
    select_news_class_button.click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()

    titles_div = soup.find('div',class_= "col-12 col-sm-8")
    h3 = titles_div.find_all('h3')
    titles = {}
    for title in h3:
        a = title.find('a', href=True)
        url = f'https://www.mehrnews.com/{a["href"]}'
        heading = title.find('a').text
        titles[heading] = url

    return titles


def get_news_text(url):
    driver = webdriver.Chrome(service=Service(path), options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()

    return soup.find('div', class_="item-text").text