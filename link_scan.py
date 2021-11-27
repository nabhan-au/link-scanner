import urllib
from selenium import webdriver
from urllib.request import urlopen

def get_links(url: str):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    no_dup_link = []
    selenium = webdriver.Chrome()
    selenium.get(url)
    links = selenium.find_elements_by_xpath("//*[@href]")
    for i in links:
        link = i.get_attribute("href")
        link = link.split("#")
        link = link[0].split("?")
        if link[0] not in no_dup_link and link[0] != '':
            no_dup_link.append(link[0])
    return no_dup_link
    
    
def is_valid_url(url: str):
    try:
        response = urlopen(url)
        return True
    except:
        return False
    


print(is_valid_url("https://cpske.github.io/ISP/assignment/ku-polls/"))