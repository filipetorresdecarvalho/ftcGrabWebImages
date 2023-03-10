import os
import requests
from bs4 import BeautifulSoup

# set the base URL of the directory listing
base_url = "https://example.com/images/"

# download the directory listing HTML
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# find all the image links on the directory listing page
image_links = [link.get("href") for link in soup.find_all("a") if link.get("href").endswith(".jpg")]

# create a directory to store the downloaded images
if not os.path.exists("images"):
    os.makedirs("images")

# download each image that has not already been downloaded
for link in image_links:
    image_url = base_url + link
    file_path = f"images/{link}"
    if not os.path.exists(file_path):
        response = requests.get(image_url)
        with open(file_path, "wb") as f:
            f.write(response.content)
            print(f"Downloaded {link}")
    else:
        print(f"File {link} already exists, skipping download.")
