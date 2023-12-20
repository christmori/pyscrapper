import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve

def download_image(url, folder_path):
     try:
         response = requests.get(url)
         if response.status_code == 200:
             # Get the file name from the URL
             filename = os.path.join(folder_path, os.path.basename(urlparse(url).path))
             with open(filename, 'wb') as f:
                 f.write(response.content)
             print(f"Image saved: {filename}")
         else:
             print(f"Failed to load image: {url}")
     except Exception as e:
         print(f"Error loading image {url}: {e}")

def scrape_images(url, folder_path):
     try:
         response = requests.get(url)
         if response.status_code == 200:
             soup = BeautifulSoup(response.text, 'html.parser')
             # Find all <img> tags
             img_tags = soup.find_all('img')
             for img_tag in img_tags:
                 # Get the image URL
                 img_url = urljoin(url, img_tag['src'])
                 # Save the image
                 download_image(img_url, folder_path)
         else:
             print(f"Failed to get page: {url}")
     except Exception as e:
         print(f"Error scraping images: {e}")

if __name__ == "__main__":
      # Set the site URL and folder for saving images
      website_url = "https://pypi.org/project/Scrapy/"
      download_folder = "images"

      # Check if the folder exists and create it if not
      if not os.path.exists(download_folder):
          os.makedirs(download_folder)

      # Start scraping images
      scrape_images(website_url, download_folder)
