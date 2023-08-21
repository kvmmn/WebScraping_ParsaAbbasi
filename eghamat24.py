import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.eghamat24.com/KishHotels/ShayanHotel.html"

response = requests.get(url)
# print('status code:', response.status_code)

# print('response: ', response.text)
soup = BeautifulSoup(response.text, "html.parser")

# Title
title = soup.find("h1", attrs={"class": "hotel_name"}).text
print("title", title)

# Star
star = soup.find("span", attrs={"class": "hotel_grid"}).text
star = star.replace(")", "").replace("(", "")
print("star", star)

# count_room, count_floor, check_in, check_out
this_tag = soup.find("div", attrs={"class": "hotel_details_overview"})

information_tags = this_tag.find_all("li")

info_dict = {}

for info_tag in information_tags:
    info = info_tag.text
    if "تعداد طبقه" in info:
        re_pattern = r"تعداد طبقه(\d+)"
        count_floor = int(re.findall(re_pattern, info)[0])
        print("count_floor:", count_floor)
        # info_dict['count_floor'] = count_floor
    elif "تعداد اتاق" in info:
        pass
