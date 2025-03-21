import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
# import pymongo
import os


save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

query = "charu singh kiet linkedin"
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")


soup = BeautifulSoup(response.content ,'html.parser')
# print(soup)

images_tags = soup.find_all("img")
print(len(images_tags))

img_data_mongo = []
for idx, i in enumerate(images_tags):
    image_url = i['src']
    try:
        image_data = requests.get(image_url).content
        img_data_mongo.append({"index": image_url, "image": image_data})
        with open(os.path.join(save_dir, f"{query}_{idx}.jpg"), "wb") as f:
            f.write(image_data)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {image_url}: {e}")
