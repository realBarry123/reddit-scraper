from bs4 import BeautifulSoup
import requests

def get_data(url):
    r = requests.get(url, headers = {"Content-Type":"text"})
    return r.text

soup = BeautifulSoup(get_data("https://www.reddit.com/r/copypasta/comments/15wihsx/i_saw_a_school_girls_shoulder/"), 'html.parser')
#print(soup)

data_str = ""

for item in soup.find_all("div", attrs={"class": "_2mHuuvyV9doV3zwbZPtIPG"}):
    data_str += item.get_text()
    print("1")

print(data_str)