import requests
from bs4 import BeautifulSoup
import re

class WebScraper:
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
        news_divs = soup.find_all('div', class_='col-lg-3 col-sm-6 grid-margin mb-5 mb-sm-2')

        for news_div in news_divs:
            h5_tag = news_div.find('h5')
            p_tag = news_div.find('p')
            if h5_tag and p_tag:
                link_tag = h5_tag.find('a')
                description = p_tag.get_text(strip=True).strip(".,")
                if link_tag:
                    headline_text = link_tag.get_text(strip=True).strip(".")
                    article_url = link_tag['href']
                    if article_url.startswith('/'):
                        article_url = 'https://www.deccanchronicle.com' + article_url
                    headlines_list.append((headline_text, article_url, description))

        return headlines_list

    def extract_headlines_from_multiple_pages(self):
        all_headlines = []
        for page_num in range(1, self.num_pages_to_scrape + 1):
            url = self.base_url if page_num == 1 else f'{self.base_url}/{page_num}'
            print(f"Extracting headlines from: {url}")
            headlines = self.extract_headlines_from_page(url)
            all_headlines.extend(headlines)
        return all_headlines

    def filter_headlines_by_keywords(self, headlines_data):
        filtered_headlines = []
        for headline, url, desc in headlines_data:
            if any(keyword.lower() in headline.lower() for keyword in self.keywords) or any(keyword.lower() in desc.lower() for keyword in self.keywords):
                filtered_headlines.append((headline, url, desc))
        return filtered_headlines

    def extract_information_from_headlines(self, headlines):
        text_content = []
        for (headline, url, desc) in headlines:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            main_content = soup.find('div', class_='entry-main-content dropcap')

            # List of potential containers for text (paragraphs, divs, etc.)
            containers = main_content.find_all(['p', 'div'])
            for container in containers:
                text = container.get_text(separator='\n').strip()
                # Only append non-empty and non-overlapping text
                if text and not self.is_substring(text, text_content):
                    text_content.append(text)

            # Filter out unwanted text
            unwanted_prefix = "Download the all new Deccan Chronicle app"
            text_content = [text for text in text_content if not text.startswith(unwanted_prefix)]
        return text_content
    
    def extract_sentences_with_numerical_data(self, text_content):
        sentences_with_numbers = []
        for paragraph in text_content:
            # Split the paragraph into individual sentences
            sentences = re.split(r'(?<=[.!?]) +', paragraph)
            
            # Check if the sentence contains any numerical data
            for sentence in sentences:
                if re.search(r'\d+', sentence):  # Looks for digits in the sentence
                    sentences_with_numbers.append(sentence.strip())
        
        return sentences_with_numbers

    def is_substring(self, new_text, text_list):
        for existing_text in text_list:
            if new_text in existing_text or existing_text in new_text:
                return True
        return False

    # def save_to_file(self, text_content, file_name='web_scraped_data.txt'):
    #     with open(file_name, 'w') as file:
    #         for text in text_content:
    #             file.write(text + '\n\n')

