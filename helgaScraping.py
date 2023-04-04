#!/usr/bin/python3

# To the extent possible under law, the person who associated CC0 with
# this script has waived all copyright and related or neighboring rights
# to this script.
#
# You should have received a copy of the CC0 legalcode along with this
# work.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.

import json
import mechanicalsoup
import re

browser = mechanicalsoup.Browser()
p = browser.get('https://helga.hadiko.de/products/browse/')
p.raise_for_status()

last_page_link = p.soup.select_one('.last.page-item .page-link').attrs['href']
last_page_no = int(re.search(r'[0-9]+$', last_page_link)[0])

products = []

for page_no in range(1, last_page_no + 1):
	p = browser.get('https://helga.hadiko.de/products/browse/', params={'page': page_no})
	p.raise_for_status()
	for product in p.soup.select('.product-content'):
		title = product.select_one('.product-data a div').text.strip()
		price = re.match(r'[0-9]+\.[0-9]{2}', product.select_one('.product-price h3').text.strip())[0]
		products.append({'title': title, 'price': price})

print(json.dumps(products, ensure_ascii=False, indent='\t'))