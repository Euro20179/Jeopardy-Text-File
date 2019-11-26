import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

roundMoney = []

with open("all.txt", "w") as file:
	file.write("TOP")

for x in range(6474):

	start = time.time()
	
	url = f'http://www.j-archive.com/showscores.php?game_id={x}'

	page = requests.get(url)

	money = []

	soup = BeautifulSoup(page.text, 'html.parser')
	main = soup.find_all("h1")

	with open("all.txt", "a") as file:
		for m in main:
			file.write(f'\n{m.text}')

	scraped = soup.find_all("td", class_="score_positive" or "score_negative")

	for item in scraped:
		money.append(item.text)
		if len(money) == 3:
			with open("all.txt", "a") as file:
				file.write(f'\n{str(tuple(money))}')
			money.clear()

	print(f'{x}/6473 pages\nETA: {((time.time()-start) * (6673 - x)) / 60}')