import requests
from bs4 import BeautifulSoup

import time
from selenium import webdriver
from textblob import TextBlob



def youtubeselenium(link):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1200x600')

    driver = webdriver.Chrome(r'C:\Users\hp\Desktop\jerin_paper\chromedriver', options=chrome_options)

    driver.get(link)

    driver.execute_script('window.scrollTo(1, 500);')

    time.sleep(5)

    driver.execute_script('window.scrollTo(1, 3000);')

    comment_div = driver.find_element_by_xpath('//*[@id="sections"]')
    comments = comment_div.find_elements_by_xpath('//*[@id="content-text"]')
    for comment in comments:
        text = comment.text
        blob = TextBlob(text)
        print(text)
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity)





q = input("search : ")
s = requests.Session()
q = '+'.join(q.split())
url = 'https://www.youtube.com/search?q=' + q
r = s.get(url)


soup = BeautifulSoup(r.content, "html.parser")
count = 0
odd = -1


for link in soup.find_all('a', href=True):
    odd += 1
    if odd%2==0:
        if '/watch?v' in link['href'] and len(link['href'])==20:
            print('https://www.youtube.com' + link['href'])
            if(count < 2):
                linker = 'https://www.youtube.com' + link['href']
                req = s.get(linker)
                soup2 = BeautifulSoup(req.content, "html.parser")
                print(soup2.find('title'))
                youtubeselenium(linker)
                count+=1

    print()