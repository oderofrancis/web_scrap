#IMPORT THE PYTON MODULES FOR WEB SCRAPPING

import re

import requests

from bs4 import BeautifulSoup

import urllib.request as DFU

from termcolor import colored

import os


url = input("https://www.instagram.com/p/CaZaOnaMxjc/?utm_source=ig_web_copy_link")

data = requests.get(url)

print(data)

str = data.text



match = re.findall(r'url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count', str)

extraction = ".mp4"


if len(match) == 0:

 match = re.findall(r'profile_pic_url\W\W\W([-\W\w]+)\W\W\Wdisplay_resources', str)

 extraction = ".jpg"

res = match[0]


page = BeautifulSoup(str, "html.parser")

title = page.find("title")

title = title.get_text()

title = re.sub(r"\W+", "_", title)



print("\n"+title)

title = "download/web_scrap"+title+"web_scrap"

title = title





if res != "" :

 print('found \n \n'+'\033[1m'+colored(res, 'green')+'\033[0m'+'\n')

 download = input("Do you want to download(y/N) : ")

 if (download == "y" or download == "Y"):
  try:
   fileName = title
   print("Downloading.....")
   DFU.urlretrieve(res, fileName+extraction)
   print("Download Successfully!")
   os.system("tree download")

  except:
   print("Sorry! Download Unsuccessful")



else:
 print('did not find or post is from private account')
 exit()

