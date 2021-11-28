import os
import sys
import urllib
import urllib.request
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_links(url: str):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    no_dup_link = []
    if url != []:
        selenium = webdriver.Chrome(options=options)
        selenium.get(url)
        links = selenium.find_elements_by_xpath("//a[@href]")
        for i in links:
            link = i.get_attribute("href")
            link = link.split("#")
            link = link[0].split("?")
            if link[0] not in no_dup_link and link[0] != '':
                no_dup_link.append(link[0])
    return no_dup_link
    
    
def is_valid_url(url: str)->bool:
    """Check is url valid or not

    Args:
        url (str): string of url

    Returns:
        bool: retrun true if url is valid
    """
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(url,None,headers)
    try:
        urllib.request.urlopen(request)
        return True
    except urllib.error.HTTPError:
        return False
    
    
def invalid_urls(urllist: List)->List:
    """If url is invalid put url in list and return list

    Args:
        urllist (List): list of urls

    Returns:
        List: return list of invalid url
    """
    invalid_list = []
    for url in urllist:
        if not is_valid_url(url):
            invalid_list.append(url)
    return invalid_list

# print(invalid_urls(["https://cpske.github.io/ISP/bad/index"]))
# get_links("https://cpske.github.io/ISP/")

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except:
        print("Usage:  python3 link_scan.py url \n\nTest all hyperlinks on the given url.")
        url = []
    all_urls = get_links(url)
    bad_urls = invalid_urls(all_urls)
    print_str = ""
    for url in all_urls:
        print_str += url + "\n"
    if len(bad_urls) > 0:
        print_str += "\nBad Links:\n"
    for url in bad_urls:
        print_str += url + "\n"
    print(print_str)
