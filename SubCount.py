
import requests
from bs4 import BeautifulSoup
from tkinter import *

try:
    id = input("Enter a Id: ")

    URL = 'https://socialblade.com/youtube/channel/' + id + "/realtime"
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find(id="userName").get_text()
    id =  soup.find(id="rawCount").get_text()

    print("The userName is "+ name + "and the count is " + id)
    print("Made By Tr1x")
except:
    print("Invalid Id")
