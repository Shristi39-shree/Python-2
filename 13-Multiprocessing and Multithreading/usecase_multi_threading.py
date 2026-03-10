'''

Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to fetch web pages. These tasks are I/O-bound because they spend a lot of time waiting for response from servers. Multithreading can significantly improve the performance by allowing multiple web pages to be fetch concurrently.

''' 

# https://www.wikipedia.org/
# https://en.wikipedia.org/wiki/English_Wikipedia
# https://wikimediafoundation.org/


### To check whether its working or not 
# import requests
# from bs4 import BeautifulSoup
# print("Everything working!")

import threading
import requests
from bs4 import BeautifulSoup

urls=[
 'https://www.wikipedia.org/',
 'https://en.wikipedia.org/wiki/English_Wikipedia',
 'https://wikimediafoundation.org/'

]

def fetch_content(url):
  response=requests.get(url)
  soup=BeautifulSoup(response.content,'html.parser')
  print(f'Fetched {len(soup.text)} chracters from {url}')

threads=[]

for url in urls:
  thread=threading.Thread(target=fetch_content,args=(url,))
  threads.append(thread)  
  thread.start()

for thread in threads:
  thread.join()

print("All web pages fetched")