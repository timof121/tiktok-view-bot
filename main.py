import requests as r
import random
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:60.9) Gecko/20100101 Goanna/4.3 Firefox/60.9 Mypal/28.6.1',
    'authority': 'www.tiktok.com',
    'origin': 'https://www.tiktok.com',
}

proxy = set()
with open("proxy.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())

proxies = {
    'http': 'http://' + random.choice(list(proxy))
}

e = input('Video link: ')

while True:
    output = r.get(e, proxies=proxies)
    if output.ok:
        print('[+]Request succesfully sent!')
    else:
        print('[-]Failed to send request!')
    sleep(2)
