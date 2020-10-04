from selenium import webdriver

a = input()
#d = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('headless')
d = webdriver.Chrome(chrome_options=options)


#d.maximize_window()
d.get('https://yandex.ru')
usd = d.find_element_by_xpath('//*[@id="wd-_topnews"]/div/div[3]/div/div/div[1]')
eur = d.find_element_by_xpath('//*[@id="wd-_topnews"]/div/div[3]/div/div/div[2]')
if a == 'usd' or a == 'USD':
    print(usd.text)
if a == 'eur' or a == 'EUR':
    print(eur.text)
if a == 'all':
    print(usd.text)
    print(eur.text)