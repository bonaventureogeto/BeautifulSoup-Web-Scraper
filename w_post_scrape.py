from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.coreyms.com/').text


soup = BeautifulSoup(source, 'lxml')


article = soup.find_all('article')


author = article.div.text
print(author)


# summary = article.find('div', class_='entry-content').p.text
# print(summary)

# vid_src = article.find('iframe', class_='youtube-player')['src']


# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]


# yt_link = f'https://youtube.com/watch?v={vid_id}'







