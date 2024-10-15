import requests
from bs4 import BeautifulSoup
import re

class HinduStateScraper:
    def __init__(self, base_url, keywords, num_pages_to_scrape=10):
        self.base_url = base_url
        self.keywords = keywords
        self.num_pages_to_scrape = num_pages_to_scrape

    def extract_headlines_from_page(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        headlines_list = []
        news_divs = soup.find_all('div', class_='right-content')

        for news_div in news_divs:
            h3_tag = news_div.find('h3')
            if h3_tag:
                link_tag = h3_tag.find('a')
                if link_tag:
                    headline_text = link_tag.get_text(strip=True)
                    article_url = link_tag['href']
                    if article_url.startswith('/'):
                        article_url = 'https://www.thehindu.com' + article_url
                    headlines_list.append((headline_text, article_url))

        return headlines_list

    def extract_headlines_from_multiple_pages(self):
        all_headlines = []
        for page_num in range(1, self.num_pages_to_scrape + 1):
            url = self.base_url if page_num == 1 else f'{self.base_url}?page={page_num}'
            print(f"Extracting headlines from: {url}")
            headlines = self.extract_headlines_from_page(url)
            all_headlines.extend(headlines)
        return all_headlines

    def filter_headlines_by_keywords(self, headlines_data):
        filtered_headlines = []
        for headline, url in headlines_data:
            if any(keyword.lower() in headline.lower() for keyword in self.keywords):
                filtered_headlines.append((headline, url))
        return filtered_headlines

    def extract_information_from_headlines(self, headlines):
        text_content = []
        for (headline, url) in headlines:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            article_body = soup.find('div', class_='articlebodycontent')

            if article_body:
                for element in article_body.children:
                    if element.name == 'p':
                        text_content.append(element.get_text(strip=True))
                    if element.name == 'div' and 'articleblock-container' in element.get('class', []):
                        break
        return text_content

    def extract_sentences_with_numerical_data(self, text_content):
        sentences_with_numbers = []
        for paragraph in text_content:
            sentences = re.split(r'(?<=[.!?]) +', paragraph)
            for sentence in sentences:
                if re.search(r'\d+', sentence):
                    sentences_with_numbers.append(sentence.strip())
        return sentences_with_numbers

    def save_to_file(self, text_content, file_name='web_scraped_data.txt'):
        with open(file_name, 'w') as file:
            for text in text_content:
                file.write(text + '\n\n')