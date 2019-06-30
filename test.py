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

#https://www.blacked.com/videos
#https://www.vixen.com/videos
#https://www.tushy.com/videos

#http://www.heyzo.com/contents/3000/2007/images/player_thumbnail.jpg
#https://img.badoink.com/content/scenes/324586/star-wars-slave-leia-a-xxx-parody-324586.jpg?q=80&amp;w=960
