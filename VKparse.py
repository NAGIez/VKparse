import requests 
import time
import pandas as pd
import json
from tqdm.notebook import tqdm
from datetime import datetime
from elasticsearch import Elasticsearch, helpers
from tqdm.auto import tqdm
from art import tprint

tprint("VK  Parser")
k = input('Введите название БД: ')
group_vk = input('Введите ссылку группы: vk.com/')

domains = {'DB_1' : group_vk}
url = 'https://api.vk.com/method/wall.get'
parts = {'access_token' : 'СЮДА КЛЮЧ',
         'v' : '5.131',
         'count' : 100,
         'offset' : 0}

ids = []
posts = [] 
likes = [] 
dates = [] 
comments = []
photos = [] 
views = []

parts['domain'] = domains.items()
inf_wall = requests.get(url, params = parts).json()
quantity_of_posts = inf_wall['response']['count']
for i in tqdm(range(0, quantity_of_posts - 1), desc = 'Загрузка постов',miniters=None, mininterval = 0.1, disable=False, unit='posts'):
    time.sleep(0.0001)
    inf_wall = requests.get(url, params = parts).json()
    for x in inf_wall['response']['items']:
        ids.append(x['id'])
        posts.append(x['text']) 
        dates.append(datetime.utcfromtimestamp(x['date']).strftime('%Y-%m-%dT%H:%M')) 
        likes.append(x['likes']['count']) 
        comments.append(x['comments']['count'])
        if 'views' in x:
            views.append(x['views']['count'])
        else:
            views.append('-----')
        try:
            if x['attachments'][0]['type'] == 'photo':
                max_width = x['attachments'][0]['photo']['sizes'][0]['width']
                index = 0
                index_1 = 0
                for y in x['attachments'][0]['photo']['sizes']:
                    if y['width'] >= max_width:
                        max_width = y['width']
                        index_1 = index
                    else:
                        continue
                    index += 1
                photos.append(x['attachments'][0]['photo']['sizes'][index_1]['url'])
            elif x['attachments'][0]['type'] == 'video':
                max_width = x['attachments'][0]['video']['image'][0]['width']
                index = 0
                index_1 = 0
                for y in x['attachments'][0]['video']['image']:
                    if y['width'] >= max_width:
                        max_width = y['width']
                        index_1 = index
                    else:
                        continue
                    index += 1
                photos.append(x['attachments'][0]['video']['image'][index_1]['url'])
            else:
                photos.append('-----')
        except:
            photos.append('-----')

    parts['offset'] += 100 
full_list = list(zip(ids, dates, likes, comments, views))

df = pd.DataFrame(full_list, columns = ['id_post', 
                                            'data', 
                                            'n_likes', 
                                            'n_comments', 
                                            'n_view'])
df.to_json(f'{k}.json', orient='records', lines=True)
df.to_excel(f'{k}.xlsx')
df.to_csv(f'{k}.csv', encoding='utf-8', index=False)

    
index_name = input('Введите название индекса: ')

filename = f'{k}.json'
es = Elasticsearch("http://localhost:9200", http_auth=('elastic', 'changeme'))

i = 1
f = open(filename)

for i in tqdm(range(0, i)):
    for line in f:
        es.index(index=index_name, ignore=400, doc_type='group_1', id=i, body=json.loads(line))
        i = i + 1

print('\nГотово!')