import requests
from scrapy.selector import Selector
splash_url = 'http://104.215.145.171:8050/render.html'
args = {'url':'https://www.1pondo.tv/list/?o=newest', 'timeout':5, 'image':0}
response = requests.get(splash_url, params=args)
sel = Selector(response)
print(response.text)

#sudo docker run -p 8050:8050 -p 8051:8051 scrapinghub/splash
#http://localhost:8050/render.html?url=https://www.1pondo.tv/list/?o=newest
#http://104.215.145.171:8050/render.html?url=https://www.1pondo.tv/list/?o=newest