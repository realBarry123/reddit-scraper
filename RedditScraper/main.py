from bs4 import BeautifulSoup
from selenium import webdriver

def get_data(url):
    #r = requests.get(url, headers = {"Content-Type":"text"})
    r = driver.get(url)
    return r.page_source

driver = webdriver.Chrome()
driver.get("https://www.reddit.com/r/UBC/comments/15xvfde/failed/")
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")
print(soup)


data_str = ""

for item in soup.find_all("div", attrs={"class": "_2mHuuvyV9doV3zwbZPtIPG"}):
    data_str += item.get_text()
    print("1")

for item in soup.find_all("div", class_="_2mHuuvyV9doV3zwbZPtIPG"):
    data_str += item.text.strip()
    print("1")

print(data_str)