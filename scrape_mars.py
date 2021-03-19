from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://mars.nasa.gov/news/'

browser.visit(url)
html = browser.html
soup = bs(html, "html.parser")
#news_title = "NASA's Persever....." find a way to get beautifulsoup to print this
news_title = soup.find("div", class_="content_title").text
print(news_title)
news_para = soup.find("div", class_= "article_teaser_body").text
print(news_para)
#Space Images
image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
browser.visit(image_url)
#not sure how to use splinter for this but hovering over the image link in inspector mode gave me the link
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'
#Mars Facts
facts_url = 'https://space-facts.com/mars/'
#thank you Google on how to read html in pandas
mars_facts = pd.read_html(facts_url)
#indexing to see if that helps
mars_facts[0]
#it helps to do variables in the correct order
mars_table = mars_facts[0]
mars_table.columns = ["Information", "Values"]
mars_table = mars_table.set_index(["Information"])
html_string = mars_table.to_html()
html_string
#Mars Hemispheres
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemi_url)
hemisphere_images_urls = []
cerebus_img = browser.links.find_by_text('Cerberus Hemisphere Enhanced')
time.sleep(5)
cerebus_img