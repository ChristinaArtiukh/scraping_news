import requests
from bs4 import BeautifulSoup


def scraping_headers_pages():
    url = 'https://news.liga.net/'
    req = requests.get(url).text
    # # soup = BeautifulSoup(req, 'lxml')
    # with open('test.html', 'w', encoding='utf-8') as file:
    #     file.write(req)
    # with open('test.html', 'r', encoding='utf-8') as file:
    #     scr = file.read()
    news_data = []

    soup = BeautifulSoup(req, 'lxml')
    content = soup.find('div', class_="custom-tab-content active").find_all('div', class_="news-nth")
    for news in content:
        try:
            title = news.find('div', class_="news-nth-title news-time-var").find('a').text
        except Exception:
            title = 'Without title'
        try:
            link = news.find('a').get('href')
        except Exception:
            link = 'Without link'
        try:
            link_name = news.find('a').get('href')
            name = link_name.split('/')[-1]
        except Exception:
            name = 'Without link name'
        try:
            time = news.find('div', class_="news-nth-time").get('data-date')
        except Exception:
            time = 'Without time'
        news_data.append(
            {'title': title,
             'link': link,
             'name': name,
             'time': time
             }
        )
    return news_data


def return_name_link_for_page(url):
    req = requests.get(url).text
    # with open('posledniy-match-pered-evro-segodnya-sbornaya-ukrainy-sygraet-s-kiprom-gde-i-kogda-smotret.html', 'w', encoding='utf-8') as file:
    #     file.write(req)
    # with open('posledniy-match-pered-evro-segodnya-sbornaya-ukrainy-sygraet-s-kiprom-gde-i-kogda-smotret.html', 'r', encoding='utf-8') as file:
    #     req = file.read()
    news_data = []
    soup = BeautifulSoup(req, 'lxml')
    content = soup.find('div', class_="col-12 mt-20")
    try:
        title = content.find('h1').text
    except Exception:
        title = 'Without title'
    try:
        data = content.find('div', class_ ="article-time d-inline-flex").text
    except Exception:
        data = 'Without data'
    try:
        video = content.find('div', class_="row no-gutters").find('div', class_="col-12").find('iframe').get('src')
    except Exception:
        video = 'Without video'
    try:
        new_link = url.split('/')
        sub = 'liga.net'
        domain = next((s for s in new_link if sub in s), None)
        image_link = content.find('div', class_="row no-gutters").find('img').get('src')
        image = f'https://{domain}{image_link}'
    except Exception:
        image = 'Without image'
    try:
        text_content = content.find('div', class_="news-wrap opinion-end clearfix airSticky_stop-block").find('div', {
            'id': "news-text"}).text
    except Exception:
        text_content = 'Without text_content'
    try:
        authors = content.find('div', class_="news-wrap opinion-end clearfix airSticky_stop-block").find('div', {
            'id': "news-text"}).find('div', class_="authors").text
    except Exception:
        authors = 'Without authors'

    news_data.append({
        'title': title,
        'data': data,
        'video': video,
        'image': image,
        'text_content': text_content,
        'authors': authors,
    })
    return news_data


