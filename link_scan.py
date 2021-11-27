import os
import sys
import urllib
from typing import List
from selenium import webdriver

def get_links(url: str):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    no_dup_link = []
    selenium = webdriver.Chrome()
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
    try:
        urllib.request.urlopen(url)
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
    url = sys.argv[1]
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