import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	pages = 1
	while page <= max_pages:
		url = 'http://buckysroom.org/trade/search.php?pages=' + str(pages)
		soruce_code = requests.get(url)
		plain_text = soruce_code.text
		soup = BeautifulSoup(plain_text)
		
		name_page = r"crawl" + str(pages) + ".text"
		fw = open(name_page, 'w')

		for link in soup.findAll('a', {'class': 'item-name'}) :
			href = "http://buckysroom.org/" + link.get('href')
			title = link.string
			fw.write(href + '\n')
			fw.write(title + '\n \n')
			
		fw.close()
		page += 1

trade_spider(3)