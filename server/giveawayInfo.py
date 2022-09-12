import requests
from bs4 import BeautifulSoup

website_url = 'https://asset.party/get/developer/preview'

class GiveawayInfo:
    def __init__(self):
        None
    
    def get_web_content(self):
        self._req = requests.get(website_url)
        self._web_content = self._req.content
        return self._web_content

    def get_keys(self, content):
        self._scraper = BeautifulSoup(content, 'html.parser')
        for key in self._scraper.find_all('span', {'class': 'tag'}):
            self._element = key.find('i').getText()
            if (self._element == 'key'):
                self._keys = key.getText()
                self._keys = self._keys.replace('key', '')
                return self._keys.replace(' ', '')

    def get_viewers(self, content):
        self._scraper = BeautifulSoup(content, 'html.parser')
        for viewer in self._scraper.find_all('span', {'class': 'tag'}):
            self._element = viewer.find('i').getText()
            if (self._element == 'visibility'):
                self._viewers = viewer.getText()
                self._viewers = self._viewers.replace('visibility', '')
                return self._viewers.replace(' ', '')