import requests
from bs4 import BeautifulSoup
import operator

def start(url):
	word_list = []
	source_code = requests.get(url)
	soup = BeautifulSoup(source_code)
	for main_text in soup.findAll('a',{"class": "__|?|__"}): #give_class
		content = main_text.string
		words = content.lower().split()
		for each_word in words:
			word_list.append(each_word)
	clean_up_list(word_list)

def clean_up_list(word_list):
	new_world_list = []
	for word in word_list:
		symbols = "!@#$%^&*()_+=`~,./;'<>?:\"[]{}\\|"
		for i in range(0, len(symbols)):
			word = word.replace(symbols[i], "")
		if len(word) > 0:
			new_world_list.append(word)
	word_counter(new_world_list)
			
def word_counter(new_world_list):
	word_count = {}
	for word in new_world_list:
		if word in word_count:
			word_count[word] += 1
		else
			word_count[word] = 1
	for key,value in sorted(word_count.items(), key = operator.itemgetter(1)):
		print(key, value)

url = input('Enter URL') #enter url
start(url)