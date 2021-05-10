import re
import urllib.request
import time
import random

for index in range(227, 1419):
    chaper_url = 'https://ctext.org/library.pl?if=gb&file=102034&page=%d' % (
        index)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=chaper_url, headers=headers)
    request = urllib.request.urlopen(req)
    buf = request.read().decode('utf-8')
    # m = re.search(r"src=.*\/(.*).png",buf)
    # print(m.groups())
    listurl = re.findall(r"src=\'(http.*.png)\'", buf)
    for url in listurl:
        f = open('data/' + str(index)+'.png', 'wb')
        req = urllib.request.Request(url=url, headers=headers)
        request = urllib.request.urlopen(req)
        buf = request.read()
        f.write(buf)
        f.close()

    time.sleep(random.randint(10, 100))
